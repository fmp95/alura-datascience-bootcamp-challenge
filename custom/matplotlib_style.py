from cycler import cycler
from random import shuffle, seed

seed(165)

green = "#8feaa1"
red = "#e57373"
blue = "#4DB6AC"
yellow = "#FFF59D"
light_blue = "#90CAF9"
black = "#202024"
white = "#F5F5F5"
transparent = "#fff0"

color = [
    "#ef9a9a",
    "#F48FB1",
    "#CE93D8",
    "#B39DDB",
    "#9FA8DA",
    "#90CAF9",
    "#81D4FA",
    "#80DEEA",
    "#80CBC4",
    "#A5D6A7",
    "#C5E1A5",
    "#E6EE9C",
    "#FFF59D",
    "#FFE082",
    "#FFCC80",
    "#FFAB91",
    "#BCAAA4",
    "#EEEEEE",
    "#B0BEC5",
    "#e57373",
    "#F06292",
    "#BA68C8",
    "#9575CD",
    "#7986CB",
    "#64B5F6",
    "#4FC3F7",
    "#4DD0E1",
    "#4DB6AC",
    "#81C784",
    "#AED581",
    "#DCE775",
    "#FFF176",
    "#FFD54F",
    "#FFB74D",
    "#FF8A65",
    "#A1887F",
    "#E0E0E0",
    "#90A4AE",
]

shuffle(color)

color_cycler = cycler(color=color)

matplotlib_style = {
    "axes.facecolor": transparent,
    "axes.edgecolor": green,
    "axes.linewidth": 3,
    "axes.grid": True,
    "axes.labelcolor": green,
    "axes.labelsize": 22,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "axes.titlecolor": green,
    "axes.titleweight": "bold",
    "axes.titlelocation": "left",
    "axes.titlepad": 30,
    "axes.titlesize": 28,
    "axes.prop_cycle": color_cycler,
    "figure.figsize": [15, 10],
    "font.family": "Roboto",
    "grid.alpha": 0.2,
    "grid.color": white,
    "grid.linestyle": "--",
    "grid.linewidth": 0.5,
    "legend.fontsize": 18,
    "legend.facecolor": white,
    "mathtext.default": "default",
    "xtick.labelcolor": green,
    "xtick.labelsize": 14,
    "xtick.alignment": "center",
    "xaxis.labellocation": "left",
    "ytick.labelcolor": green,
    "ytick.labelsize": 14,
    "ytick.alignment": "center",
    "yaxis.labellocation": "bottom",
    "image.cmap": "Pastel2",
    "lines.linewidth": 3,
}