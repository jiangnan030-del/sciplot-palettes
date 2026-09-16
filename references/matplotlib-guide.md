# Matplotlib / Seaborn 科研绘图配色指南

本文档提供将 sciplot-palettes 配色方案应用到 matplotlib/seaborn 绘图的完整代码模板。

## 目录

- [全局设置](#全局设置)
- [分类色板（Categorical）](#分类色板categorical)
- [连续色板（Sequential）](#连续色板sequential)
- [发散色板（Diverging）](#发散色板diverging)
- [按图表类型的应用示例](#按图表类型的应用示例)
- [出版级导出设置](#出版级导出设置)

---

## 全局设置

### 推荐 rcParams 配置

```python
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

# 全局出版级样式
plt.rcParams.update({
    'font.family': 'Arial',          # 或 'Times New Roman'
    'font.size': 10,
    'axes.linewidth': 0.8,
    'axes.labelsize': 11,
    'axes.titlesize': 12,
    'xtick.labelsize': 9,
    'ytick.labelsize': 9,
    'legend.fontsize': 9,
    'figure.dpi': 150,
    'savefig.dpi': 600,              # 出版级分辨率
    'savefig.bbox': 'tight',
    'axes.spines.top': False,
    'axes.spines.right': False,
})
```

---

## 分类色板（Categorical）

### 定义自定义色板

```python
# === Nature 经典色板 ===
nature_colors = [
    '#E64B35', '#4DBBD5', '#00A087', '#3C5488',
    '#F39B7F', '#8491B4', '#91D1C2', '#DC0000'
]

# === Okabe-Ito 色盲安全色板 ===
okabe_ito_colors = [
    '#E69F00', '#56B4E9', '#009E73', '#F0E442',
    '#0072B2', '#D55E00', '#CC79A7', '#999999'
]

# === 东方美学：烟雨釉色 ===
misty_glaze = ['#f0f7f7', '#b2d8dc', '#b0d9dd', '#b0dbdd']

# === 东方美学：晴初雪霁 ===
snow_after_sun = ['#eaedf1', '#ede3cd', '#c0cee2', '#b9c7d5']

# === 东方美学：三分缠绵 ===
deep_love = ['#232323', '#691d09', '#831100', '#381a1a']

# === 东方美学：月亮速递 ===
moon_express = ['#fffae5', '#ffffff', '#d4e3fe', '#caf0fe']
```

### 应用为 seaborn 调色板

```python
import seaborn as sns

# 方法1：直接设置 palette
sns.set_palette(nature_colors)

# 方法2：在绘图时指定
sns.boxplot(data=df, x='group', y='value', palette=nature_colors)

# 方法3：创建 ListedColormap（用于颜色条）
from matplotlib.colors import ListedColormap
cmap = ListedColormap(nature_colors, name='nature')
```

---

## 连续色板（Sequential）

### 从 HEX 列表创建连续色板

```python
from matplotlib.colors import LinearSegmentedColormap

# 蓝青渐变
blue_teal = ['#f7fbff', '#deebf7', '#c6dbef', '#9ecae1', '#6baed6',
             '#4292c6', '#2171b5', '#08519c', '#08306b']
cmap_blue_teal = LinearSegmentedColormap.from_list('blue_teal', blue_teal)

# 温热渐变
warm_seq = ['#fff5f0', '#fee0d2', '#fcbba1', '#fc9272', '#fb6a4a',
            '#ef3b2c', '#cb181d', '#99000d', '#67000d']
cmap_warm = LinearSegmentedColormap.from_list('warm', warm_seq)

# 翠绿渐变
forest_seq = ['#f7fcf5', '#e5f5e0', '#c7e9c0', '#a1d99b', '#74c476',
              '#41ab5d', '#238b45', '#006d2c', '#00441b']
cmap_forest = LinearSegmentedColormap.from_list('forest', forest_seq)
```

### 热图使用示例

```python
import numpy as np

data = np.random.randn(10, 10)

fig, ax = plt.subplots(figsize=(5, 4))
im = ax.imshow(data, cmap=cmap_blue_teal, aspect='auto')
cbar = fig.colorbar(im, ax=ax, shrink=0.8)
cbar.set_label('Intensity (a.u.)', fontsize=10)
plt.tight_layout()
```

---

## 发散色板（Diverging）

### 创建发散色板

```python
# 红蓝发散（中点为中性灰）
rdbu_colors = ['#b2182b', '#d6604d', '#f4a582', '#fddbc7', '#f7f7f7',
               '#d1e5f0', '#92c5de', '#4393c3', '#2166ac']
cmap_rdbu = LinearSegmentedColormap.from_list('rdbu_diverge', rdbu_colors)

# 使用 TwoSlopeNorm 确保中点正确
from matplotlib.colors import TwoSlopeNorm

vmax = np.abs(data).max()
norm = TwoSlopeNorm(vmin=-vmax, vcenter=0, vmax=vmax)

fig, ax = plt.subplots(figsize=(5, 4))
im = ax.imshow(data, cmap=cmap_rdbu, norm=norm, aspect='auto')
fig.colorbar(im, ax=ax, shrink=0.8)
```

---

## 按图表类型的应用示例

### 分组柱状图

```python
groups = ['A', 'B', 'C', 'D']
values = [23, 45, 32, 56]
errors = [3, 4, 2.5, 5]

fig, ax = plt.subplots(figsize=(4, 3))
x = np.arange(len(groups))
bars = ax.bar(x, values, yerr=errors, capsize=3,
              color=nature_colors[:4], edgecolor='white', linewidth=0.8)

ax.set_xticks(x)
ax.set_xticklabels(groups)
ax.set_ylabel('Value')
plt.tight_layout()
```

### 多系列折线图

```python
x = np.linspace(0, 10, 100)
series = [np.sin(x + i*0.5) for i in range(4)]

fig, ax = plt.subplots(figsize=(5, 3.5))
for i, y in enumerate(series):
    ax.plot(x, y, color=okabe_ito_colors[i], linewidth=1.8,
            label=f'Series {i+1}')

ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.legend(frameon=False)
plt.tight_layout()
```

### 散点图（带分类）

```python
np.random.seed(42)
for i in range(4):
    x = np.random.normal(i*2, 0.8, 30)
    y = np.random.normal(i*1.5, 0.8, 30)
    ax.scatter(x, y, color=nature_colors[i], s=30, alpha=0.8,
               edgecolors='white', linewidth=0.5, label=f'Group {i+1}')

ax.legend(frameon=False)
```

### 箱线图

```python
sns.boxplot(data=df, x='category', y='value',
            palette=okabe_ito_colors, width=0.6,
            fliersize=3, linewidth=0.8)
```

### 小提琴图

```python
sns.violinplot(data=df, x='category', y='value',
               palette=nature_colors[:5], inner='quartile',
               linewidth=0.8)
```

### 堆叠面积图

```python
ax.stackplot(x, *series, colors=moon_express[2:], alpha=0.8,
             labels=[f'S{i+1}' for i in range(len(series))])
```

---

## 出版级导出设置

```python
# 推荐导出格式
# 1. PDF（矢量，期刊首选）
plt.savefig('figure.pdf', format='pdf')

# 2. PNG（高分辨率预览）
plt.savefig('figure.png', dpi=600, format='png')

# 3. SVG（矢量，可编辑）
plt.savefig('figure.svg', format='svg')
```

### 黑白打印兼容检查

```python
# 快速验证：转换为灰度后是否可区分
from matplotlib.colors import rgb_to_hsv

for i, hex_color in enumerate(nature_colors[:6]):
    h = hex_color.lstrip('#')
    r, g, b = tuple(int(h[j:j+2], 16)/255 for j in (0, 2, 4))
    hsv = rgb_to_hsv([r, g, b])
    print(f'Color {i+1}: H={hsv[0]:.2f}, S={hsv[1]:.2f}, V={hsv[2]:.2f}')
```

> 灰度值差异 > 0.1 的配色方案在黑白打印时仍可区分。

---

## 常见问题

**Q: 色板颜色不够用怎么办？**
A: 分类色板最多使用 8 色。超过 8 个类别时，建议：
- 合并次要类别为 "Other"
- 使用渐变+标记形状区分
- 使用 facet/子图拆分展示

**Q: 如何确保色盲友好？**
A: 优先使用 Okabe-Ito 或 Wong 色盲优化色板。也可以在 https://www.color-blindness.com/coblis-color-blindness-simulator/ 在线模拟验证。

**Q: 期刊要求特定颜色怎么办？**
A: 查阅期刊作者指南（Author Guidelines），部分期刊指定使用其品牌色。sciplot-palettes 的色值可直接替换为期刊要求色。
