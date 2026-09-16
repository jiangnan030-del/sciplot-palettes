# sciplot-palettes

> 科研绘图配色方案库 —— 16 套经过精心调校的学术图表配色，覆盖东方美学、顶级期刊、色盲友好、连续/发散色板。

![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Palettes](https://img.shields.io/badge/Palettes-16-purple.svg)

---

## 目录

- [项目简介](#项目简介)
- [配色方案一览](#配色方案一览)
- [快速开始](#快速开始)
- [使用方法](#使用方法)
- [目录结构](#目录结构)
- [配色选择指南](#配色选择指南)
- [License](#license)

---

## 项目简介

`sciplot-palettes` 是一个面向科研工作者的配色方案库，旨在解决学术论文绘图中"不知道用什么颜色"的痛点。所有配色均经过以下标准筛选：

- **学术审美**：符合 Nature / Science 等顶级期刊的配色习惯
- **色盲友好**：核心色板通过色觉障碍模拟测试
- **打印兼容**：黑白灰度打印仍可区分
- **代码即用**：直接输出 matplotlib / seaborn / Origin / CSS 可用代码

灵感来源：小红书 @跟珍妮学配色 的东方美学色卡，扩展为完整科研绘图体系。

---

## 配色方案一览

### 东方美学系列

| 色板 | 预览 | 色值 | 风格 |
|------|------|------|------|
| **烟雨釉色** | 🟦🟦🟦🟦 | `#f0f7f7` `#b2d8dc` `#b0d9dd` `#b0dbdd` | 青瓷釉色，清淡雅致 |
| **晴初雪霁** | ⬜🟨🟦🩶 | `#eaedf1` `#ede3cd` `#c0cee2` `#b9c7d5` | 雪后初晴，冷暖交融 |
| **三分缠绵** | ⬛🟫🟥🟤 | `#232323` `#691d09` `#831100` `#381a1a` | 浓郁深沉，视觉冲击 |
| **月亮速递** | 🤍⬜💙🩵 | `#fffae5` `#ffffff` `#d4e3fe` `#caf0fe` | 明亮通透，清新治愈 |

### 学术期刊系列

| 色板 | 色数 | 适用场景 |
|------|------|----------|
| **Nature 经典** | 8 | 多类别分组柱状图、箱线图 |
| **Science 简约** | 8 | 多系列折线图、散点图矩阵 |
| **投稿标准** | 8 | 通用 SCI 投稿，兼容性最佳 |

### 色盲友好系列

| 色板 | 依据 | 特点 |
|------|------|------|
| **Okabe-Ito** | Okabe & Ito (2008) | 8 色全部通过色觉模拟测试 |
| **Wong 优化** | Wong (2011) | 首色为黑色，增强轮廓区分 |

### 连续色板（Sequential）

| 色板 | 色调 | 适用 |
|------|------|------|
| 蓝青渐变 | 浅→深蓝 | 温度分布、浓度场、强度图 |
| 温热渐变 | 米白→深红 | 热成像、应力分布 |
| 翠绿渐变 | 浅→深绿 | 生物量、生态指标 |
| 紫雾渐变 | 淡→深紫 | 光谱数据、浓度梯度 |

### 发散色板（Diverging）

| 色板 | 中点 | 适用 |
|------|------|------|
| 红蓝发散 | 中性灰 | 差异分析、误差分布 |
| 棕绿发散 | 浅灰 | 干湿对比、正负效应 |
| 紫橙发散 | 浅灰 | 聚类分析、热图 |

---

## 快速开始

### 1. 浏览所有色板

```bash
python scripts/generate_palette_code.py list
```

### 2. 查看色板详情

```bash
python scripts/generate_palette_code.py show nature-classic
python scripts/generate_palette_code.py show misty-glaze
```

### 3. 生成代码

```bash
# matplotlib 代码
python scripts/generate_palette_code.py code okabe-ito --format matplotlib

# seaborn 代码
python scripts/generate_palette_code.py code nature-classic --format seaborn

# Origin RGB 数值
python scripts/generate_palette_code.py code deep-love --format origin

# CSS 变量
python scripts/generate_palette_code.py code moon-express --format css
```

---

## 使用方法

### Matplotlib 示例

```python
import matplotlib.pyplot as plt
import numpy as np

# 定义色板（由 CLI 工具生成）
nature_colors = [
    "#E64B35", "#4DBBD5", "#00A087", "#3C5488",
    "#F39B7F", "#8491B4", "#91D1C2", "#DC0000"
]

# 分组柱状图
groups = ['A', 'B', 'C', 'D']
values = [23, 45, 32, 56]

fig, ax = plt.subplots(figsize=(4, 3))
ax.bar(groups, values, color=nature_colors[:4], edgecolor='white')
plt.savefig('bar_plot.pdf', dpi=600, bbox_inches='tight')
```

### Seaborn 示例

```python
import seaborn as sns
import matplotlib.pyplot as plt

okabe_ito = ["#E69F00", "#56B4E9", "#009E73", "#F0E442",
             "#0072B2", "#D55E00", "#CC79A7", "#999999"]

sns.set_palette(okabe_ito)
sns.boxplot(data=df, x='group', y='value')
```

### 连续/发散色板

```python
from matplotlib.colors import LinearSegmentedColormap, TwoSlopeNorm

# 发散色板
rdbu = ['#b2182b', '#d6604d', '#f4a582', '#fddbc7', '#f7f7f7',
        '#d1e5f0', '#92c5de', '#4393c3', '#2166ac']
cmap = LinearSegmentedColormap.from_list('rdbu', rdbu)

# 配合 TwoSlopeNorm 使用（确保 0 点居中）
norm = TwoSlopeNorm(vmin=-vmax, vcenter=0, vmax=vmax)
im = ax.imshow(data, cmap=cmap, norm=norm)
```

---

## 目录结构

```
sciplot-palettes/
├── SKILL.md                          # Skill 主入口（AI Agent 加载用）
├── README.md                         # 本文件
├── references/
│   ├── palettes.md                   # 完整配色方案库（含色值、说明、速查表）
│   └── matplotlib-guide.md           # Matplotlib/Seaborn 代码模板与出版级设置
└── scripts/
    └── generate_palette_code.py      # CLI 工具：浏览、预览、生成配色代码
```

---

## 配色选择指南

| 图表类型 | 推荐色板 | 色数 | 理由 |
|----------|----------|------|------|
| 分组柱状图（≤8组） | Nature 经典 / Okabe-Ito | 6-8 | 类别区分度高 |
| 折线图多系列（≤6条） | Science 简约 / 投稿标准 | 4-6 | 线条清晰可辨 |
| 散点图聚类 | Nature 经典 | 3-5 | 突出簇间差异 |
| 热图（连续数据） | 蓝青渐变 / 翠绿渐变 | 9+ | 平滑色阶过渡 |
| 热图（差异数据） | 红蓝发散 / 紫橙发散 | 9 | 明确正负方向 |
| 流程示意图 | 东方美学系列 | 3-4 | 风格统一雅致 |
| 强调重点数据 | 三分缠绵 | 1-2 | 深红突出醒目 |
| 出版投稿通用 | Okabe-Ito 色盲安全 | 6-8 | 审稿友好，打印友好 |

---

## 作为 Skill 使用

本仓库同时是一个 AI Agent Skill，可直接安装到支持 Skill 机制的 AI 助手中：

1. 将整个 `sciplot-palettes/` 目录放入 `.user_skills/` 目录
2. 触发示例：
   - "帮我选个科研绘图配色"
   - "Nature 论文的柱状图用什么配色"
   - "生成 matplotlib 色盲友好配色代码"

---

## 致谢

- 东方美学色卡灵感：小红书 @跟珍妮学配色
- Okabe-Ito 色盲安全调色板：Okabe & Ito (2008)
- 配色设计参考：ColorBrewer、Matplotlib Tableau、seaborn

## License

MIT License
