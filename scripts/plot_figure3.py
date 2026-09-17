#!/usr/bin/env python3
"""Draw manuscript Figure 3 from equations 19-22 (orni_slab.G, impulse_response)."""
from __future__ import annotations

import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.gridspec import GridSpec
from matplotlib.ticker import FuncFormatter

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from orni_slab import TABLE1, G, impulse_response  # noqa: E402

TRIM = FuncFormatter(lambda v, _: f"{v:g}")
OUT = ROOT / "figures" / "figure3_Gt.png"
COL = {"xx": "#231F20", "xy": "#ED1F24", "yx": "#3C4CA8", "yy": "#55C270"}


def main() -> None:
    tf = np.linspace(0.0, 5.0, 6001)
    fig = plt.figure(figsize=(9.0, 10.6))
    top = GridSpec(2, 3, figure=fig, hspace=0.09, wspace=0.22,
                   left=0.085, right=0.985, top=0.963, bottom=0.585)
    bot = GridSpec(2, 3, figure=fig, hspace=0.28, wspace=0.22,
                   left=0.085, right=0.985, top=0.505, bottom=0.045)
    axes = [[fig.add_subplot(top[0, j]) for j in range(3)],
            [fig.add_subplot(top[1, j]) for j in range(3)],
            [fig.add_subplot(bot[0, j]) for j in range(3)],
            [fig.add_subplot(bot[1, j]) for j in range(3)]]
    letters = iter("abcdefghijkl")
    for j, name in enumerate(TABLE1):
        g = G(tf, name)
        peak = max(np.max(np.abs(g[k])) for k in ("xx", "xy", "yx", "yy"))
        for k in ("xx", "xy", "yx", "yy"):
            axes[0][j].plot(tf, g[k] / peak, color=COL[k], lw=1.5, label=f"$G^{{{k}}}$")
        u, v = impulse_response(tf, name, 1.0, 1.0)
        w = max(np.max(np.abs(u)), np.max(np.abs(v)))
        axes[1][j].plot(tf, u / w, color="#3C4CA8", lw=1.5, label=r"$u/w$")
        axes[1][j].plot(tf, v / w, color="#ED1F24", lw=1.5, label=r"$v/w$")
        axes[2][j].plot(u / w, v / w, color="#231F20", lw=1.2)
        for m in range(1, 6):
            k = int(np.argmin(np.abs(tf - m)))
            axes[2][j].plot(u[k] / w, v[k] / w, "o", mfc="#ED1F24", mec="k", ms=4)
        # trajectory: integrate (u, v) in inertial-period time
        dt = tf[1] - tf[0]
        x = np.cumsum(u) * dt
        y = np.cumsum(v) * dt
        s = max(np.max(np.abs(x)), np.max(np.abs(y)))
        axes[3][j].plot(x / s, y / s, color="#231F20", lw=1.2)
        for i, ylab in enumerate([r"$G/\max|G|$", r"$u/w,\,v/w$", r"$v/w$", r"$y$"]):
            axes[i][j].set_title(f"({next(letters)}) {name}", fontsize=10)
            axes[i][j].xaxis.set_major_formatter(TRIM)
            axes[i][j].yaxis.set_major_formatter(TRIM)
            if j == 0:
                axes[i][j].set_ylabel(ylab)
        axes[0][j].set_xlim(0, 5)
        axes[1][j].set_xlim(0, 5)
        axes[0][j].set_xlabel(r"$t\times f$")
        axes[1][j].set_xlabel(r"$t\times f$")
        axes[2][j].set_aspect("equal")
        axes[3][j].set_aspect("equal")
        axes[2][j].set_xlabel(r"$u/w$")
        axes[3][j].set_xlabel(r"$x$")
        if j == 0:
            axes[0][j].legend(fontsize=7, frameon=False, loc="upper right")
    OUT.parent.mkdir(exist_ok=True)
    fig.savefig(OUT, dpi=200)
    print("wrote", OUT)


if __name__ == "__main__":
    main()
