# -- Path setup --------------------------------------------------------------
import sys, os
sys.path.insert(0, os.path.abspath("..."))

# -- Project information -----------------------------------------------------
project = 'FLO-2D Pro Documentation'
copyright = "2025, Jimmy O'Brien, Noemi Gonzalez-Ramirez, Karen O'Brien, Robson Pachaly"
author = "Jimmy O'Brien, Noemi Gonzalez-Ramirez, Karen O'Brien, Robson Pachaly"
html_logo = "FLO-2D Transparent.png"

# -- Sphinx Multiversion Settings -------------------------------------------
# NOTE: Use one of the following settings depending on your build environment

# 🔁 FULL BUILD: Use this when building all branches (e.g., on GitHub Actions)
smv_tag_whitelist = r'^$'  # Exclude all tags
smv_branch_whitelist = r'^Build.*$'  # Include branches like Build21, Build23, etc.
smv_remote_whitelist = r'^origin$'  # Default remote

# 🔁 QUICK BUILD: Uncomment below for fast local dev on current branch
# smv_tag_whitelist = r'^$'
# smv_branch_whitelist = r'^(main|Tutorials)$'  # Change to your working branch
# smv_remote_whitelist = r'^$'  # Local only

# -- General configuration ---------------------------------------------------
extensions = [
    'sphinxcontrib.mermaid',
    'sphinx_multiversion'
]
templates_path = ['_templates']
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- HTML Output -------------------------------------------------------------
html_theme = "sphinx_rtd_theme"
html_static_path = ['_static']
html_css_files = [
    ('static/custom.css', {'priority': 1000})
]

# -- HTML Context for Version Dropdown (optional enhancement) ----------------
html_context = {
    'current_version': "main",
    # You can populate this with actual versions later using git refs or dynamically.
    # 'versions': [["Build21", "/Build21/"], ["Build23", "/Build23/"], ...]
}

# -- DOCX Output (if used) ---------------------------------------------------
docx_documents = [
    ('index', 'FLO-2D Tutorials.docx', {
         'title': 'FLO-2D Plugin for QGIS Tutorials',
         'created': 'Karen O\'Brien',
         'subject': 'Sphinx builder extension',
         'keywords': ['sphinx', 'docx', 'documentation']
     }, True),
]
docx_pagebreak_before_section = 1
