# -*- coding: utf-8 -*-
"""
毕业论文仿真程序：数字通信系统调制方式仿真与性能分析
====================================================
内容：BPSK / QPSK / 16QAM 在 AWGN（加性高斯白噪声）与瑞利衰落信道下的
     蒙特卡洛误码率(BER)仿真，并与理论曲线对比。

运行方法（二选一）：
  1. PyCharm 中右键本文件 -> Run
  2. 命令行：python communication_sim.py

输出：4 张论文图，保存到上级目录的《结果图》文件夹
  图1 AWGN信道三种调制 BER 曲线（仿真 vs 理论）
  图2 QPSK 星座图随信噪比的变化
  图3 瑞利衰落 vs AWGN（含分集接收对比）
  图4 基带波形与眼图

依赖：numpy、matplotlib（pip install numpy matplotlib）
"""
import os
import math
import numpy as np
import matplotlib
matplotlib.use('Agg')                      # 后台出图，不弹窗（PyCharm 中更稳）
import matplotlib.pyplot as plt

# ---------- 中文显示设置（Windows 自带微软雅黑）----------
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei', 'SimHei', 'sans-serif']
plt.rcParams['axes.unicode_minus'] = False

OUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '结果图')
os.makedirs(OUT_DIR, exist_ok=True)

USE_DIVERSITY = True      # 是否仿真瑞利信道下 2 支路最大比合并(MRC)分集 —— 论文亮点实验
SEED = 2026               # 随机种子：固定后结果可复现（写进论文增加可信度）


# ============================================================
# 一、信源：随机比特发生器
# ============================================================
def gen_bits(n, rng):
    """产生 n 个等概 0/1 比特（信源模型：离散无记忆信源）"""
    return rng.integers(0, 2, n)


# ============================================================
# 二、调制器
# ============================================================
def bpsk_mod(bits):
    """BPSK：0 -> -1, 1 -> +1（符号能量 Es=1，比特能量 Eb=1）"""
    return (2.0 * bits - 1).astype(float)


def qpsk_mod(bits):
    """QPSK 格雷映射：每 2 比特 -> (I,Q)∈{(±1,±1)}，平均能量 Es=2 -> 每比特 Eb=1
       映射表：00->(+,+) 01->(+,-) 11->(-,-) 10->(-,+)  （相邻星座点只差1比特）"""
    b = bits.reshape(-1, 2)
    I = np.where(b[:, 0] == 1, 1.0, -1.0)
    Q = np.where(b[:, 1] == 1, 1.0, -1.0)
    return I + 1j * Q


def qam16_mod(bits):
    """16QAM 格雷映射：每 4 比特 -> (I,Q)∈{±1,±3}²
       能量归一化：原始平均能量 10，缩放 √(4/10) 后 Es=4 -> Eb=1"""
    b = bits.reshape(-1, 4)
    # 每两比特映射到 4 电平格雷码：00->-3 01->-1 11->+1 10->+3
    gray2level = {-3: (0, 0), -1: (0, 1), 1: (1, 1), 3: (1, 0)}
    level2bits = {v: k for k, v in gray2level.items()}
    def two_bits_to_level(bb):
        return level2bits[(int(bb[0]), int(bb[1]))]
    I = np.array([two_bits_to_level(x) for x in b[:, 0:2]], dtype=float)
    Q = np.array([two_bits_to_level(x) for x in b[:, 2:4]], dtype=float)
    scale = math.sqrt(4.0 / 10.0)
    return (I + 1j * Q) * scale


# ============================================================
# 三、信道
# ============================================================
def awgn(symbols, ebn0_db, bits_per_symbol):
    """AWGN 信道：r = s + n，n 的每维方差 σ² = N0/2
       归一化约定：Eb = 1（调制器已保证），N0 = 1/γb，γb=Eb/N0"""
    gamma_b = 10 ** (ebn0_db / 10.0)
    n0 = 1.0 / gamma_b
    sigma = math.sqrt(n0 / 2.0)
    noise = sigma * (np.random.standard_normal(symbols.shape)
                     + 1j * np.random.standard_normal(symbols.shape))
    return symbols + noise


def rayleigh(symbols, rng, ebn0_db, n_branch=1):
    """瑞利衰落信道（可选 MRC 分集）：每支路 r = h*s + n，h~CN(0,1)
       接收端理想信道估计（h 已知），MRC 合并。返回每支路的接收信号和信道增益"""
    gamma_b = 10 ** (ebn0_db / 10.0)
    n0 = 1.0 / gamma_b
    sigma = math.sqrt(n0 / 2.0)
    r_list, h_list = [], []
    for _ in range(n_branch):
        h = (rng.standard_normal(symbols.shape)
             + 1j * rng.standard_normal(symbols.shape)) / math.sqrt(2.0)
        n = sigma * (rng.standard_normal(symbols.shape)
                     + 1j * rng.standard_normal(symbols.shape))
        r_list.append(h * symbols + n)
        h_list.append(h)
    return r_list, h_list


# ============================================================
# 四、解调器（最近邻判决 + 格雷逆映射）
# ============================================================
def bpsk_demod(r):
    """BPSK 判决：实部>0 -> 1"""
    return (r.real > 0).astype(int)


def qpsk_demod(r):
    """QPSK 逆映射：I>0->b1=1, Q>0->b2=1（与调制表对应）"""
    b1 = (r.real > 0).astype(int)
    b2 = (r.imag > 0).astype(int)
    return np.stack([b1, b2], axis=1).reshape(-1)


def qam16_demod(r):
    """16QAM：判决到最近电平 ±1±3，再逆格雷映射回 4 比特"""
    scale = math.sqrt(4.0 / 10.0)
    x = r / scale
    def nearest(v):
        lv = np.array([-3, -1, 1, 3])
        idx = np.abs(v[:, None] - lv[None, :]).argmin(axis=1)
        return lv[idx]
    I = nearest(x.real)
    Q = nearest(x.imag)
    gray2level = {-3: (0, 0), -1: (0, 1), 1: (1, 1), 3: (1, 0)}
    out = np.zeros(len(I) * 4, dtype=int)
    for k in range(len(I)):
        a, b = gray2level[I[k]]
        c, d = gray2level[Q[k]]
        out[4 * k:4 * k + 4] = [a, b, c, d]
    return out


# ============================================================
# 五、理论误码率公式（论文第2章推导，第4章对照）
# ============================================================
def Q(x):
    return 0.5 * math.erfc(x / math.sqrt(2.0))

def theory_awgn_bpsk(g):
    return Q(math.sqrt(2.0 * g))            # Pb = Q(√(2γb))

def theory_awgn_qpsk(g):
    return Q(math.sqrt(2.0 * g))            # 格雷映射下与BPSK相同

def theory_awgn_qam16(g):
    # 方形M-QAM格雷映射近似式：Pb ≈ (4/k)(1-1/√M)·Q(√(3kγb/(M-1)))，M=16,k=4
    return (1 - 1 / 4.0) * Q(math.sqrt(3.0 * 4 * g / 15.0))

def theory_rayleigh_bpsk(g, L=1):
    """瑞利信道 BPSK 相干接收，L 支路 MRC 合并的精确闭式解"""
    mu = math.sqrt(g / (1.0 + g))
    if L == 1:
        return 0.5 * (1.0 - mu)
    # L 支路 MRC：Pb = ((1-μ)/2)·Σ_{i=0}^{L-1} C(L-1+i,i)·((1+μ)/2)^i
    from math import comb
    s = 0.0
    for i in range(L):
        s += comb(L - 1 + i, i) * ((1 + mu) / 2.0) ** i
    return ((1 - mu) / 2.0) * s


# ============================================================
# 六、蒙特卡洛统计
# ============================================================
def simulate_awgn(mode, ebn0_db, n_bits, rng):
    bits = gen_bits(n_bits, rng)
    if mode == 'BPSK':
        tx, rx, est = bpsk_mod(bits), None, None
        r = awgn(tx, ebn0_db, 1)
        est = bpsk_demod(r)
    elif mode == 'QPSK':
        tx = qpsk_mod(bits)
        r = awgn(tx, ebn0_db, 2)
        est = qpsk_demod(r)
    elif mode == '16QAM':
        tx = qam16_mod(bits)
        r = awgn(tx, ebn0_db, 4)
        est = qam16_demod(r)
    else:
        raise ValueError(mode)
    return np.mean(est != bits)             # BER = 错误比特数/总比特数


def simulate_rayleigh_bpsk(ebn0_db, n_bits, rng, n_branch=1):
    """瑞利信道 BPSK + L 支路 MRC。返回 BER"""
    bits = gen_bits(n_bits, rng)
    s = bpsk_mod(bits)
    r_list, h_list = rayleigh(s, rng, ebn0_db, n_branch)
    # MRC 合并（实信号）：z = Σ Re{h* · r} / Σ|h|²  -> 等效判决量
    z = sum((h.conjugate() * r).real for h, r in zip(h_list, r_list))
    denom = sum((np.abs(h) ** 2) for h in h_list)
    z = z / denom
    est = (z > 0).astype(int)
    return np.mean(est != bits)


# ============================================================
# 主实验
# ============================================================
def main():
    rng = np.random.default_rng(SEED)
    ebn0s = np.arange(0, 13, 1.0)           # AWGN：0~12 dB
    print('=' * 60)
    print('实验1：AWGN 信道 BPSK / QPSK / 16QAM 误码率仿真')
    print('=' * 60)

    # ---- 图1：AWGN BER 曲线 ----
    plt.figure(figsize=(8, 5.5))
    markers = {'BPSK': 'o', 'QPSK': 's', '16QAM': '^'}
    colors = {'BPSK': '#4C72B0', 'QPSK': '#55A868', '16QAM': '#DD8452'}
    results_table = {}
    for mode in ['BPSK', 'QPSK', '16QAM']:
        n_bits = 2_000_000 if mode != '16QAM' else 2_000_000
        bers = []
        for db in ebn0s:
            # 低误码率处增加样本量（经验：至少 100/BER 个比特）
            nb = int(min(max(n_bits, 0), 6_000_000))
            ber = simulate_awgn(mode, db, nb, rng)
            bers.append(ber)
            print(f'  {mode:6s} Eb/N0={db:4.1f} dB   BER={ber:.3e}')
        results_table[mode] = bers
        g = 10 ** (ebn0s / 10)
        theory = [theory_awgn_bpsk(x) if mode == 'BPSK'
                  else theory_awgn_qpsk(x) if mode == 'QPSK'
                  else theory_awgn_qam16(x) for x in g]
        plt.semilogy(ebn0s, theory, '-', color=colors[mode], lw=1.8,
                     label=f'{mode} 理论')
        plt.semilogy(ebn0s, bers, markers[mode], color=colors[mode], ms=8,
                     mfc='none', mew=1.8, label=f'{mode} 仿真')
    plt.grid(True, which='both', alpha=0.3)
    plt.xlabel('Eb/N0 (dB)'); plt.ylabel('误比特率 BER')
    plt.title('图1  AWGN 信道下三种调制的 BER 曲线（蒙特卡洛 200 万比特/点）')
    plt.legend(); plt.ylim(1e-6, 1)
    plt.tight_layout()
    plt.savefig(os.path.join(OUT_DIR, '图1_AWGN误码率曲线.png'), dpi=200)
    plt.close()
    print('  -> 已保存 图1_AWGN误码率曲线.png')

    # ---- 图2：QPSK 星座图 ----
    print('\n实验2：QPSK 接收星座图（直观展示噪声影响）')
    fig, axes = plt.subplots(1, 4, figsize=(13, 3.6))
    for ax, db in zip(axes, [0, 4, 8, 12]):
        bits = gen_bits(4000, rng)
        tx = qpsk_mod(bits)
        r = awgn(tx, db, 2)
        ax.plot(r.real, r.imag, '.', ms=3, alpha=0.5, color='#4C72B0')
        ax.plot([1, -1, 1, -1], [1, 1, -1, -1], 'k+', ms=12, mew=2)
        ax.set_title(f'Eb/N0 = {db} dB'); ax.set_xlabel('I'); ax.set_ylabel('Q')
        ax.set_xlim(-2.8, 2.8); ax.set_ylim(-2.8, 2.8); ax.set_aspect('equal'); ax.grid(alpha=0.3)
    fig.suptitle('图2  QPSK 星座图：信噪比越高，接收点越向 4 个理想星座点（+号）聚拢', y=1.04)
    plt.tight_layout()
    plt.savefig(os.path.join(OUT_DIR, '图2_QPSK星座图.png'), dpi=200, bbox_inches='tight')
    plt.close()
    print('  -> 已保存 图2_QPSK星座图.png')

    # ---- 图3：瑞利衰落与分集 ----
    print('\n实验3：瑞利衰落信道 vs AWGN（含2支路MRC分集）')
    ebn0_r = np.arange(0, 31, 2.0)
    ber_ray, ber_ray_div = [], []
    for db in ebn0_r:
        ber_ray.append(simulate_rayleigh_bpsk(db, 400_000, rng, 1))
        if USE_DIVERSITY:
            ber_ray_div.append(simulate_rayleigh_bpsk(db, 400_000, rng, 2))
        print(f'  瑞利BPSK Eb/N0={db:4.1f} dB   无分集BER={ber_ray[-1]:.3e}'
              + (f'   2支路MRC BER={ber_ray_div[-1]:.3e}' if USE_DIVERSITY else ''))
    plt.figure(figsize=(8, 5.5))
    g = 10 ** (ebn0_r / 10)
    plt.semilogy(ebn0_r, [theory_rayleigh_bpsk(x, 1) for x in g], '-', color='#C44E52', lw=1.8,
                 label='瑞利 理论(无分集)')
    plt.semilogy(ebn0_r, ber_ray, 'o', color='#C44E52', ms=7, mfc='none', mew=1.8,
                 label='瑞利 仿真(无分集)')
    if USE_DIVERSITY:
        plt.semilogy(ebn0_r, [theory_rayleigh_bpsk(x, 2) for x in g], '-', color='#8172B2', lw=1.8,
                     label='瑞利 理论(2支路MRC)')
        plt.semilogy(ebn0_r, ber_ray_div, 's', color='#8172B2', ms=7, mfc='none', mew=1.8,
                     label='瑞利 仿真(2支路MRC)')
    plt.semilogy(ebn0_r, [theory_awgn_bpsk(x) for x in g], '--', color='#4C72B0', lw=1.8,
                 label='AWGN 理论(BPSK)')
    plt.grid(True, which='both', alpha=0.3)
    plt.xlabel('Eb/N0 (dB)'); plt.ylabel('误比特率 BER')
    plt.title('图3  瑞利衰落 vs AWGN：衰落代价与分集增益')
    plt.legend(); plt.ylim(1e-5, 1)
    plt.tight_layout()
    plt.savefig(os.path.join(OUT_DIR, '图3_瑞利信道与分集.png'), dpi=200)
    plt.close()
    print('  -> 已保存 图3_瑞利信道与分集.png')

    # ---- 图4：波形 + 眼图 ----
    print('\n实验4：基带发送/接收波形与眼图')
    sps = 32                                   # 每比特采样点数（成型滤波用）
    bits = gen_bits(40, rng)
    s = bpsk_mod(bits)
    # 升余弦成型（简易实现：矩形脉冲+升余弦滚降滤波）
    beta = 0.35
    t = np.arange(-4 * sps, 4 * sps + 1) / sps
    with np.errstate(divide='ignore', invalid='ignore'):
        h = np.sinc(t) * np.cos(np.pi * beta * t) / (1 - (2 * beta * t) ** 2)
    h[~np.isfinite(h)] = 0
    h /= np.sqrt(np.sum(h ** 2))               # 单位能量
    tx_wave = np.convolve(s, h)[:len(s) * sps]
    snr_db = 8
    sigma = math.sqrt((10 ** (-snr_db / 10)) / 2 / sps * 1.0)  # 匹配Eb/N0（近似演示）
    rx_wave = tx_wave + sigma * rng.standard_normal(len(tx_wave))
    fig, axes = plt.subplots(2, 1, figsize=(10, 6))
    tt = np.arange(len(tx_wave)) / sps
    axes[0].plot(tt, tx_wave, lw=1.2, color='#4C72B0', label='发送基带波形（升余弦成型 β=0.35）')
    axes[0].plot(tt, rx_wave, lw=0.6, alpha=0.6, color='#C44E52', label=f'接收波形（Eb/N0={snr_db}dB）')
    axes[0].legend(fontsize=9); axes[0].set_xlabel('t / Tb'); axes[0].set_ylabel('幅度')
    axes[0].set_title('图4a  BPSK 基带发送与接收波形')
    for k in range(4 * sps, len(rx_wave) - 2 * sps, sps):
        axes[1].plot(np.arange(2 * sps) / sps, rx_wave[k:k + 2 * sps], lw=0.7, alpha=0.3,
                     color='#55A868')
    axes[1].set_title('图4b  接收信号眼图（眼睛张开度反映噪声容限）')
    axes[1].set_xlabel('t / Tb'); axes[1].set_ylabel('幅度')
    plt.tight_layout()
    plt.savefig(os.path.join(OUT_DIR, '图4_波形与眼图.png'), dpi=200)
    plt.close()
    print('  -> 已保存 图4_波形与眼图.png')

    # ---- 汇总表（可直接抄进论文）----
    print('\n' + '=' * 60)
    print('AWGN 误码率汇总表（论文表4-1 可直接使用）')
    print(f"{'Eb/N0(dB)':>10} {'BPSK':>12} {'QPSK':>12} {'16QAM':>12}")
    for i, db in enumerate(ebn0s):
        row = ' '.join(f'{results_table[m][i]:12.3e}' for m in ['BPSK', 'QPSK', '16QAM'])
        print(f'{db:10.1f} {row}')
    print('=' * 60)
    print(f'全部完成！结果图保存在：{os.path.abspath(OUT_DIR)}')


if __name__ == '__main__':
    main()
