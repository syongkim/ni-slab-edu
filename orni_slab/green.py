"""Green function G (manuscript equations 17-22).

Equations 17-18 are the convolutions of G with the wind stress. Equations 19-22 are
the four components. With f = 1, t counted in inertial periods (t_phys * f), and all
rates angular,

    E = exp(-0.5 (R b + R/b) * 2 pi t_f)
    G^xx ~ E [ cos(th w/2) + (Rb - R/b)/th sin(th w/2) ]
    G^xy ~ E * 2 (f - u_y)/th sin(th w/2)
    G^yx ~ -E * 2 (f + v_x)/th sin(th w/2)
    G^yy ~ E [ cos(th w/2) - (Rb - R/b)/th sin(th w/2) ]

with w = 2 pi t_f and th = vartheta. The returned arrays are rho h G, so the common
factor 1/(rho h) is divided out.
"""
from __future__ import annotations

from typing import Mapping

import numpy as np

from .params import Coefficients, coefficients


def G(t_f: np.ndarray, c: str | Mapping[str, float] | Coefficients) -> dict[str, np.ndarray]:
    """Four components of G(t), equations 19-22, as rho h G (f = 1).

    Parameters
    ----------
    t_f :
        Time in inertial periods, t * f / (2 pi) would be wrong; here t_f = t_phys * f
        with f the angular Coriolis frequency, so one inertial period is t_f = 1 when
        the oscillation carries 2 pi. Manuscript Figure 3 uses the abscissa t * f with
        that convention (ticks at 1, 2, ... inertial periods).
    """
    coef = c if isinstance(c, Coefficients) else coefficients(c)
    tf = np.asarray(t_f, dtype=float)
    P, Q = 1.0 - coef.uy, 1.0 + coef.vx
    X, Y = coef.R_over_b, coef.R_b
    th = np.sqrt(4.0 * P * Q - (Y - X) ** 2)
    w = 2.0 * np.pi * tf
    E = np.exp(-0.5 * (X + Y) * w)
    cs, sn = np.cos(th * w / 2.0), np.sin(th * w / 2.0)
    return {
        "xx": E * (cs + (Y - X) / th * sn),
        "xy": E * (2.0 * P / th) * sn,
        "yx": -E * (2.0 * Q / th) * sn,
        "yy": E * (cs - (Y - X) / th * sn),
        "vartheta": th,
        "envelope": E,
    }


def impulse_response(t_f: np.ndarray, c: str | Mapping[str, float] | Coefficients,
                     tau_x: float = 1.0, tau_y: float = 1.0) -> tuple[np.ndarray, np.ndarray]:
    """Equations 17-18 for an impulse (tau^x, tau^y) = (tau_x, tau_y) at t = 0."""
    g = G(t_f, c)
    u = tau_x * g["xx"] + tau_y * g["xy"]
    v = tau_x * g["yx"] + tau_y * g["yy"]
    return u, v
