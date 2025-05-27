# extensions/equation_reset.py

from sphinx.util import logging
logger = logging.getLogger(__name__)

def add_reset_js(app, pagename, templatename, context, doctree):
    chapter_number = extract_chapter_number(pagename)
    if not chapter_number:
        return

    reset_script = f"""
    <script>
    MathJax.texReset();
    MathJax.tags.reset();
    MathJax.tags.counter = 0;
    MathJax.tags.allLabels = {{}};
    MathJax.config.tex.tagFormat = {{
        number: function(n) {{ return "{chapter_number}." + n }}
    }};
    MathJax.startup.getComponents();
    </script>
    """

    context['metatags'] += reset_script

def extract_chapter_number(pagename):
    if "chapter2" in pagename:
        return "2"
    elif "chapter3" in pagename:
        return "3"
    return None

def setup(app):
    app.connect('html-page-context', add_reset_js)
