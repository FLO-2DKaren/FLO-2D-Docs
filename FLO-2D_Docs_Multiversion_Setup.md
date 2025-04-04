
# FLO-2D Pro Documentation Multiversion Setup Summary

## ✅ Project Structure
- `source/` contains `conf.py`, `index.rst`, `_templates/`, and `style/`.
- Logo image (`FLO-2D Transparent.png`) is in the root and referenced via `../` in `conf.py`.
- Custom template file `versions.html` is located in `source/_templates/`.

## ✅ .gitignore & .gitattributes
- Cleaned-up `.gitignore` to ignore `_build/`, `__pycache__/`, `.idea/`, etc.
- Added `.gitattributes` to normalize line endings across systems.

## ✅ Git Branch System
- Branches: `Build21`, `Build23`, `Build25`.
- Each branch created from `main` using `create_doc_branch.py`.
- Branch-specific version headers inserted into `index.rst`.
- All branches committed cleanly and ready for `sphinx-multiversion`.

## ✅ Sphinx Config
- Using `sphinx_rtd_theme` with `sphinx-multiversion`.
- Multiversion settings in `conf.py`:
  ```python
  smv_branch_whitelist = r'^Build.*$'
  smv_tag_whitelist = r'^$'
  smv_remote_whitelist = r'^origin$'
  ```

## ✅ Version Selector
- Working correctly with `versions.html` override.
- Order reversed to show latest version (`Build25`) first using `{% for item in versions|reverse %}`.

## ✅ Build Process
- `sphinx-multiversion source build/html` builds all branches.
- Output includes version tabs and works correctly.

---

## 🔜 Next Phase: Building Each Version

### Goal
Add real content to:
- `Build21`
- `Build23`
- `Build25`

### Plan
1. Switch to each branch (`git checkout Build21`)
2. Add content in:
   - `source/index.rst`
   - New `.rst` files (e.g., `setup.rst`, `pro.rst`, etc.)
3. Update the `toctree` in `index.rst` to include the new pages
4. Rebuild with `sphinx-multiversion` to test
