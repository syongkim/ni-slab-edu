"""Frozen coefficients of Table 1 and the derived scalars F, a, b, R, vartheta."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Mapping

import numpy as np

# Table 1 of the manuscript (angular rates in units of f).
TABLE1: dict[str, dict[str, float]] = {
    "C1": dict(ux=0.0, vy=0.0, vx=0.0, uy=0.0, rx=0.02, ry=0.03),
    "C2": dict(ux=0.0, vy=0.0, vx=-0.05, uy=-0.15, rx=0.02, ry=0.03),
    "C3": dict(ux=0.15, vy=0.10, vx=0.0, uy=0.0, rx=0.02, ry=0.03),
}


@dataclass(frozen=True)
class Coefficients:
    """Dimensionless rates (units of f) and the derived scalars of equations 7-10."""

    ux: float
    uy: float
    vx: float
    vy: float
    rx: float
    ry: float

    @property
    def F(self) -> float:
        """Equation 7: F = sqrt((f - u_y)(f + v_x)) with f = 1."""
        return float(np.sqrt((1.0 - self.uy) * (1.0 + self.vx)))

    @property
    def a(self) -> float:
        return float(np.sqrt((1.0 + self.vx) / (1.0 - self.uy)))

    @property
    def b(self) -> float:
        Rob, Rb = self.rx + self.ux, self.ry + self.vy
        return float(np.sqrt(Rb / Rob)) if Rob > 0 else float("nan")

    @property
    def R_over_b(self) -> float:
        return self.rx + self.ux

    @property
    def R_b(self) -> float:
        return self.ry + self.vy

    @property
    def r_e(self) -> float:
        """Equation 25: r^e = (r^a + delta)/2 with r^a = r^x + r^y, delta = u_x + v_y."""
        return 0.5 * (self.rx + self.ry + self.ux + self.vy)

    @property
    def vartheta(self) -> float:
        """vartheta = sqrt(4 F^2 - (R b - R/b)^2), so f^e = vartheta/2."""
        d = self.R_b - self.R_over_b
        return float(np.sqrt(4.0 * self.F**2 - d**2))

    @property
    def f_e(self) -> float:
        return 0.5 * self.vartheta


def coefficients(case: str | Mapping[str, float]) -> Coefficients:
    c = TABLE1[case] if isinstance(case, str) else dict(case)
    return Coefficients(**{k: float(c[k]) for k in ("ux", "uy", "vx", "vy", "rx", "ry")})
