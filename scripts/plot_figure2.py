#!/usr/bin/env python3
"""Draw manuscript Figure 2 from equations 12-16 (orni_slab.Hc)."""
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

from orni_slab import TABLE1, Hc, coefficients  # noqa: E402

TRIM = FuncFormatter(lambda v, _: f"{v:g}")
OUT = ROOT / "figures" / "figure2_Hs.png"


def main() -> None:
    sig = np.linspace(-3.0, 3.0, 901)
    Ff = np.linspace(0.0, 2.0, 401)
    S, FF = np.meshgrid(sig, Ff)
    fig = plt.figure(figsize=(9.2, 8.4))
    maps = GridSpec(2, 3, figure=fig, hspace=0.16, wspace=0.14,
                    left=0.075, right=0.885, top=0.955, bottom=0.545)
    cuts = GridSpec(2, 3, figure=fig, hspace=0.12, wspace=0.14,
                    left=0.075, right=0.885, top=0.470, bottom=0.065)
    ax = [[fig.add_subplot(maps[i, j]) for j in range(3)] for i in range(2)]
    ax += [[fig.add_subplot(cuts[i, j]) for j in range(3)] for i in range(2)]

    amp = {n: np.log10(np.abs(Hc(S, TABLE1[n], F=FF))) for n in TABLE1}
    vmax = 0.5 * np.ceil(2 * max(a.max() for a in amp.values()))
    vmin = vmax - 3.0
    letters = iter("abcdefghijkl")
    for j, name in enumerate(TABLE1):
        c = coefficients(name)
        a = np.clip(amp[name], vmin, vmax)
        ax[0][j].pcolormesh(sig, Ff, a, vmin=vmin, vmax=vmax, cmap="jet", shading="auto")
        ax[1][j].pcolormesh(sig, Ff, np.degrees(np.angle(Hc(S, name, F=FF))),
                             vmin=-180, vmax=180, cmap="hsv", shading="auto")
        cut = Hc(sig, name)
        ax[2][j].plot(sig, np.log10(np.abs(cut)), "k-", lw=1.6)
        ax[3][j].plot(sig, np.degrees(np.angle(cut)), "k-", lw=1.6)
        for i in range(4):
            ax[i][j].set_title(f"({next(letters)}) {name}", fontsize=10)
            ax[i][j].axvline(-1, color="0.5", lw=0.8)
            ax[i][j].axvline(1, color="0.5", lw=0.8)
            ax[i][j].xaxis.set_major_formatter(TRIM)
            ax[i][j].yaxis.set_major_formatter(TRIM)
        for i in (0, 1):
            ax[i][j].plot([-c.F, c.F], [c.F, c.F], "w-", lw=0.7)
            ax[i][j].plot([-1, 1, 1, -1, -1], [0, 0, 1, 1, 0], "w-", lw=0.7)
            ax[i][j].set_xlim(-3, 3)
            ax[i][j].set_ylim(0, 2)
        ax[2][j].set_xlim(-3, 3)
        ax[3][j].set_xlim(-3, 3)
        ax[3][j].set_ylim(-180, 180)
        ax[3][j].set_yticks([-180, -90, 0, 90, 180])
        ax[0][j].set_ylabel(r"$F/f$" if j == 0 else "")
        ax[2][j].set_ylabel(r"$\log_{10}|H^{\mathrm{c}}|$" if j == 0 else "")
        ax[3][j].set_xlabel(r"$\sigma/f$")
        ax[3][j].set_ylabel("phase (deg)" if j == 0 else "")
    OUT.parent.mkdir(exist_ok=True)
    fig.savefig(OUT, dpi=200)
    print("wrote", OUT)


if __name__ == "__main__":
    main()
