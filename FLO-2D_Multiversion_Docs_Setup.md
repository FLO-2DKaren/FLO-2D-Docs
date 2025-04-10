
# FLO-2D Multiversion Documentation Setup Guide

## ✅ Step-by-Step Guide

### 🧱 1. Branch Setup in Git

```bash
git checkout -b Build21
# Add content for Build21
git push -u origin Build21

git checkout -b Build23
# Add content for Build23
git push -u origin Build23

git checkout -b Build25
# Add content for Build25
git push -u origin Build25

# Return to main
git checkout main
```

---

### ⚙️ 2. Configure `conf.py`

In your `source/` directory, include the following in `conf.py`:

```python
smv_tag_whitelist = r'^$'
smv_branch_whitelist = r'^(main|Build.*)$'
smv_remote_whitelist = r'^origin$'

extensions = [
    'sphinxcontrib.mermaid',
    'sphinx_multiversion'
]

templates_path = ['_templates']

html_context = {
    'current_version': "main",
}
```

Also make sure you have `source/_templates/versions.html` for version dropdown.

---

### 🧾 3. Add Landing Page to `main`

Edit `source/index.rst` in `main` branch:

```rst
Welcome to FLO-2D Documentation
===============================

This is the landing page for all builds of the documentation.

.. toctree::
   :maxdepth: 1

   Build25/index
   Build23/index
   Build21/index
```

---

### 🧰 4. Add GitHub Actions Workflow

Save this as `.github/workflows/main.yml`:

```yaml
name: Build and publish multiversion documentation

on:
  push:
    branches: [ main, Build* ]
  workflow_dispatch:

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout all branches
        uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.12'

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install sphinx sphinx-multiversion sphinx-rtd-theme sphinxcontrib-mermaid ghp-import

      - name: Build multiversion docs
        run: |
          sphinx-multiversion source _site

      - name: List _site contents
        run: |
         ls -R _site

      - name: Add root index.html
        run: |
          echo '<!DOCTYPE html><html><head><meta http-equiv="Refresh" content="0; url=Build25/index.html" /></head><body><p>Redirecting to Build25...</p></body></html>' > _site/index.html

      - name: Deploy using ghp-import
        run: |
          ghp-import -n -p -f _site
```

---

### 🌍 5. Enable GitHub Pages

- Go to your repo → **Settings > Pages**
- Set **Source**: `Deploy from a branch`
- Set **Branch**: `gh-pages` → `/ (root)`
- Click **Save**

---

### 🚀 6. Trigger Deployment

From the `main` branch, run:

```bash
git add .
git commit -m "Initial deploy of multiversion documentation"
git push origin main
```

OR use **Actions → main.yml → Run workflow**.

---

### 🌐 7. Access Your Site

Visit:

```
https://<your-username>.github.io/<your-repo-name>/
```

It redirects to Build25 and includes version tabs.
