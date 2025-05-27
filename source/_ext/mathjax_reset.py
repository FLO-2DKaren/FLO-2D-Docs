# source/_ext/mathjax_reset.py
import os

def setup(app):
    app.connect("source-read", inject_reset_script)
    return {"version": "0.1", "parallel_read_safe": True}

def inject_reset_script(app, docname, source):
    chapter = os.path.basename(docname).lower()
    folder = os.path.dirname(docname).split("/")[-1].lower()

    # Assign a MathJax prefix by folder/chapter (e.g., "Reference Manual" → "1", "Channel Modeling Guidelines" → "2")
    chapter_prefix = {
        "reference manual": "1",
        "channel modeling guidelines": "2",
    }.get(folder, "0")

    # Inject the JavaScript only at the top of each chapter .rst
    if chapter.startswith("chapter"):
        script = f"""
.. raw:: html

   <script>
     MathJax.texReset();
     MathJax.tags.reset();
     MathJax.tags.counter = 0;
     MathJax.tags.allLabels = {{}};
     MathJax.config.tex.tagFormat = {{
       number: function(n) {{ return "{chapter_prefix}." + n; }}
     }};
     MathJax.startup.getComponents();
   </script>
"""
        source[0] = script + "\n" + source[0]
