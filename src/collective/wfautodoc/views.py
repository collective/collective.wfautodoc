from .generator import generate_gv
from Products.CMFCore.utils import getToolByName
from Products.Five.browser import BrowserView
from pygraphviz import AGraph

import tempfile


class GVFileView(BrowserView):
    def __call__(self):
        self.request.response.setHeader("Content-Type", "text/vnd.graphviz")
        self.request.response.setHeader(
            "Content-Disposition", "attachment; filename=%s.gv" % self.context.getId()
        )
        return generate_gv(self.context)


class SVGFileView(BrowserView):
    def __call__(self):
        self.request.response.setHeader("Content-Type", "image/svg+xml")
        self.request.response.setHeader(
            "Content-Disposition", "inline; filename=%s.svg" % self.context.getId()
        )
        tfile = tempfile.NamedTemporaryFile(suffix=".svg")
        gv = generate_gv(self.context)
        ag = AGraph(string=gv)
        ag.layout()
        ag.draw(path=tfile, format="svg", prog="dot")
        tfile.seek(0)
        return tfile.read()
