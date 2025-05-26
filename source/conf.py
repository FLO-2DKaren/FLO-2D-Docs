import os
import re

# Detect subproject from current working directory
def detect_section():
    cwd = os.getcwd()
    if "tutorials" in cwd.lower():
        return "Tutorials"
    elif "flo-2d_plugin" in cwd.lower():
        return "FLO-2D_Plugin"
    elif "flo-2d_pro" in cwd.lower():
        return "FLO-2D Pro"
    elif "setup" in cwd.lower():
        return "Setup"
    return "Main"

section = detect_section()

# Base config
project = "FLO-2D Pro Documentation"
html_theme = "sphinx_rtd_theme"

# Section-specific logic
if section == "Tutorials":
    numfig = True
    numfig_secnum_depth = 2
    mathjax3_config = {
        "tex": {"tags": "all", "useLabelIds": True},
        "options": {"displayAlign": "right"}
    }
elif section == "FLO-2D_Plugin":
    numfig = True
    numfig_secnum_depth = 1
elif section == "FLO-2D Pro":
    numfig = True
    numfig_secnum_depth = 3
elif section == "setup":
    numfig = True
    numfig_secnum_depth = 3