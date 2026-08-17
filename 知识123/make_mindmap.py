# -*- coding: utf-8 -*-
"""生成静态版《通信工程知识导图》PNG（离线可看，适合打印）"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
import numpy as np
import math

plt.rcParams['font.sans-serif'] = ['Microsoft YaHei', 'SimHei', 'sans-serif']
plt.rcParams['axes.unicode_minus'] = False

DATA = [
    ("01 数学基础", ["复数与欧拉公式", "正弦信号三要素", "分贝dB换算", "傅里叶分析思想", "概率与高斯分布", "Q函数与erfc"]),
    ("02 电路分析", ["基尔霍夫定律", "分压分流", "戴维南定理", "RC动态电路", "相量法与阻抗", "谐振与Q值", "功率因数"]),
    ("03 模拟电子", ["二极管特性", "三极管工作区", "共射放大与Q点", "场效应管", "负反馈组态", "运放虚短虚断"]),
    ("04 数字电子", ["数制与格雷码", "逻辑代数", "卡诺图化简", "译码器/MUX", "触发器", "计数器/状态机", "ADC与DAC"]),
    ("05 信号与系统", ["卷积", "傅里叶级数", "傅里叶变换", "频谱与带宽", "采样定理", "拉氏变换判稳", "z变换"]),
    ("06 数字信号处理", ["DFT与分辨率", "FFT", "窗函数与泄漏", "FIR设计", "IIR设计", "匹配滤波器"]),
    ("07 通信原理★", ["香农公式", "AM/FM调制", "PCM编码", "基带码型", "升余弦与眼图", "ASK/FSK/PSK", "QPSK/16QAM", "误码率BER", "汉明码", "复用多址"]),
    ("08 电磁场", ["麦克斯韦方程", "平面波/极化", "趋肤效应", "全反射", "传输线匹配", "天线链路预算"]),
    ("09 高频电子", ["LC选频网络", "丙类功放", "振荡器", "超外差混频", "检波鉴频", "锁相环PLL"]),
    ("10 信息论", ["熵与自信息", "霍夫曼编码", "信道容量", "香农三定理", "率失真", "LDPC/Polar"]),
    ("11 移动通信", ["蜂窝复用", "衰落与多径", "多普勒", "多址方式", "分集均衡", "MIMO波束", "5G场景"]),
    ("12 光纤通信", ["全反射/NA", "单模多模", "损耗窗口", "色散", "光器件", "WDM", "PON到户"]),
    ("13 计算机网络", ["分层模型", "以太网MAC", "子网划分", "TCP握手", "DNS/HTTP", "WiFi信道"]),
    ("毕业论文★", ["调制仿真选题", "蒙特卡洛BER", "瑞利+分集", "论文结构", "答辩预演"]),
]

PALETTE = ['#4C72B0', '#55A868', '#DD8452', '#C44E52', '#8172B2', '#937860',
           '#DA8BC3', '#8C8C8C', '#4C72B0', '#55A868', '#DD8452', '#8172B2',
           '#C44E52', '#2AA198']

N = len(DATA)
COL_W, ROW_H = 1.0, 0.62
max_leaves = max(len(v) for _, v in DATA)
fig_w = N * COL_W * 2.5
fig_h = max_leaves * ROW_H + 3.4

fig, ax = plt.subplots(figsize=(fig_w, fig_h))
ax.set_xlim(0, N)
ax.set_ylim(0, max_leaves + 3.4)
ax.axis('off')

def draw_box(x, y, w, h, text, fc, fontsize, fontcolor='white', bold=True):
    box = FancyBboxPatch((x - w / 2, y - h / 2), w, h,
                         boxstyle='round,pad=0.02,rounding_size=0.06',
                         facecolor=fc, edgecolor='none', zorder=3)
    ax.add_patch(box)
    ax.text(x, y, text, ha='center', va='center', fontsize=fontsize,
            color=fontcolor, zorder=4, fontweight='bold' if bold else 'normal')

# 根节点
root_x, root_y = N / 2, max_leaves + 2.6
draw_box(root_x, root_y, 1.7, 0.52, '通信工程知识体系', '#333333', 17)

# 各学科列
for i, (subject, leaves) in enumerate(DATA):
    x = i + 0.5
    color = PALETTE[i % len(PALETTE)]
    # 根 → 学科
    sx, sy = root_x, root_y - 0.26
    ex, ey = x, max_leaves + 1.05
    mx = (sx + ex) / 2
    ax.plot([sx, mx, ex], [sy, (sy + ey) / 2, ey], color=color, lw=1.6,
            solid_capstyle='round', zorder=1)
    # 学科标题
    draw_box(x, max_leaves + 0.85, COL_W * 0.92, 0.44, subject, color, 11.5)
    # 叶子
    for j, leaf in enumerate(leaves):
        y = max_leaves - 0.35 - j
        ax.plot([x, x], [max_leaves + 0.63, y + 0.19], color=color, lw=1.1,
                alpha=0.55, zorder=1)
        draw_box(x, y, COL_W * 0.92, 0.34, leaf, '#FFFFFF', 9.5,
                 fontcolor='#333333', bold=False)
        for patch in ax.patches[-1:]:
            patch.set_edgecolor(color)
            patch.set_linewidth(0.8)

ax.set_title('通信工程全课程知识导图（★=核心章节；详解见 通信工程知识库 各学科讲义）',
             fontsize=15, pad=20, color='#444444')

import os
out = r'E:\知识123\知识导图\通信工程知识导图.png'
fig.savefig(out, dpi=110, bbox_inches='tight', facecolor='white')
print('saved', out)
