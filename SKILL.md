---
name: sciplot-palettes
description: "科研绘图配色方案库与代码生成工具。当用户需要为学术论文、科研图表选择配色方案，或需要在 matplotlib/seaborn/Origin 中应用专业科研配色时使用。触发场景包括：(1) 论文投稿图表配色推荐；(2) matplotlib/seaborn 自定义色板设置；(3) 色盲友好配色选择；(4) 热图/柱状图/折线图配色方案查询；(5) 东方美学/学术期刊风格配色需求。"
---

# Sciplot Palettes — 科研绘图配色方案库

## 概述

提供经过精心调校的科研绘图配色方案，涵盖东方美学、学术期刊、色盲友好、连续色板和发散色板五大类。支持直接输出 matplotlib/seaborn/Origin/CSS 可用代码。

## 快速开始

### 1. 浏览可用色板

```bash
python scripts/generate_palette_code.py list
```

### 2. 查看色板详情与预览

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

## 配色方案总览

| 分类 | 色板名称 | 色数 | 适用场景 |
|------|----------|------|----------|
| 东方美学 | misty-glaze（烟雨釉色） | 4 | 环境科学、材料表征 |
| 东方美学 | snow-after-sun（晴初雪霁） | 4 | 大气科学、地球物理 |
| 东方美学 | deep-love（三分缠绵） | 4 | 材料/能源，强调重点 |
| 东方美学 | moon-express（月亮速递） | 4 | 医学可视化、教育图表 |
| 学术期刊 | nature-classic（Nature 经典） | 8 | 多类别分组柱状图 |
| 学术期刊 | science-minimal（Science 简约） | 8 | 多系列折线图、散点图 |
| 学术期刊 | publication-ready（投稿标准） | 8 | 通用出版，兼容性最好 |
| 色盲友好 | okabe-ito（Okabe-Ito） | 8 | 所有需广泛可读的图表 |
| 色盲友好 | wong-colorblind（Wong 优化） | 8 | 带轮廓线的多类图表 |
| 连续色板 | sequential-blue-teal（蓝青渐变） | 9 | 温度分布、强度图 |
| 连续色板 | sequential-warm（温热渐变） | 9 | 热成像、应力分布 |
| 连续色板 | sequential-forest（翠绿渐变） | 9 | 生物量、生态指标 |
| 连续色板 | sequential-purple（紫雾渐变） | 9 | 光谱数据、浓度梯度 |
| 发散色板 | diverging-red-blue（红蓝发散） | 9 | 差异分析、误差分布 |
| 发散色板 | diverging-brown-green（棕绿发散） | 9 | 干湿对比、正负效应 |
| 发散色板 | diverging-purple-orange（紫橙发散） | 9 | 聚类分析、热图 |

## 使用工作流

### 场景 A：论文投稿配图

1. 确认目标期刊类型（Nature 系 / Science 系 / 通用 SCI）
2. 优先选择 `okabe-ito`（色盲安全）或 `nature-classic`
3. 运行 `code <palette> --format matplotlib` 生成代码
4. 参考 [references/matplotlib-guide.md](references/matplotlib-guide.md) 中的出版级导出设置

### 场景 B：需要风格化配色（东方美学）

1. 根据图表主题选择对应意境色板：
   - 材料/陶瓷 → `misty-glaze`
   - 大气/气象 → `snow-after-sun`
   - 强调对比/重点突出 → `deep-love`
   - 医学/健康 → `moon-express`
2. 东方美学色板色数较少（4色），适合 3-4 个类别的图表

### 场景 C：热图/强度图

1. 数值连续数据 → 连续色板（sequential-*）
2. 有正负/双向含义 → 发散色板（diverging-*）
3. 生成代码后参考 matplotlib-guide.md 中的 `TwoSlopeNorm` 用法

### 场景 D：不确定选哪个色板

查阅 [references/palettes.md](references/palettes.md) 末尾的"配色选择速查表"。

## 资源索引

| 文件 | 内容 | 何时读取 |
|------|------|----------|
| [references/palettes.md](references/palettes.md) | 完整配色方案库（含 HEX/RGB、风格说明、选择速查表） | 需要查看色板完整色值或选择配色方案时 |
| [references/matplotlib-guide.md](references/matplotlib-guide.md) | matplotlib/seaborn 代码模板与出版级设置 | 需要写绘图代码、配置全局样式、导出出版级图片时 |
| [scripts/generate_palette_code.py](scripts/generate_palette_code.py) | 配色代码生成 CLI 工具 | 需要快速获取特定色板的代码片段时直接运行 |
