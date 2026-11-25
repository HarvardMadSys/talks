#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = ["matplotlib", "numpy", "segno"]
# ///
"""Badges, QR code and figures for deck.md, drawn in the MaDSys palette.

    uv run make_figures.py       # writes figures/badge_*.svg, figures/qr_paper.svg, figures/fNN_*.png

The two example figures use made-up data: replace them with your own, keeping the style block.
The logos (figures/logo_*.png) come from the MaDSys PowerPoint template and are not generated here.
"""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import matplotlib.transforms as mtrans  # noqa: E402
import numpy as np  # noqa: E402
import segno  # noqa: E402
from matplotlib.colors import to_rgb  # noqa: E402
from matplotlib.patches import Patch  # noqa: E402

HERE = Path(__file__).resolve().parent
FIG = HERE / "figures"
FIG.mkdir(exist_ok=True)

# The MaDSys PowerPoint theme (template.potx): accent1 crimson, dk2 navy, accent2 burnt orange,
# accent3 green, accent5 brown, accent6 grey, the footer's slate, and the slide background.
MS = {"crimson": "#A51C30", "navy": "#0E2841", "orange": "#B04E12", "green": "#196B24",
      "brown": "#8F3E0E", "grey": "#595959", "slate": "#6B777D", "mauve": "#96607D"}
INK, MUTED, BG = "#000000", "#595959", "#F7F7F7"
# One colour per system, the same on every figure; list the mapping in the README's colour table.
# Your system is crimson; baselines take the darker, quieter colours.
SERIES = {"Ours": MS["crimson"], "Baseline A": MS["navy"], "Baseline B": MS["orange"],
          "Baseline C": MS["slate"]}
# Badges for slide titles and lists: letter -> colour. Use a dark colour so the white letter stays
# readable: crimson, navy, green, orange, brown or grey.
BADGES = {"A": MS["crimson"], "B": MS["navy"], "C": MS["green"]}
# The QR code on the "More in the paper" slide points here.
PAPER_URL = "https://madsys.seas.harvard.edu/"
W = 10  # default figure width (inches); the deck shows figures about 700–850 px wide

plt.rcParams.update({
    # Aptos is the template's font; matplotlib falls back to Arial when Aptos is not installed.
    "font.family": "sans-serif", "font.sans-serif": ["Aptos", "Arial", "Liberation Sans", "DejaVu Sans"],
    "font.size": 17, "axes.titlesize": 17, "axes.labelsize": 17, "legend.fontsize": 15,
    "xtick.labelsize": 15, "ytick.labelsize": 15, "axes.edgecolor": "#444444", "axes.linewidth": 0.9,
    "axes.spines.top": False, "axes.spines.right": False, "axes.grid": True, "grid.color": "#dedede",
    "grid.linewidth": 0.7, "axes.axisbelow": True, "legend.frameon": False,
    # the slide background, so figures sit on the slide without a white box
    "figure.facecolor": BG, "axes.facecolor": BG, "savefig.facecolor": BG,
    "figure.dpi": 100, "savefig.dpi": 200, "savefig.bbox": "tight",
    "axes.prop_cycle": matplotlib.cycler(color=[MS[k] for k in ("crimson", "navy", "orange", "slate",
                                                                  "green", "brown", "mauve", "grey")]),
})


def save(fig, name):
    fig.savefig(FIG / f"{name}.png")
    plt.close(fig)
    print("wrote", name)


def no_grid(ax, axis):
    ax.grid(axis=axis, visible=False)


def bars(ax, cats, series, width=0.8, fmt="{:.0f}", size=13, horizontal=False):
    """Grouped bars: one group per category, series = [(label, values, colour), ...]."""
    k = len(series)
    w = width / k
    x = np.arange(len(cats))
    for i, (lab, vals, col) in enumerate(series):
        pos = x + (i - (k - 1) / 2) * w
        vals = np.asarray(vals, dtype=float)
        b = (ax.barh(pos, vals, height=w, color=col, label=lab) if horizontal
             else ax.bar(pos, vals, width=w, color=col, label=lab))
        if fmt:
            ax.bar_label(b, labels=[fmt.format(v) for v in vals], fontsize=size, padding=2)
    if horizontal:
        ax.set_yticks(x, cats)
        no_grid(ax, "y")
    else:
        ax.set_xticks(x, cats)
        no_grid(ax, "x")
    return x


def title(ax, letter, text):
    ax.set_title(f"({letter}) {text}", loc="left", fontsize=17)


def tint(col, amount):
    """Mix a colour with white: amount 0 keeps it, 1 is white."""
    return tuple(c + (1 - c) * amount for c in to_rgb(col))


def bands(ax, spans, label_y=None):
    """Alternating light bands for phases on the x axis; spans = [(label, x0, x1), ...]."""
    for i, (lab, a, b) in enumerate(spans):
        ax.axvspan(a, b, color="#EDEDED" if i % 2 == 0 else "#E4E4E4", lw=0, zorder=0)
        if label_y is not None:
            ax.text(a + (b - a) / 2, label_y, lab, ha="center", va="bottom", fontsize=14, color=MUTED,
                    transform=mtrans.blended_transform_factory(ax.transData, ax.transAxes))


# --- badges used in slide titles and lists ----------------------------------------------------------
for letter, col in BADGES.items():
    (FIG / f"badge_{letter}.svg").write_text(
        f'<svg xmlns="http://www.w3.org/2000/svg" width="36" height="28" viewBox="0 0 36 28">'
        f'<rect x="1" y="1" width="34" height="26" rx="6" fill="{col}"/>'
        f'<text x="18" y="20" text-anchor="middle" font-family="Aptos, Helvetica, Arial, sans-serif" '
        f'font-size="17" font-weight="700" fill="#ffffff">{letter}</text></svg>\n')

# --- QR code for the paper ---------------------------------------------------------------------------
segno.make(PAPER_URL, error="m").save(FIG / "qr_paper.svg", scale=10, border=2, dark=INK, light="#ffffff")
print("wrote qr_paper")

rng = np.random.default_rng(0)

# --- f01: a metric over time, in four phases (example data) ------------------------------------------
t = np.arange(0, 120)
spans = [("warm-up", 0, 20), ("steady", 20, 55), ("burst", 55, 85), ("cool-down", 85, 120)]
burst = np.clip((t - 55) / 4, 0, 1) * np.clip((88 - t) / 4, 0, 1)  # 0 outside the burst, 1 inside
level = {"Ours": (60, 1.4), "Baseline A": (70, 3.4), "Baseline B": (95, 2.7), "Baseline C": (140, 2.0)}
fig, ax = plt.subplots(figsize=(W, 3.5))
bands(ax, spans, label_y=1.0)
for name, col in SERIES.items():
    base, peak = level[name]
    p99 = base * (1 + (peak - 1) * burst) * rng.lognormal(0, 0.05, len(t))
    ax.plot(t, p99, color=col, lw=2.6 if name == "Ours" else 1.9, label=name)
ax.set_xlim(0, 120)
ax.set_ylim(0, 400)
ax.set_yticks(range(0, 301, 100))
ax.set_xlabel("time (s)")
ax.set_ylabel("p99 latency (ms)  ↓ better")
ax.legend(ncol=4, loc="upper left", fontsize=14)
save(fig, "f01_example_timeseries")

# --- f02: two panels of grouped bars (example data) --------------------------------------------------
cats = ["W1", "W2", "W3", "W4"]
tput = {"Ours": [9.1, 7.4, 11.2, 6.3], "Baseline A": [5.2, 4.9, 6.0, 4.1], "Baseline B": [3.8, 4.4, 5.1, 2.9]}
lat = {"Ours": [38, 52, 31, 64], "Baseline A": [71, 88, 63, 120], "Baseline B": [95, 84, 90, 151]}
fig, (ax, bx) = plt.subplots(1, 2, figsize=(W, 3.4), gridspec_kw={"wspace": 0.28})
bars(ax, cats, [(s, tput[s], SERIES[s]) for s in tput], fmt="{:.1f}", size=12)
bars(bx, cats, [(s, lat[s], SERIES[s]) for s in lat], size=12)
ax.set_ylabel("throughput (k req/s)  ↑ better")
bx.set_ylabel("p99 latency (ms)  ↓ better")
title(ax, "a", "throughput")
title(bx, "b", "tail latency")
ax.set_ylim(0, 13)
bx.set_ylim(0, 175)
fig.legend(handles=[Patch(color=SERIES[s], label=s) for s in tput], loc="lower center",
           bbox_to_anchor=(0.5, 0.98), ncol=3)
save(fig, "f02_example_bars")
