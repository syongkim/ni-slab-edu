"""ni-slab-edu: slab model with two-dimensional full horizontal velocity-gradient tensor.

Educational Python for the extended slab operator of Kim (ORNI manuscript).
Implements the transfer function H (equations 12-16) and the Green function G
(equations 17-22), and redraws manuscript Figures 2 and 3 from those closed forms.

All rates are angular (rad/unit-time). Spectra and axes that the manuscript plots in
cycles per day are conversions of those angular rates by 2 pi, as stated in the text.
"""

from .params import TABLE1, coefficients
from .transfer import H, Hc
from .green import G, impulse_response

__all__ = ["TABLE1", "coefficients", "H", "Hc", "G", "impulse_response"]
__version__ = "0.1.0"
