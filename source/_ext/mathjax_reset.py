from docutils import nodes
from sphinx.transforms import SphinxTransform
import os

class MathJaxResetTransform(SphinxTransform):
    default_priority = 500

    def apply(self):
        docname = self.env.docname.lower()  # Normalize to lowercase
        if not docname:
            return

        # Normalize folder names (as Sphinx lowercases paths)
        if docname.startswith("flo-2d-pro/reference manual/chapter"):
            chapter_number = docname.split("/")[-1].split(" ")[1]
        elif docname.startswith("flo-2d-pro/channel modeling guidelines/chapter"):
            chapter_number = docname.split("/")[-1].split(" ")[1]
        else:
            return

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
