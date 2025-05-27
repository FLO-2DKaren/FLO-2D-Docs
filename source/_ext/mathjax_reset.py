from docutils import nodes
from sphinx.transforms import SphinxTransform
import os

class MathJaxResetTransform(SphinxTransform):
    default_priority = 500

    def apply(self):
        docname = self.env.docname  # e.g., 'flo-2d-pro/Reference Manual/Chapter 2'
        if not docname:
            return

        # Match specific subfolders
        if docname.startswith("flo-2d-pro/Reference Manual/Chapter"):
            chapter_number = docname.split("/")[-1].split(" ")[1]
        elif docname.startswith("flo-2d-pro/Channel Modeling Guidelines/Chapter"):
            chapter_number = docname.split("/")[-1].split(" ")[1]
        else:
            return  # Not a chapter file in one of the target folders

        # Inject MathJax reset script with proper chapter number prefix
        script = f"""
        <script>
          MathJax.texReset();
          MathJax.tags.reset();
          MathJax.tags.counter = 0;
          MathJax.tags.allLabels = {{}};
          MathJax.startup.getComponents();
          MathJax.config.tex.tagFormat = {{
            number: (n) => "{chapter_number}." + n
          }};
        </script>
        """
        raw_node = nodes.raw('', script, format='html')
        self.document.insert(0, raw_node)

def setup(app):
    app.add_transform(MathJaxResetTransform)
