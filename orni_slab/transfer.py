"""Transfer function H (manuscript equations 12-16).

With f = 1 and all rates in units of f,

    H^xx = (i sigma + R b) / (rho h xi)
    H^xy = (F / a) / (rho h xi)
    H^yx = - (F a) / (rho h xi)
    H^yy = (i sigma + R/b) / (rho h xi)
    xi   = (i sigma + R/b)(i sigma + R b) + F^2

The returned arrays are the dimensionless product rho h H, so rho and h cancel.
"""
from __future__ import annotations

from typing import Mapping

import numpy as np

from .params import Coefficients, coefficients


def H(sigma: np.ndarray, c: str | Mapping[str, float] | Coefficients,
      F: float | np.ndarray | None = None) -> dict[str, np.ndarray]:
    """Four components of H, equations 12-15, as rho h H (f = 1)."""
    coef = c if isinstance(c, Coefficients) else coefficients(c)
    sig = np.asarray(sigma, dtype=float)
    Ff = coef.F if F is None else np.asarray(F, dtype=float)
    Rob, Rb, a = coef.R_over_b, coef.R_b, coef.a
    xi = (1j * sig + Rob) * (1j * sig + Rb) + Ff**2
    return {
        "xx": (1j * sig + Rb) / xi,
        "xy": (Ff / a) / xi,
        "yx": -(Ff * a) / xi,
        "yy": (1j * sig + Rob) / xi,
        "xi": xi,
    }


def Hc(sigma: np.ndarray, c: str | Mapping[str, float] | Coefficients,
       F: float | np.ndarray | None = None) -> np.ndarray:
    """Complex rotary response to a unit stress in x: H^xx + i H^yx (equation 12, 14).

    This is what manuscript Figure 2 plots. In the isotropic, gradient-free limit it
    collapses to 1 / [i(sigma + 1) + r], equation 3 of Kim et al. (2014).
    """
    h = H(sigma, c, F=F)
    return h["xx"] + 1j * h["yx"]
