# GitHub + Zenodo (DOI)

Local path: `/pao1/work/papers/orni/deposit/` (GitHub root of `syongkim/ni-slab-edu`).
Title / description: **Slab model with two-dimensional full horizontal velocity-gradient tensor**.

## Correct order

1. Create empty **public** repo `ni-slab-edu` (no README/license on GitHub).
2. Push `main` + tag `v0.1.0` — **no Release yet**.
3. Zenodo → GitHub → switch **on** for `syongkim/ni-slab-edu`.
4. **Then** publish GitHub Release from tag `v0.1.0`.

Zenodo only harvests Releases published **after** the switch is on.

## Push

```bash
cd /pao1/work/papers/orni/deposit
git push -u origin main
git push origin v0.1.0
```

## Zenodo switch

1. https://zenodo.org — log in with GitHub (`syongkim`).
2. Top-right GitHub icon → **GitHub**.
3. Find `syongkim/ni-slab-edu` → switch **on**.
4. If missing: GitHub → Settings → Applications → **Zenodo** → grant `ni-slab-edu`.

## Release (only after switch is on)

https://github.com/syongkim/ni-slab-edu/releases/new?tag=v0.1.0

## Record DOIs

Put version DOI and concept DOI into `CITATION.cff`.

Old name `orni-slab-edu` is retired; do not flip Zenodo on that repo.

## If Zenodo shows Failed

Usually the GitHub webhook rejected `.zenodo.json`. This deposit no longer ships that file (same as `cssim-fol`). Delete the failed GitHub Release, keep tag `v0.1.0` (or retag after the push), confirm the Zenodo switch is still **on**, then Publish release again.
