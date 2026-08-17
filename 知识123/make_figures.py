# -*- coding: utf-8 -*-
"""生成通信工程知识库全部教学插图，输出到 通信工程知识库/images 目录"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, RegularPolygon, FancyArrowPatch, Rectangle
import math, os

plt.rcParams['font.sans-serif'] = ['Microsoft YaHei', 'SimHei', 'sans-serif']
plt.rcParams['axes.unicode_minus'] = False

OUT = r'E:\知识123\通信工程知识库\images'
os.makedirs(OUT, exist_ok=True)

def save(fig, name):
    fig.savefig(os.path.join(OUT, name), dpi=130, bbox_inches='tight')
    plt.close(fig)
    print('saved', name)

def Qfunc(x):
    return 0.5 * math.erfc(x / math.sqrt(2))

# ============ 00 通信系统框图 ============
fig, ax = plt.subplots(figsize=(11, 3.2))
ax.axis('off')
blocks = [('信息源', 0.02), ('信源编码', 0.17), ('信道编码', 0.32), ('调制', 0.47),
          ('信道+噪声', 0.62), ('解调', 0.77), ('信宿', 0.92)]
for txt, x in blocks:
    color = '#4C72B0' if txt != '信道+噪声' else '#C44E52'
    ax.add_patch(Rectangle((x, 0.32), 0.11, 0.36, facecolor=color, edgecolor='k',
                           transform=ax.transAxes, clip_on=False, zorder=3))
    ax.text(x + 0.055, 0.5, txt, ha='center', va='center', color='w',
            fontsize=12, transform=ax.transAxes, zorder=4)
for i in range(len(blocks) - 1):
    x1 = blocks[i][1] + 0.11
    x2 = blocks[i + 1][1]
    ax.annotate('', xy=(x2, 0.5), xytext=(x1, 0.5), xycoords=ax.transAxes,
                arrowprops=dict(arrowstyle='->', lw=1.8), zorder=2)
ax.annotate('噪声 n(t)', xy=(0.675, 0.70), xytext=(0.675, 0.95), xycoords=ax.transAxes,
            arrowprops=dict(arrowstyle='->', color='#C44E52', lw=1.8), fontsize=12, color='#C44E52')
ax.text(0.055, 0.15, '发送设备', ha='center', fontsize=11, transform=ax.transAxes)
ax.text(0.545, 0.15, '发送端', ha='center', fontsize=11, transform=ax.transAxes)
ax.text(0.825, 0.15, '接收端', ha='center', fontsize=11, transform=ax.transAxes)
ax.set_xlim(0, 1); ax.set_ylim(0, 1)
save(fig, '00_通信系统框图.png')

# ============ 01 正弦信号 ============
fig, axes = plt.subplots(1, 2, figsize=(11, 3.6))
t = np.linspace(0, 1, 1000)
s = 2 * np.cos(2 * np.pi * 3 * t + np.pi / 3)
axes[0].plot(t, s, lw=2, color='#4C72B0')
axes[0].axhline(0, color='gray', lw=0.8)
axes[0].annotate('', xy=(0.583, 2), xytext=(0.583, 0), arrowprops=dict(arrowstyle='<->', color='red'))
axes[0].text(0.60, 1.0, '振幅 A=2', color='red', fontsize=11)
axes[0].annotate('', xy=(0.167, -2.6), xytext=(0.5, -2.6), arrowprops=dict(arrowstyle='<->', color='green'))
axes[0].text(0.24, -3.4, '周期 T=1/3 s', color='green', fontsize=11)
axes[0].set_title(r'$s(t)=2\cos(2\pi\cdot 3t+\pi/3)$  振幅/频率/相位', fontsize=12)
axes[0].set_xlabel('t (s)'); axes[0].set_ylabel('幅度')
t2 = np.linspace(0, 1, 1000)
axes[1].plot(t2, np.cos(2 * np.pi * 2 * t2), '--', lw=1.5, label=r'$\cos(2\pi 2t)$', color='gray')
axes[1].plot(t2, np.cos(2 * np.pi * 2 * t2 + np.pi / 2), lw=2,
             label=r'$\cos(2\pi 2t+\pi/2)=-\sin(2\pi 2t)$', color='#DD8452')
axes[1].legend(fontsize=10); axes[1].axhline(0, color='gray', lw=0.8)
axes[1].set_title('相位差 π/2 的两个同频正弦波', fontsize=12)
axes[1].set_xlabel('t (s)')
plt.tight_layout()
save(fig, '01_正弦信号.png')

# ============ 02 周期方波频谱 ============
fig, axes = plt.subplots(1, 2, figsize=(11, 3.6))
t = np.linspace(-1.5, 1.5, 3000)
nmax = 7
sq = np.zeros_like(t)
for n in range(1, nmax + 1, 2):
    sq += 4 / (np.pi * n) * np.sin(2 * np.pi * n * t)
axes[0].plot(t, np.sign(np.sin(np.pi * t)), lw=2, color='gray', alpha=0.6, label='理想方波')
axes[0].plot(t, sq, lw=2, color='#4C72B0', label='取1~7次谐波合成')
axes[0].legend(fontsize=10); axes[0].set_ylim(-1.6, 1.6)
axes[0].set_title('方波的傅里叶级数合成（吉布斯现象）', fontsize=12)
axes[0].set_xlabel('t (s)')
n = np.arange(1, 16, 2)
mag = 4 / (np.pi * n)
axes[1].stem(n, mag, basefmt=' ')
axes[1].set_title('幅度谱：只在奇次谐波有谱线，按 1/n 衰减', fontsize=12)
axes[1].set_xlabel('谐波次数 n'); axes[1].set_ylabel('|b_n|')
plt.tight_layout()
save(fig, '02_频谱_周期方波.png')

# ============ 03 采样定理 ============
fig, axes = plt.subplots(1, 2, figsize=(11, 3.6))
fs = 10.0
t = np.linspace(0, 1, 1000)
for ax, f, title in [(axes[0], 2, 'f=2Hz < fs/2=5Hz：可完美恢复（不混叠）'),
                     (axes[1], 7, 'f=7Hz > fs/2=5Hz：采样后看起来像 3Hz（混叠！）')]:
    x = np.cos(2 * np.pi * f * t)
    n = np.arange(0, 1, 1 / fs)
    xs = np.cos(2 * np.pi * f * n)
    ax.plot(t, x, lw=1, color='gray', alpha=0.7)
    ax.plot(n, xs, 'o', ms=7, color='#C44E52')
    alias_f = abs(f - fs * round(f / fs))
    ta = np.linspace(0, 1, 500)
    ax.plot(ta, 0.9 * np.cos(2 * np.pi * alias_f * ta + np.pi), '--', lw=1.2, color='#55A868')
    ax.set_title(title, fontsize=12); ax.set_xlabel('t (s)')
    ax.plot([], [], 'o', color='#C44E52', label='采样点')
    ax.plot([], [], '--', color='#55A868', label='混叠信号 %gHz' % alias_f)
    ax.legend(fontsize=9)
plt.tight_layout()
save(fig, '03_采样定理.png')

# ============ 04 卷积图解 ============
fig, axes = plt.subplots(1, 3, figsize=(12, 3.4))
tt = np.linspace(-1, 5, 1000)
x = np.where((tt >= 0) & (tt <= 1), 1.0, 0.0)
h = np.where(tt >= 0, np.exp(-1.5 * tt), 0.0)
axes[0].plot(tt, x, lw=2); axes[0].set_title('输入 x(t)：单位矩形', fontsize=12)
axes[1].plot(tt, h, lw=2, color='#DD8452'); axes[1].set_title('系统 h(t)=e^{-1.5t}u(t)', fontsize=12)
y = np.where(tt < 1, (1 - np.exp(-1.5 * tt)) / 1.5, (np.exp(1.5) - 1) / 1.5 * np.exp(-1.5 * tt))
y = np.where(tt >= 0, y, 0)
axes[2].plot(tt, y, lw=2, color='#55A868')
axes[2].fill_between(tt, 0, y, alpha=0.15, color='#55A868')
axes[2].set_title('输出 y(t)=x(t)*h(t)', fontsize=12)
for ax in axes:
    ax.set_xlabel('t'); ax.axhline(0, color='gray', lw=0.8)
plt.tight_layout()
save(fig, '04_卷积图解.png')

# ============ 05 滤波器响应 ============
fig, axes = plt.subplots(1, 2, figsize=(11, 3.6))
f = np.linspace(0, 4, 1000)
for order, color in [(2, '#4C72B0'), (4, '#DD8452'), (8, '#55A868')]:
    H = 1 / np.sqrt(1 + f ** (2 * order))
    axes[0].plot(f, H, lw=2, label='n=%d 阶巴特沃斯' % order, color=color)
axes[0].axvline(1, ls='--', color='gray'); axes[0].text(1.05, 0.5, '截止频率 fc', fontsize=10)
axes[0].legend(fontsize=9); axes[0].set_title('低通滤波器幅频响应', fontsize=12)
axes[0].set_xlabel('f/fc'); axes[0].set_ylabel('|H(f)|')
f2 = np.linspace(0, 10, 2000)
f0, B = 5.0, 2.0
Hbp = 1 / np.sqrt(1 + ((f2 - f0) / (B / 2)) ** 6)
axes[1].plot(f2, Hbp, lw=2, color='#C44E52')
axes[1].fill_betweenx([0, 1.02], f0 - B / 2, f0 + B / 2, alpha=0.12, color='#C44E52')
axes[1].text(f0, 0.55, '通带宽度 B=2Hz\n中心 f0=5Hz', ha='center', fontsize=10)
axes[1].set_title('带通滤波器：只放行某一频段', fontsize=12)
axes[1].set_xlabel('f (Hz)'); axes[1].set_ylabel('|H(f)|')
plt.tight_layout()
save(fig, '05_滤波器响应.png')

# ============ 06 DFT频谱分析 ============
fig, axes = plt.subplots(1, 2, figsize=(11, 3.6))
fs, N = 1000.0, 1024
n = np.arange(N)
sig = np.cos(2 * np.pi * 50 * n / fs) + 0.7 * np.cos(2 * np.pi * 120 * n / fs) \
    + 0.5 * np.random.randn(N)
axes[0].plot(n[:200] / fs, sig[:200], lw=0.8, color='#4C72B0')
axes[0].set_title('时域波形（前0.2s）：看不出成分', fontsize=12)
axes[0].set_xlabel('t (s)')
sp = np.abs(np.fft.fft(sig)) / N
freq = np.fft.fftfreq(N, 1 / fs)
mask = freq >= 0
axes[1].plot(freq[mask], sp[mask] * 2, lw=1, color='#C44E52')
axes[1].set_title('DFT 幅度谱：50Hz 与 120Hz 两个分量一目了然', fontsize=12)
axes[1].set_xlabel('f (Hz)'); axes[1].set_ylabel('幅度')
plt.tight_layout()
save(fig, '06_DFT频谱分析.png')

# ============ 07 AM调制 ============
fig, axes = plt.subplots(1, 2, figsize=(11, 3.6))
t = np.linspace(0, 1, 2000)
fm, fc, ma = 2.0, 20.0, 0.5
m = np.cos(2 * np.pi * fm * t)
s = (1 + ma * m) * np.cos(2 * np.pi * fc * t)
axes[0].plot(t, s, lw=0.9, color='#4C72B0')
axes[0].plot(t, 1 + ma * m, '--', lw=1.4, color='#C44E52', label='上包络')
axes[0].plot(t, -(1 + ma * m), '--', lw=1.4, color='#C44E52')
axes[0].legend(fontsize=9)
axes[0].set_title('AM 已调波：包络 = 调制信号', fontsize=12)
axes[0].set_xlabel('t (s)')
fn = [-fc - fm, -fc, -fc + fm, fc - fm, fc, fc + fm]
mag = [ma / 2, 1, ma / 2, ma / 2, 1, ma / 2]
axes[1].stem(fn, mag, basefmt=' ')
axes[1].set_title('频谱：载波 + 上下边带', fontsize=12)
axes[1].set_xlabel('f (Hz)'); axes[1].set_ylabel('相对幅度')
plt.tight_layout()
save(fig, '07_AM调制.png')

# ============ 08 数字基带码型 ============
bits = [1, 0, 1, 1, 0, 0, 1, 0]
fig, axes = plt.subplots(4, 1, figsize=(11, 7), sharex=True)
def draw_code(ax, code, title):
    x = np.arange(len(code) + 1)
    ax.step(x, code + [code[-1]], where='post', lw=2)
    ax.set_ylim(-1.6, 1.6); ax.set_yticks([-1, 0, 1])
    ax.set_title(title, fontsize=11, loc='left')
    ax.grid(axis='x', alpha=0.3)
uni = [b for b in bits]
bi = [1 if b else -1 for b in bits]
rz = []
for b in bits:
    rz += [b, 0]
diff, prev = [], 0
for b in bits:
    prev = 1 - prev if b else prev
    diff.append(prev)
draw_code(axes[0], uni, '① 单极性NRZ（有直流）')
axes[0].step(np.arange(len(rz) + 1), rz + [0], where='post', lw=1.6, alpha=0)  # keep x scale
axes[0].set_title('① 单极性NRZ（有直流分量，0=无脉冲 1=有脉冲）', fontsize=11, loc='left')
draw_code(axes[1], bi, '② 双极性NRZ（+1 / -1，抗干扰更好）')
xr = np.arange(len(rz) + 1) / 2
axes[2].step(xr, rz + [0], where='post', lw=2)
axes[2].set_ylim(-0.3, 1.6); axes[2].set_yticks([0, 1])
axes[2].set_title('③ 单极性RZ（归零码，每位中间回到0，利于提取时钟）', fontsize=11, loc='left')
axes[2].grid(axis='x', alpha=0.3)
draw_code(axes[3], diff, '④ 差分码（遇1翻转遇0保持，解决相位模糊）')
axes[3].set_xticks(np.arange(9)); axes[3].set_xticklabels([''] + [str(b) for b in bits])
axes[3].set_xlabel('比特：1 0 1 1 0 0 1 0')
plt.tight_layout()
save(fig, '08_数字基带码型.png')

# ============ 09 ASK/FSK/PSK ============
bits = [1, 0, 1, 1, 0, 0, 1]
fig, axes = plt.subplots(3, 1, figsize=(11, 7), sharex=True)
sps = 100
t = np.arange(len(bits) * sps) / sps  # 单位：比特
def seg_wave(freq_per_bit, amp_on=1.0, phase_flip=False):
    y = np.zeros_like(t)
    phase = 0.0
    for i, b in enumerate(bits):
        tt = np.arange(sps) / sps
        if phase_flip and b == 1:
            phase += np.pi
        y[i * sps:(i + 1) * sps] = (amp_on if (b or not amp_on is None and amp_on == 1) else 0)
    return y
# 2ASK
y_ask = np.zeros_like(t)
for i, b in enumerate(bits):
    tt = np.arange(sps) / sps
    if b == 1:
        y_ask[i * sps:(i + 1) * sps] = np.cos(2 * np.pi * 2 * tt)
axes[0].plot(t, y_ask, lw=1.2, color='#4C72B0')
axes[0].set_title('2ASK（幅移键控）：1→有载波，0→无载波', fontsize=12, loc='left')
# 2FSK
y_fsk = np.zeros_like(t)
for i, b in enumerate(bits):
    tt = np.arange(sps) / sps
    f = 3 if b == 1 else 1.5
    y_fsk[i * sps:(i + 1) * sps] = np.cos(2 * np.pi * f * tt)
axes[1].plot(t, y_fsk, lw=1.2, color='#DD8452')
axes[1].set_title('2FSK（频移键控）：1→高频，0→低频', fontsize=12, loc='left')
# 2PSK
y_psk = np.zeros_like(t)
phase = 0.0
for i, b in enumerate(bits):
    tt = np.arange(sps) / sps
    if b == 1:
        phase += np.pi
    y_psk[i * sps:(i + 1) * sps] = np.cos(2 * np.pi * 2 * tt + phase)
axes[2].plot(t, y_psk, lw=1.2, color='#55A868')
axes[2].set_title('2PSK（相移键控）：1→相位翻转180°', fontsize=12, loc='left')
axes[2].set_xlabel('比特序号'); axes[2].set_xticks(np.arange(len(bits)) + 0.5)
axes[2].set_xticklabels([str(b) for b in bits])
for ax in axes:
    ax.axhline(0, color='gray', lw=0.6)
    for i in range(1, len(bits)):
        ax.axvline(i, color='gray', ls=':', lw=0.8)
plt.tight_layout()
save(fig, '09_ASK_FSK_PSK.png')

# ============ 10 QPSK星座图 ============
fig, ax = plt.subplots(figsize=(5.2, 5))
pts = [(1, 1, '00'), (-1, 1, '01'), (-1, -1, '11'), (1, -1, '10')]
for I, Qx, lab in pts:
    ax.plot(I / np.sqrt(2), Qx / np.sqrt(2), 'o', ms=14, color='#4C72B0')
    ax.text(I / np.sqrt(2) + 0.07, Qx / np.sqrt(2) + 0.07, lab, fontsize=13)
ax.axhline(0, color='gray'); ax.axvline(0, color='gray')
ax.set_xlim(-1.3, 1.3); ax.set_ylim(-1.3, 1.3); ax.set_aspect('equal')
ax.grid(alpha=0.3)
ax.set_xlabel('同相分量 I'); ax.set_ylabel('正交分量 Q')
ax.set_title('QPSK 星座图：2个比特 → 4个相位', fontsize=13)
save(fig, '10_QPSK星座图.png')

# ============ 11 16QAM星座图 ============
fig, ax = plt.subplots(figsize=(5.6, 5.6))
levels = [-3, -1, 1, 3]
for I in levels:
    for Qx in levels:
        ax.plot(I, Qx, 's', ms=11, color='#C44E52')
ax.axhline(0, color='gray'); ax.axvline(0, color='gray')
ax.set_xlim(-4.2, 4.2); ax.set_ylim(-4.2, 4.2); ax.set_aspect('equal')
ax.grid(alpha=0.3)
ax.set_xlabel('I 路'); ax.set_ylabel('Q 路')
ax.set_title('16QAM 星座图：4个比特 → 16个幅度/相位组合', fontsize=13)
save(fig, '11_16QAM星座图.png')

# ============ 12 眼图 ============
rng = np.random.default_rng(7)
sps = 20
Nsym = 400
syms = rng.choice([-1, 1], Nsym)
beta = 0.35
span = 6
tp = np.arange(-span * sps, span * sps + 1) / sps
with np.errstate(divide='ignore', invalid='ignore'):
    h = np.sinc(tp) * np.cos(np.pi * beta * tp) / (1 - (2 * beta * tp) ** 2)
h[~np.isfinite(h)] = np.pi / 4 * np.sinc(1 / (2 * beta)) * np.cos(np.pi / 2) / 1  # 极限值
h = h / np.sqrt(np.sum(h ** 2) / sps)
y = np.convolve(syms, h)[: Nsym * sps + span * sps]
fig, ax = plt.subplots(figsize=(8, 4.5))
for k in range(span * sps, len(y) - 2 * sps, sps):
    seg = y[k:k + 2 * sps]
    ax.plot(np.arange(len(seg)) / sps, seg, lw=0.7, alpha=0.25, color='#4C72B0')
ax.set_title('眼图：张得越开，码间串扰越小，最佳抽样时刻在"眼睛"最大处', fontsize=12)
ax.set_xlabel('t / Tb（2个比特周期）'); ax.set_ylabel('幅度')
save(fig, '12_眼图.png')

# ============ 13 升余弦滤波器 ============
fig, axes = plt.subplots(1, 2, figsize=(11, 3.6))
f = np.linspace(0, 2, 2000)
for beta, color in [(0.0, '#4C72B0'), (0.5, '#DD8452'), (1.0, '#55A868')]:
    H = np.where(f <= (1 - beta) / 2, 1.0,
                 np.where(f < (1 + beta) / 2,
                          0.5 * (1 + np.cos(np.pi * 1 / (2 * beta) * (2 * f - 1 + beta)) if beta > 0 else 0),
                          0.0))
    axes[0].plot(f, H, lw=2, label='β=%.1f' % beta, color=color)
axes[0].set_title('升余弦滚降幅频响应（滚降系数β）', fontsize=12)
axes[0].set_xlabel('f × Tb'); axes[0].legend(fontsize=10)
tt = np.arange(-6, 6.01, 0.05)
for beta, color in [(0.35, '#4C72B0'), (1.0, '#C44E52')]:
    with np.errstate(divide='ignore', invalid='ignore'):
        hh = np.sinc(tt) * np.cos(np.pi * beta * tt) / (1 - (2 * beta * tt) ** 2)
    hh[~np.isfinite(hh)] = 0
    axes[1].plot(tt, hh, lw=2, label='β=%.2f' % beta, color=color)
axes[1].set_title('升余弦冲激响应：尾部衰减快→对定时误差不敏感', fontsize=12)
axes[1].set_xlabel('t / Tb'); axes[1].legend(fontsize=10)
plt.tight_layout()
save(fig, '13_升余弦滤波器.png')

# ============ 14 香农容量曲线 ============
fig, ax = plt.subplots(figsize=(7.5, 4))
snr_db = np.linspace(0, 30, 300)
snr = 10 ** (snr_db / 10)
C = np.log2(1 + snr)
ax.plot(snr_db, C, lw=2.5, color='#4C72B0')
for db in [0, 10, 20, 30]:
    c = np.log2(1 + 10 ** (db / 10))
    ax.plot(db, c, 'o', color='#C44E52')
    ax.annotate('%.1f dB → %.2f bit/s/Hz' % (db, c), xy=(db, c),
                xytext=(db - 4, c + 3), fontsize=10,
                arrowprops=dict(arrowstyle='->', color='gray'))
ax.set_xlabel('信噪比 SNR (dB)'); ax.set_ylabel('频谱效率 C/B (bit/s/Hz)')
ax.set_title(r'香农公式：$C = B\cdot\log_2(1+\mathrm{SNR})$ —— 信道容量的极限', fontsize=13)
ax.grid(alpha=0.3)
save(fig, '14_香农容量曲线.png')

# ============ 15 BER曲线（理论+仿真） ============
fig, ax = plt.subplots(figsize=(8, 5))
ebn0_db = np.linspace(0, 10, 45)
g = 10 ** (ebn0_db / 10)
pb_bpsk = [Qfunc(math.sqrt(2 * x)) for x in g]
pb_fsk = [Qfunc(math.sqrt(x)) for x in g]
pb_ask = [Qfunc(math.sqrt(x / 2)) for x in g]
ax.semilogy(ebn0_db, pb_bpsk, lw=2, color='#4C72B0', label='2PSK 理论: ½erfc(√(γ))')
ax.semilogy(ebn0_db, pb_fsk, lw=2, color='#55A868', label='2FSK 理论: ½erfc(√(γ/2))')
ax.semilogy(ebn0_db, pb_ask, lw=2, color='#DD8452', label='2ASK 理论: ½erfc(√(γ/4))')
# 蒙特卡洛仿真 BPSK
rng = np.random.default_rng(2026)
sim_db, sim_ber = [], []
for db in range(0, 11):
    n_bits = 2_000_00 if db >= 7 else 100_000
    bits_ = rng.integers(0, 2, n_bits * 2)
    s = (2 * bits_ - 1).astype(float)          # BPSK: 0→-1, 1→+1 (Eb=1)
    n0 = 1 / (10 ** (db / 10))                 # Eb/N0 = γ
    noise = np.sqrt(n0 / 2) * rng.standard_normal(s.shape)
    r = s + noise
    est = (r > 0).astype(int)
    ber = np.mean(est != bits_)
    sim_db.append(db); sim_ber.append(max(ber, 1e-7))
ax.semilogy(sim_db, sim_ber, 'o', ms=8, mfc='none', mew=2, color='#C44E52', label='BPSK 蒙特卡洛仿真点')
ax.set_xlabel('Eb/N0 (dB)'); ax.set_ylabel('误比特率 BER')
ax.set_title('AWGN 信道误码率曲线（γ = Eb/N0）', fontsize=13)
ax.grid(True, which='both', alpha=0.3); ax.legend(fontsize=10)
ax.set_ylim(1e-6, 1)
save(fig, '15_BER曲线.png')

# ============ 16 电磁波频谱 ============
fig, ax = plt.subplots(figsize=(12, 3.6))
bands = [
    (3, 30, '甚低频 VLF\n(潜艇通信)', '#8C8C8C'),
    (30, 300, '低频 LF\n(AM广播/导航)', '#4C72B0'),
    (300, 3000, '中频 MF\n(中波广播)', '#DD8452'),
    (3e3, 30e3, '高频 HF\n(短波/远距离)', '#55A868'),
    (30e3, 300e3, '甚高频 VHF\n(FM/电视)', '#C44E52'),
    (300e3, 3e6, '特高频 UHF\n(手机/WiFi/GPS)', '#8172B2'),
    (3e6, 30e6, '超高频 SHF\n(微波雷达/卫星)', '#937860'),
    (30e6, 300e6, '极高频 EHF\n(毫米波/5G)', '#DA8BC3'),
]
for f1, f2, name, color in bands:
    ax.fill_betweenx([0.25, 0.75], np.log10(f1), np.log10(f2), alpha=0.85, color=color)
    ax.text((np.log10(f1) + np.log10(f2)) / 2, 0.5, name, ha='center', va='center',
            color='w', fontsize=9)
ax.set_xlim(np.log10(3), np.log10(3e8)); ax.set_ylim(0, 1)
ax.set_yticks([])
xt = [3, 30, 300, 3e3, 30e3, 300e3, 3e6, 30e6, 300e6]
ax.set_xticks([np.log10(x) for x in xt])
ax.set_xticklabels(['3Hz', '30', '300', '3k', '30k', '300k', '3M', '30M', '300M'])
ax.set_title('电磁波频谱划分与典型应用（频率：Hz，对数刻度）', fontsize=13)
save(fig, '16_电磁波频谱.png')

# ============ 17 多径与瑞利衰落 ============
fig, axes = plt.subplots(1, 2, figsize=(11, 3.6))
f = np.linspace(0, 20, 2000)
H = np.abs(1 + 0.85 * np.exp(-1j * 2 * np.pi * f * 0.15))  # 主径+时延0.15s的反射径
axes[0].plot(f, H, lw=1.5, color='#4C72B0')
axes[0].set_title('两径信道：|H(f)| 随频率起伏（频率选择性衰落）', fontsize=12)
axes[0].set_xlabel('f (Hz)'); axes[0].set_ylabel('|H(f)|')
fs_t, fd = 1000.0, 10.0
t = np.arange(0, 2, 1 / fs_t)
r = np.zeros(len(t), dtype=complex)
rng2 = np.random.default_rng(3)
for k in range(30):
    th = rng2.uniform(0, 2 * np.pi)
    ph = rng2.uniform(0, 2 * np.pi)
    r += np.exp(1j * (2 * np.pi * fd * np.cos(th) * t + ph))
env = np.abs(r) / 30
axes[1].plot(t, env, lw=0.8, color='#C44E52')
axes[1].set_title('瑞利衰落包络（多普勒 fd=10Hz）：信号忽强忽弱', fontsize=12)
axes[1].set_xlabel('t (s)'); axes[1].set_ylabel('归一化幅度')
plt.tight_layout()
save(fig, '17_多径与瑞利衰落.png')

# ============ 18 OFDM正交子载波 ============
fig, ax = plt.subplots(figsize=(9, 4))
T = 1.0
t = np.linspace(0, T, 500)
total = np.zeros_like(t)
for k, color in [(1, '#4C72B0'), (2, '#DD8452'), (3, '#55A868'), (4, '#C44E52')]:
    w = np.cos(2 * np.pi * k * t)
    ax.plot(t, w, lw=1, alpha=0.55, color=color, label='子载波 %d' % k)
    total += w
ax.plot(t, total, 'k', lw=2.2, label='叠加波形')
ax.legend(fontsize=9, ncol=5, loc='upper center')
ax.set_title('OFDM：在一个符号周期 T 内各子载波恰好整数个周期 → 相互正交', fontsize=12)
ax.set_xlabel('t (s)')
save(fig, '18_OFDM正交子载波.png')

# ============ 19 光纤结构与全反射 ============
fig, axes = plt.subplots(1, 2, figsize=(11, 4))
ax1 = axes[0]
ax1.add_patch(Circle((0, 0), 3.0, facecolor='#F5D061', edgecolor='k', lw=2))       # 涂覆层
ax1.add_patch(Circle((0, 0), 2.1, facecolor='#B8D4E3', edgecolor='k', lw=2))       # 包层
ax1.add_patch(Circle((0, 0), 1.0, facecolor='#4C72B0', edgecolor='k', lw=2))       # 纤芯
ax1.text(0, 0, '纤芯\nn1≈1.468', ha='center', va='center', color='w', fontsize=10)
ax1.text(0, 1.55, '包层 n2≈1.462', ha='center', fontsize=10)
ax1.text(0, 2.55, '涂覆层(保护)', ha='center', fontsize=10)
ax1.set_xlim(-3.4, 3.4); ax1.set_ylim(-3.4, 3.4); ax1.set_aspect('equal'); ax1.axis('off')
ax1.set_title('光纤横截面', fontsize=12)
ax2 = axes[1]
ax2.plot([-5, 5], [2, 2], 'k', lw=2); ax2.plot([-5, 5], [-2, -2], 'k', lw=2)
ax2.plot([-5, 5], [2.15, 2.15], 'gray', lw=6, alpha=0.4)
ax2.plot([-5, 5], [-2.15, -2.15], 'gray', lw=6, alpha=0.4)
path_x, path_y = [-4, -1.8, 1.8, 4], [0, 1.7, -1.7, 0]
ax2.plot(path_x, path_y, '-', color='#C44E52', lw=2)
for xx, yy, a in [(-1.8, 1.7, 1), (1.8, -1.7, 1)]:
    ax2.plot(xx, yy, 'o', color='#C44E52', ms=5)
ax2.annotate('全反射\n(θ > 临界角)', xy=(1.8, -1.7), xytext=(2.2, 0.2), fontsize=11,
             arrowprops=dict(arrowstyle='->'))
ax2.text(-4.6, 0.6, '入射光', fontsize=11)
ax2.text(2.5, 1.5, '包层 n2', fontsize=10); ax2.text(2.5, 2.5, '涂覆层', fontsize=10)
ax2.set_title('纵向：光在纤芯中反复全反射前进', fontsize=12)
ax2.set_xlim(-5.5, 5.5); ax2.set_ylim(-3.2, 3.2); ax2.axis('off')
plt.tight_layout()
save(fig, '19_光纤结构与全反射.png')

# ============ 20 蜂窝网络频率复用 ============
fig, ax = plt.subplots(figsize=(7.5, 6.5))
colors7 = ['#4C72B0', '#DD8452', '#55A868', '#C44E52', '#8172B2', '#937860', '#DA8BC3']
k = 0
for row in range(4):
    for col in range(5):
        x = col * np.sqrt(3) + (row % 2) * np.sqrt(3) / 2
        y = row * 1.5
        cidx = (k + row * 3) % 7
        hexa = RegularPolygon((x, y), numVertices=6, radius=0.58,
                              orientation=np.pi / 6, facecolor=colors7[cidx],
                              alpha=0.85, edgecolor='w')
        ax.add_patch(hexa)
        ax.text(x, y, 'F%d' % (cidx + 1), ha='center', va='center', color='w', fontsize=11)
ax.set_title('蜂窝网络：7小区频率复用（同色=同频组，相隔足够远不干扰）', fontsize=12)
ax.set_xlim(-1.2, 8.2); ax.set_ylim(-1.2, 5.8)
ax.set_aspect('equal'); ax.axis('off')
save(fig, '20_蜂窝网络与频率复用.png')

# ============ 21 RC电路充放电 ============
fig, ax = plt.subplots(figsize=(8, 4.2))
t = np.linspace(0, 5, 500)
charge = 1 - np.exp(-t)
discharge = np.exp(-(t - 3)) * (t >= 3)
ax.plot(t, charge, lw=2.5, color='#4C72B0', label='充电 v_C(t)=V(1-e^{-t/τ})')
ax.plot(t[t >= 3], discharge[t >= 3], lw=2.5, color='#C44E52', label='放电 v_C(t)=V·e^{-(t-3)/τ}')
for k, v in [(1, 0.632), (2, 0.865), (3, 0.950)]:
    ax.plot(k, v, 'o', color='#4C72B0')
    ax.annotate('t=%dτ: %.1f%%' % (k, v * 100), xy=(k, v), xytext=(k + 0.15, v - 0.13), fontsize=10)
ax.axvline(3, ls='--', color='gray', lw=1)
ax.text(3.05, 0.15, 't=3τ 时开关切换到放电', fontsize=10, rotation=90)
ax.set_xlabel('t / τ  (τ=RC 时间常数)'); ax.set_ylabel('v_C / V')
ax.legend(fontsize=10); ax.grid(alpha=0.3)
ax.set_title('RC 电路充放电：3τ 基本达到稳态（约95%）', fontsize=13)
save(fig, '21_RC电路充放电.png')

# ============ 22 二极管特性曲线 ============
fig, ax = plt.subplots(figsize=(8, 4.2))
v = np.linspace(-1, 0.8, 1000)
Is, nVt = 1e-12, 2 * 0.026
i = Is * (np.exp(v / nVt) - 1)
i_plot = np.clip(i, -2e-12 * 1e3, 60e-3)
ax.plot(v, i_plot * 1e3, lw=2.5, color='#4C72B0')
ax.axvline(0.7, ls='--', color='#C44E52')
ax.text(0.71, 30, '导通电压≈0.7V(硅管)\n导通后电流指数上升', fontsize=11, color='#C44E52')
ax.set_xlabel('电压 V (V)'); ax.set_ylabel('电流 I (mA)')
ax.set_title('二极管伏安特性：单向导电性（肖克利方程）', fontsize=13)
ax.grid(alpha=0.3)
save(fig, '22_二极管特性曲线.png')

# ============ 23 三极管输出特性 ============
fig, ax = plt.subplots(figsize=(8, 4.6))
vce = np.linspace(0, 10, 400)
beta_, VA = 100.0, 100.0
for ib_uA, color in zip([10, 20, 30, 40, 50, 60],
                        ['#4C72B0', '#DD8452', '#55A868', '#C44E52', '#8172B2', '#937860']):
    ic = beta_ * ib_uA * 1e-6 * (1 - np.exp(-vce / 0.2)) / (1 - vce / VA)
    ax.plot(vce, ic * 1e3, lw=2, color=color, label='IB=%dμA' % ib_uA)
ax.axvspan(0, 0.3, alpha=0.12, color='gray')
ax.text(0.1, 2.2, '饱和区', fontsize=11, rotation=90)
ax.text(4.5, 5.6, '放大区：I_C = β·I_B', fontsize=12)
ax.set_xlabel('V_CE (V)'); ax.set_ylabel('I_C (mA)')
ax.legend(fontsize=9, ncol=2)
ax.set_title('三极管（BJT）共射输出特性曲线', fontsize=13)
ax.grid(alpha=0.3)
save(fig, '23_三极管输出特性.png')

# ============ 24 卡诺图 ============
fig, ax = plt.subplots(figsize=(6, 6))
cols = ['00', '01', '11', '10']  # CD
rows = ['00', '01', '11', '10']  # AB
vals = [['1', '0', '0', '1'],
        ['0', '1', '1', '0'],
        ['0', '1', '1', '0'],
        ['1', '0', '0', '1']]
# m编号: 行AB, 列CD -> m = A*8+B*4+C*2+D
mnum = [['0', '1', '3', '2'],
        ['4', '5', '7', '6'],
        ['12', '13', '15', '14'],
        ['8', '9', '11', '10']]
ax.set_xlim(0, 5); ax.set_ylim(0, 5); ax.axis('off')
for j, c in enumerate(cols):
    ax.text(j + 1.5, 4.65, c, ha='center', fontsize=13)
for i, r in enumerate(rows):
    ax.text(0.35, 3.5 - i, r, va='center', fontsize=13)
ax.text(0.35, 4.9, 'AB\\CD', fontsize=11)
for i in range(4):
    for j in range(4):
        x, y = 1 + j, 3 - i
        ax.add_patch(Rectangle((x, y), 1, 1, facecolor='w', edgecolor='k', lw=1.5))
        ax.text(x + 0.5, y + 0.62, vals[i][j], ha='center', fontsize=15,
                color='#C44E52' if vals[i][j] == '1' else 'gray')
        ax.text(x + 0.85, y + 0.18, 'm' + mnum[i][j], ha='right', fontsize=8, color='gray')
# 圈组: 四角 m0,m2,m8,m10（B=0,D=0）
for (cx, cy) in [(1.05, 3.05), (4.05, 3.05), (1.05, 0.05), (4.05, 0.05)]:
    ax.add_patch(Rectangle((cx, cy), 0.9, 0.9, fill=False, edgecolor='#4C72B0', lw=3))
# 中央 2x2：m5,m7,m13,m15（B=1,D=1）
ax.add_patch(Rectangle((2.05, 1.05), 1.9, 1.9, fill=False, edgecolor='#55A868', lw=3))
ax.text(0.1, -0.35, '蓝圈：四角 m0,m2,m8,m10 → B非·D非    绿圈：m5,m7,m13,m15 → BD\n'
                   r'$F = \bar{B}\bar{D} + BD$（B 与 D 相同为1：同或）',
        fontsize=12)
ax.set_title('四变量卡诺图化简示例', fontsize=14)
save(fig, '24_卡诺图.png')

# ============ 25 网络协议栈 ============
fig, ax = plt.subplots(figsize=(9, 6))
osi = ['7 应用层', '6 表示层', '5 会话层', '4 传输层', '3 网络层', '2 数据链路层', '1 物理层']
tcpi = ['应用层\n(HTTP/FTP/DNS…)', '传输层\n(TCP/UDP)', '网际层\n(IP)', '网络接口层\n(以太网/WiFi)']
for i, name in enumerate(osi):
    y = 6 - i
    ax.add_patch(Rectangle((0.5, y), 2.6, 0.8, facecolor='#4C72B0', alpha=0.85))
    ax.text(1.8, y + 0.4, name, ha='center', va='center', color='w', fontsize=11)
mapping = [(0, 0), (1, 0), (2, 0), (3, 1), (4, 2), (5, 3), (6, 3)]
for i, ti in mapping:
    y_osi = 6 - i
    y_tcp = 5.4 - ti * 1.6
    ax.plot([2.6], [y_osi + 0.4], 'o', color='gray', ms=3)
for ti, name in enumerate(tcpi):
    y = 5.4 - ti * 1.6
    h = 1.2 if ti == 0 else 1.2
    ax.add_patch(Rectangle((4.3, y - 0.4), 3.4, h, facecolor='#55A868', alpha=0.85))
    ax.text(6.0, y + 0.2, name, ha='center', va='center', color='w', fontsize=11)
ax.text(1.8, 7.1, 'OSI 七层模型', ha='center', fontsize=13)
ax.text(6.0, 7.1, 'TCP/IP 四层模型', ha='center', fontsize=13)
ax.annotate('', xy=(4.3, 5.4), xytext=(3.1, 6.4), arrowprops=dict(arrowstyle='<->', color='gray'))
ax.annotate('', xy=(4.3, 3.8), xytext=(3.1, 4.4), arrowprops=dict(arrowstyle='<->', color='gray'))
ax.annotate('', xy=(4.3, 2.2), xytext=(3.1, 3.4), arrowprops=dict(arrowstyle='<->', color='gray'))
ax.annotate('', xy=(4.3, 0.6), xytext=(3.1, 1.4), arrowprops=dict(arrowstyle='<->', color='gray'))
ax.set_xlim(0, 8.2); ax.set_ylim(0, 7.6); ax.axis('off')
ax.set_title('OSI 与 TCP/IP 协议栈对照', fontsize=14)
save(fig, '25_网络协议栈.png')

# ============ 26 WIFI信道 ============
fig, ax = plt.subplots(figsize=(10, 3.8))
for ch in range(1, 14):
    f0 = 2412 + (ch - 1) * 5 - 2400
    color = '#4C72B0' if ch in (1, 6, 11) else '#C44E52'
    ax.barh(0, 22, left=f0 - 11, height=0.5, alpha=0.45 if ch not in (1, 6, 11) else 0.85,
            color=color, edgecolor='k', lw=0.5)
    ax.text(f0, 0.35, str(ch), ha='center', fontsize=9)
for ch in (1, 6, 11):
    f0 = 2412 + (ch - 1) * 5 - 2400
    ax.text(f0, -0.42, '不重叠\n信道 %d' % ch, ha='center', fontsize=9, color='#4C72B0')
ax.axvline(2412 - 2400, ls=':', color='gray'); ax.axvline(2472 - 2400, ls=':', color='gray')
ax.text(2417 - 2400, 0.72, '2.4GHz ISM 频段', fontsize=10)
ax.set_xlabel('频率（相对 2400 MHz 的偏移，MHz）'); ax.set_yticks([])
ax.set_xlim(8, 105)
ax.set_title('2.4GHz WiFi：13个信道每格5MHz但带宽22MHz → 只有 1/6/11 互不重叠', fontsize=12)
save(fig, '26_WIFI信道.png')

print('全部图片生成完成！')
