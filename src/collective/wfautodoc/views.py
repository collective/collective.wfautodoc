from Products.CMFCore.utils import getToolByName
from Products.Five.browser import BrowserView
from .generator import generate_gv

class GVFileView(BrowserView):
    
    def __call__(self):
        self.request.response.setHeader('Content-Type', 'text/vnd.graphviz')
        self.request.response.setHeader('Content-Disposition', 
                                        'attachment; filename=%s.gv' % \
                                        self.context.getId())
        return generate_gv(self.context)