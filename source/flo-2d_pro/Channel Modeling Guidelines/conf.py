# -- Path setup --------------------------------------------------------------
import sys, os
sys.path.insert(0, os.path.abspath("..."))

# -- HTML Output -------------------------------------------------------------
html_theme = "sphinx_rtd_theme"

import os

# Absolute path to shared _static directory
html_static_path = [os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '_static'))]

# Path to custom.css relative to _static
html_css_files = [
    'css/custom.css'
]


extensions += ['sphinx.ext.mathjax']  # Add mathjax support

# Equation numbering with section prefixes
numfig = True
numfig_secnum_depth = 1

# MathJax 3 config
mathjax_path = "https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"
mathjax3_config = {
    "tex": {
        "tags": "none",         # Let Sphinx handle equation numbering
        "useLabelIds": True
    },
    "options": {
        "displayAlign": "right"
    }
}
