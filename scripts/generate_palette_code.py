#!/usr/bin/env python3
"""
sciplot-palettes: 科研绘图配色代码生成器

用法:
  python generate_palette_code.py list                    # 列出所有色板
  python generate_palette_code.py show <name>             # 显示色板详情
  python generate_palette_code.py code <name> --format matplotlib   # 生成matplotlib代码
  python generate_palette_code.py code <name> --format seaborn      # 生成seaborn代码
  python generate_palette_code.py code <name> --format origin       # 生成Origin代码
  python generate_palette_code.py code <name> --format css           # 生成CSS变量
  python generate_palette_code.py preview <name>          # 终端预览色板
"""

import sys
import argparse
from typing import List, Dict

# ============================================================
# 配色数据库
# ============================================================

PALETTES: Dict[str, Dict] = {
    # --- 东方美学系列 ---
    "misty-glaze": {
        "name_cn": "烟雨釉色",
        "category": "categorical",
        "series": "东方美学",
        "description": "青瓷釉色，清淡雅致，低饱和青绿色调",
        "colors": ["#f0f7f7", "#b2d8dc", "#b0d9dd", "#b0dbdd"],
    },
    "snow-after-sun": {
        "name_cn": "晴初雪霁",
        "category": "categorical",
        "series": "东方美学",
        "description": "雪后初晴，冷暖交融，清冷中带一丝暖意",
        "colors": ["#eaedf1", "#ede3cd", "#c0cee2", "#b9c7d5"],
    },
    "deep-love": {
        "name_cn": "三分缠绵",
        "category": "categorical",
        "series": "东方美学",
        "description": "浓郁深沉，红黑对比，视觉冲击力强",
        "colors": ["#232323", "#691d09", "#831100", "#381a1a"],
    },
    "moon-express": {
        "name_cn": "月亮速递",
        "category": "categorical",
        "series": "东方美学",
        "description": "明亮通透，奶白与浅蓝交织，清新治愈",
        "colors": ["#fffae5", "#ffffff", "#d4e3fe", "#caf0fe"],
    },
    # --- 经典学术期刊系列 ---
    "nature-classic": {
        "name_cn": "Nature 经典",
        "category": "categorical",
        "series": "学术期刊",
        "description": "Nature 期刊常用配色，饱和度适中，类别区分度高",
        "colors": [
            "#E64B35", "#4DBBD5", "#00A087", "#3C5488",
            "#F39B7F", "#8491B4", "#91D1C2", "#DC0000",
        ],
    },
    "science-minimal": {
        "name_cn": "Science 简约",
        "category": "categorical",
        "series": "学术期刊",
        "description": "Okabe-Ito 调色板，色盲友好，黑白打印可区分",
        "colors": [
            "#0072B2", "#E69F00", "#009E73", "#CC79A7",
            "#56B4E9", "#F0E442", "#D55E00", "#999999",
        ],
    },
    "publication-ready": {
        "name_cn": "期刊投稿标准",
        "category": "categorical",
        "series": "学术期刊",
        "description": "Matplotlib Tableau 默认配色，被广泛接受",
        "colors": [
            "#1f77b4", "#ff7f0e", "#2ca02c", "#d62728",
            "#9467bd", "#8c564b", "#e377c2", "#7f7f7f",
        ],
    },
    # --- 色盲友好系列 ---
    "okabe-ito": {
        "name_cn": "Okabe-Ito 色盲安全",
        "category": "categorical",
        "series": "色盲友好",
        "description": "Okabe & Ito (2008) 色盲安全调色板，8色全部通过模拟测试",
        "colors": [
            "#E69F00", "#56B4E9", "#009E73", "#F0E442",
            "#0072B2", "#D55E00", "#CC79A7", "#999999",
        ],
    },
    "wong-colorblind": {
        "name_cn": "Wong 色盲优化",
        "category": "categorical",
        "series": "色盲友好",
        "description": "加入黑色作为第一色，增强轮廓线区分度",
        "colors": [
            "#000000", "#E69F00", "#56B4E9", "#009E73",
            "#F0E442", "#0072B2", "#D55E00", "#CC79A7",
        ],
    },
    # --- 连续色板 ---
    "sequential-blue-teal": {
        "name_cn": "蓝青渐变",
        "category": "sequential",
        "series": "连续色板",
        "description": "从浅蓝到深蓝，经典科学可视化配色",
        "colors": [
            "#f7fbff", "#deebf7", "#c6dbef", "#9ecae1", "#6baed6",
            "#4292c6", "#2171b5", "#08519c", "#08306b",
        ],
    },
    "sequential-warm": {
        "name_cn": "温热渐变",
        "category": "sequential",
        "series": "连续色板",
        "description": "从米白到深红，暖色调能量感",
        "colors": [
            "#fff5f0", "#fee0d2", "#fcbba1", "#fc9272", "#fb6a4a",
            "#ef3b2c", "#cb181d", "#99000d", "#67000d",
        ],
    },
    "sequential-forest": {
        "name_cn": "翠绿渐变",
        "category": "sequential",
        "series": "连续色板",
        "description": "从浅绿到深绿，自然系",
        "colors": [
            "#f7fcf5", "#e5f5e0", "#c7e9c0", "#a1d99b", "#74c476",
            "#41ab5d", "#238b45", "#006d2c", "#00441b",
        ],
    },
    "sequential-purple": {
        "name_cn": "紫雾渐变",
        "category": "sequential",
        "series": "连续色板",
        "description": "从淡紫到深紫，优雅专业",
        "colors": [
            "#fcfbfd", "#efedf5", "#dadaeb", "#bcbddc", "#9e9ac8",
            "#807dba", "#6a51a3", "#54278f", "#3f007d",
        ],
    },
    # --- 发散色板 ---
    "diverging-red-blue": {
        "name_cn": "红蓝发散",
        "category": "diverging",
        "series": "发散色板",
        "description": "经典 RdBu 反转，红色表示正向/高值，蓝色表示负向/低值",
        "colors": [
            "#b2182b", "#d6604d", "#f4a582", "#fddbc7", "#f7f7f7",
            "#d1e5f0", "#92c5de", "#4393c3", "#2166ac",
        ],
    },
    "diverging-brown-green": {
        "name_cn": "棕绿发散",
        "category": "diverging",
        "series": "发散色板",
        "description": "Brown-Green 配色，学术感强",
        "colors": [
            "#8c510a", "#bf812d", "#dfc27d", "#f6e8c3", "#f5f5f5",
            "#c7eae5", "#80cdc1", "#35978f", "#01665e",
        ],
    },
    "diverging-purple-orange": {
        "name_cn": "紫橙发散",
        "category": "diverging",
        "series": "发散色板",
        "description": "Purple-Orange 对比鲜明，适合聚类分析",
        "colors": [
            "#542788", "#998ec3", "#d8daeb", "#f2f0f7", "#f7f7f7",
            "#fee0b6", "#fdb863", "#e08214", "#b35806",
        ],
    },
}


# ============================================================
# 代码生成器
# ============================================================

def hex_to_rgb(hex_color: str) -> tuple:
    h = hex_color.lstrip("#")
    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))


def generate_matplotlib_code(colors: List[str], name: str, meta: Dict) -> str:
    """生成 matplotlib 可用代码"""
    color_vars = ",\n    ".join(f'"{c}"' for c in colors)
    lines = [
        f"# {meta['name_cn']} ({name}) - matplotlib",
        f"# {meta['description']}",
        f"{name.replace('-', '_')}_colors = [",
        f"    {color_vars}",
        "]",
        "",
        "# 分类色板使用：",
        "# ax.bar(x, y, color=colors[:len(groups)])",
        "",
    ]
    if meta["category"] in ("sequential", "diverging"):
        lines.extend([
            "# 创建连续色板：",
            "from matplotlib.colors import LinearSegmentedColormap",
            f"cmap = LinearSegmentedColormap.from_list('{name}', {name.replace('-', '_')}_colors)",
            "",
        ])
    if meta["category"] == "diverging":
        lines.extend([
            "# 发散色板配合 TwoSlopeNorm 使用：",
            "from matplotlib.colors import TwoSlopeNorm",
            "norm = TwoSlopeNorm(vmin=-vmax, vcenter=0, vmax=vmax)",
            "# im = ax.imshow(data, cmap=cmap, norm=norm)",
            "",
        ])
    return "\n".join(lines)


def generate_seaborn_code(colors: List[str], name: str, meta: Dict) -> str:
    """生成 seaborn 可用代码"""
    color_vars = ", ".join(f'"{c}"' for c in colors)
    lines = [
        f"# {meta['name_cn']} ({name}) - seaborn",
        f"import seaborn as sns",
        "",
        f"{name.replace('-', '_')} = [{color_vars}]",
        "",
        "# 全局设置：",
        f"sns.set_palette({name.replace('-', '_')})",
        "",
        "# 局部使用：",
        "# sns.boxplot(data=df, x='group', y='value', palette=...)",
        "",
    ]
    return "\n".join(lines)


def generate_origin_code(colors: List[str], name: str, meta: Dict) -> str:
    """生成 Origin 可用 RGB 数值"""
    rgb_list = [hex_to_rgb(c) for c in colors]
    lines = [
        f"# {meta['name_cn']} ({name}) - Origin RGB",
        f"# 在 Origin 中通过 Plot Details → Line/Border Color → Custom 输入",
        "",
    ]
    for i, (h, rgb) in enumerate(zip(colors, rgb_list), 1):
        lines.append(f"  Color {i}: RGB({rgb[0]}, {rgb[1]}, {rgb[2]})  [{h}]")
    lines.append("")
    return "\n".join(lines)


def generate_css_code(colors: List[str], name: str, meta: Dict) -> str:
    """生成 CSS 变量代码"""
    lines = [
        f"/* {meta['name_cn']} ({name}) - CSS Variables */",
        ":root {",
    ]
    for i, c in enumerate(colors, 1):
        lines.append(f"  --{name}-{i}: {c};")
    lines.append("}")
    lines.append("")
    lines.append("/* 使用示例: */")
    lines.append("/* .chart-bar { background: var(--" + f"{name}-1); }} */")
    return "\n".join(lines)


FORMAT_GENERATORS = {
    "matplotlib": generate_matplotlib_code,
    "seaborn": generate_seaborn_code,
    "origin": generate_origin_code,
    "css": generate_css_code,
}


# ============================================================
# 终端预览
# ============================================================

def preview_palette(colors: List[str], name_cn: str, name_key: str):
    """在终端中以色块形式预览色板"""
    print(f"\n  {name_cn} ({name_key})")
    print("  " + "-" * 50)
    # 用 ANSI 转义序列显示色块
    for c in colors:
        r, g, b = hex_to_rgb(c)
        block = f"\033[48;2;{r};{g};{b}m    \033[0m"
        print(f"  {block}  {c}")
    print()


# ============================================================
# CLI 主逻辑
# ============================================================

def list_palettes():
    """列出所有可用色板"""
    current_series = ""
    print("\n  可用科研配色方案:\n")
    for key, p in PALETTES.items():
        if p["series"] != current_series:
            current_series = p["series"]
            print(f"  ── {current_series} ──")
        preview = ""
        # 显示色块预览（简化版）
        color_blocks = " ".join(
            f"\033[48;2;{hex_to_rgb(c)[0]};{hex_to_rgb(c)[1]};{hex_to_rgb(c)[2]}m  \033[0m"
            for c in p["colors"]
        )
        print(f"  {color_blocks}  {p['name_cn']:<16} ({key})")
        print(f"           {p['description']}")
    print()


def show_palette(name: str):
    """显示单个色板详情"""
    if name not in PALETTES:
        print(f"  ✗ 未找到色板: {name}")
        print(f"  可用色板: {', '.join(PALETTES.keys())}")
        sys.exit(1)
    p = PALETTES[name]
    preview_palette(p["colors"], p["name_cn"], name)
    print(f"  类别: {p['category']}")
    print(f"  系列: {p['series']}")
    print(f"  说明: {p['description']}")
    print()
    for i, c in enumerate(p["colors"], 1):
        rgb = hex_to_rgb(c)
        print(f"    {i}. {c}  RGB({rgb[0]}, {rgb[1]}, {rgb[2]})")
    print()


def generate_code(name: str, fmt: str):
    """生成指定格式的代码"""
    if name not in PALETTES:
        print(f"  ✗ 未找到色板: {name}")
        print(f"  可用色板: {', '.join(PALETTES.keys())}")
        sys.exit(1)
    if fmt not in FORMAT_GENERATORS:
        print(f"  ✗ 不支持的格式: {fmt}")
        print(f"  支持格式: {', '.join(FORMAT_GENERATORS.keys())}")
        sys.exit(1)
    p = PALETTES[name]
    print(FORMAT_GENERATORS[fmt](p["colors"], name, p))


def main():
    parser = argparse.ArgumentParser(
        description="sciplot-palettes: 科研绘图配色代码生成器"
    )
    subparsers = parser.add_subparsers(dest="command", help="可用命令")

    subparsers.add_parser("list", help="列出所有色板")

    show_parser = subparsers.add_parser("show", help="显示色板详情")
    show_parser.add_argument("name", help="色板名称")

    code_parser = subparsers.add_parser("code", help="生成配色代码")
    code_parser.add_argument("name", help="色板名称")
    code_parser.add_argument(
        "--format", "-f",
        choices=list(FORMAT_GENERATORS.keys()),
        default="matplotlib",
        help="输出格式 (默认: matplotlib)"
    )

    preview_parser = subparsers.add_parser("preview", help="终端预览色板")
    preview_parser.add_argument("name", help="色板名称")

    args = parser.parse_args()

    if args.command == "list":
        list_palettes()
    elif args.command == "show":
        show_palette(args.name)
    elif args.command == "code":
        generate_code(args.name, args.format)
    elif args.command == "preview":
        show_palette(args.name)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
