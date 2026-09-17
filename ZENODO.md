# GitHub + Zenodo (DOI)

Package root: `orni-slab-edu`.
Title / description: **Slab model with two-dimensional full horizontal velocity-gradient tensor**.

## 0. Local

```bash
cd /pao1/work/orni-slab-edu
git log --oneline
```

## 1. GitHub repo (`syongkim/orni-slab-edu`)

Create an empty **public** repository at https://github.com/new
(no README, no license on GitHub). Then:

```bash
cd /pao1/work/orni-slab-edu
git remote add origin git@github.com:syongkim/orni-slab-edu.git
git push -u origin main
git tag -a v0.1.0 -m "Educational release: H (eqs 12-16), G (eqs 17-22), Figures 2 and 3"
git push origin v0.1.0
```

On GitHub: **Releases → Draft a new release** from tag `v0.1.0`
(title: `v0.1.0`, description from README one-liner).

## 2. Zenodo ↔ GitHub

1. https://zenodo.org — log in with GitHub (`syongkim`).
2. GitHub icon → **GitHub** → find `syongkim/orni-slab-edu` → switch **on**.
3. If missing: GitHub → Settings → Applications → Zenodo → grant repo access.

## 3. DOI

Zenodo mints the DOI when the GitHub Release is published (step 1).
Record version DOI and concept DOI in `CITATION.cff` after minting.
