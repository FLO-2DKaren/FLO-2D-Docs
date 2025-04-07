# Configuration file for the Sphinx documentation builder

# -- Project information -----------------------------------------------------
project = 'FLO-2D Documentation'
copyright = '2023, FLO-2D Software, Inc.'
author = 'FLO-2D Software, Inc.'

# -- General configuration ---------------------------------------------------
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.mathjax',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',
]

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# Add any custom styles
html_css_files = [
    'css/custom.css',
]

# -- Version Options ---------------------------------------------------------
version = 'latest'
