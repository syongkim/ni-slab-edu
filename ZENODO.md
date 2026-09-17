# GitHub + Zenodo (DOI)

Local: `/pao1/work/papers/orni/deposit/` → GitHub `syongkim/ni-slab-edu`.
Title: **Slab model with two-dimensional full horizontal velocity-gradient tensor**.

## Order

1. Zenodo switch **ON** for `syongkim/ni-slab-edu`.
2. GitHub Release Publish from a tag (`v0.1.1`).

## If the Zenodo page shows Failed

Do these in order:

1. **Click the red Failed row** — Zenodo often shows the real error (CITATION / permission / download).
2. GitHub → Settings → Applications → **Zenodo** → Repository access  
   → include **`ni-slab-edu`** (rename from `orni-slab-edu` often leaves the old name only).
3. Zenodo → GitHub → `ni-slab-edu`: switch **OFF**, refresh, switch **ON**.
4. Delete the failed GitHub Releases (keep tags if you want).
5. Publish a **new** tag release:  
   https://github.com/syongkim/ni-slab-edu/releases/new?tag=v0.1.1

## Manual DOI (if webhook keeps failing)

1. Download: https://github.com/syongkim/ni-slab-edu/archive/refs/tags/v0.1.1.zip
2. https://zenodo.org/uploads/new → upload the zip → **Reserve DOI** → Publish.
3. Put version + concept DOI into `CITATION.cff`.
