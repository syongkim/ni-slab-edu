# GitHub + Zenodo (DOI)

Local path: `/pao1/work/papers/orni/deposit/` (GitHub root of `syongkim/orni-slab-edu`).
Title / description: **Slab model with two-dimensional full horizontal velocity-gradient tensor**.

## Correct order (this is what failed before)

1. Repo public, code on `main`, tag `v0.1.0` present — **no Release yet**.
2. Zenodo → GitHub → switch **on** for `syongkim/orni-slab-edu`.
3. **Then** publish the GitHub Release from tag `v0.1.0`.

Zenodo only harvests Releases published **after** the switch is on.
Turning the switch on after a Release already exists does nothing for that Release.

## 1. Local / push

```bash
cd /pao1/work/papers/orni/deposit
# or: cd "$(git rev-parse --show-toplevel)"
git push origin main
git push origin v0.1.0
```

Do **not** create the Release yet.

## 2. Zenodo switch

1. https://zenodo.org — log in with GitHub (`syongkim`).
2. Top-right GitHub icon → **GitHub**.
3. Find `syongkim/orni-slab-edu` → switch **on**.
4. If the repo is missing:
   GitHub → Settings → Applications → **Zenodo** → Repository access
   → include `orni-slab-edu` (or all) → save → refresh Zenodo.

## 3. Publish Release (only after switch is on)

https://github.com/syongkim/orni-slab-edu/releases/new?tag=v0.1.0

Publish. Wait 1–2 minutes; the DOI appears on the Zenodo record and usually on the GitHub Release sidebar.

If the switch was late: delete that Release (keep the tag) and publish again, or tag `v0.1.1` and release that.

## 4. Record DOIs

Put version DOI and concept DOI into `CITATION.cff`.
