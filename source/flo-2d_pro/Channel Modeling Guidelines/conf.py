import os
# import sys
sys.path.insert(0, os.path.abspath('.'))

project = 'Channel Modeling Guidelines'
author = 'Your Name or Team'
release = '1.0'

extensions = ['sphinx.ext.mathjax']

html_theme = "sphinx_rtd_theme"
html_static_path = ['_static']
html_css_files = [
    ('css/custom.css', {'priority': 1000})
]

numfig = True
numfig_secnum_depth = 1

mathjax_path = "https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"
mathjax3_config = {
    "tex": {
        "tags": "none",
        "useLabelIds": True
    },
    "options": {
        "displayAlign": "right"
    }
}
