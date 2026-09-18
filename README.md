# ni-slab-edu

**Slab model with two-dimensional full horizontal velocity-gradient tensor**

Educational Python for the extended slab mixed-layer operator in:

> Kim, S. Y. An extended slab mixed-layer operator for near-inertial currents with a
> full horizontal velocity-gradient tensor. *J. Geophys. Res. Oceans* (manuscript).

This repository implements **manuscript equations 12–16** (transfer function \(H\)) and
**equations 17–22** (Green function \(G\) and its convolutions), and redraws
**Figures 2 and 3** from those closed forms. It is meant for teaching and for checking
the algebra; it is not the full observational pipeline of the paper.

## What is included

| File | Role |
|---|---|
| `orni_slab/transfer.py` | \(H^{xx}, H^{xy}, H^{yx}, H^{yy}\) (eqs. 12–15), \(\xi\) (eq. 16), rotary \(H^{\mathrm{c}}=H^{xx}+iH^{yx}\) |
| `orni_slab/green.py` | \(G^{xx}, G^{xy}, G^{yx}, G^{yy}\) (eqs. 19–22); impulse response (eqs. 17–18) |
| `orni_slab/params.py` | Table 1 cases C1–C3 and the scalars \(F,a,b,r^{e},\vartheta\) |
| `scripts/plot_figure2.py` | Redraw Figure 2 |
| `scripts/plot_figure3.py` | Redraw Figure 3 |
| `scripts/verify_controls.py` | Independent checks against `scipy.linalg.expm` and the isotropic slab |

All rates are **angular** (as in the momentum equations). The manuscript plots spectra
in cycles per day as \(\sigma/2\pi\).

## Install and run

```bash
python3 -m pip install -r requirements.txt
python3 scripts/verify_controls.py
python3 scripts/plot_figure2.py
python3 scripts/plot_figure3.py
```

Figures are written to `figures/figure2_Hs.png` and `figures/figure3_Gt.png`.

## Minimal example

```python
import numpy as np
from orni_slab import Hc, G, TABLE1

sigma = np.linspace(-3, 3, 601)          # units of f
Hc_c2 = Hc(sigma, "C2")                  # Figure 2 quantity for Case C2

t_f = np.linspace(0, 5, 1001)            # inertial periods
g = G(t_f, TABLE1["C2"])                 # equations 19-22
```

## Controls

`scripts/verify_controls.py` must pass:

1. Isotropic \(H\) recovers \(1/[i(\sigma+f)+r]\).
2. Each component of \(G(t)\) matches `expm(A t)` with \(t = 2\pi\,t_{f}\).
3. \(G^{yx} = -a^{2} G^{xy}\).

## Citation

If you use this code, please cite the manuscript and this archive.

- Version DOI: https://doi.org/10.5281/zenodo.22821333
- Concept DOI: https://doi.org/10.5281/zenodo.22821332
- GitHub: https://github.com/syongkim/ni-slab-edu

See `CITATION.cff`. The Zenodo deposit was uploaded manually (the GitHub↔Zenodo
webhook listed Failed and does not show manual uploads).

## License

MIT (see `LICENSE`).
