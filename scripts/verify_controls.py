#!/usr/bin/env python3
"""Controls: G matches scipy.linalg.expm; H recovers the isotropic slab."""
from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
from scipy.linalg import expm

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from orni_slab import G, Hc, TABLE1, coefficients  # noqa: E402


def check_isotropic_H() -> None:
    c = dict(ux=0.0, uy=0.0, vx=0.0, vy=0.0, rx=0.05, ry=0.05)
    sig = np.linspace(-3, 3, 2001)
    got = Hc(sig, c)
    # 1 / [i(sigma + 1) + r] with f = 1
    expect = 1.0 / (1j * (sig + 1.0) + 0.05)
    err = np.max(np.abs(got - expect))
    assert err < 1e-12, err
    print(f"PASS isotropic H  max|err|={err:.2e}")


def check_G_expm(case: str = "C2") -> None:
    coef = coefficients(case)
    # A matrix of the linear system du/dt = A u + tau/(rho h), with f = 1
    # u_t = -(rx+ux) u + (1 - uy) v
    # v_t = -(1 + vx) u - (ry+vy) v
    A = np.array([[-(coef.rx + coef.ux), (1.0 - coef.uy)],
                  [-(1.0 + coef.vx), -(coef.ry + coef.vy)]], float)
    tf = np.linspace(0.0, 5.0, 501)
    g = G(tf, case)
    # G_matrix = expm(A t) with t = 2 pi tf (angular), and rho h G = that matrix
    errs = []
    for i, tfi in enumerate(tf[::50]):
        Gm = expm(A * (2 * np.pi * tfi))
        errs.append(abs(Gm[0, 0] - g["xx"][i * 50]))
        errs.append(abs(Gm[0, 1] - g["xy"][i * 50]))
        errs.append(abs(Gm[1, 0] - g["yx"][i * 50]))
        errs.append(abs(Gm[1, 1] - g["yy"][i * 50]))
    err = max(errs)
    assert err < 1e-9, err
    print(f"PASS G vs expm ({case})  max|err|={err:.2e}")


def check_Gyx_relation(case: str = "C2") -> None:
    coef = coefficients(case)
    tf = np.linspace(0.05, 5.0, 200)
    g = G(tf, case)
    # G^yx = -a^2 G^xy
    err = np.max(np.abs(g["yx"] + coef.a**2 * g["xy"]))
    assert err < 1e-12, err
    print(f"PASS G^yx = -a^2 G^xy ({case})  max|err|={err:.2e}")


if __name__ == "__main__":
    check_isotropic_H()
    for name in TABLE1:
        check_G_expm(name)
        check_Gyx_relation(name)
    print("ALL CONTROLS PASSED")
