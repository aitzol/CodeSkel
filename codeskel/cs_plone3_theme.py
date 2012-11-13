from zopeskel import Plone3Theme as ZSPlone3Theme

class Plone3Theme(ZSPlone3Theme):
    _template_dir = 'templates/plone3_theme'
    summary = 'A Theme for Plone 3/4 with no browser resources'
    skinbase = 'Sunburst Theme'

    def post(self, command, output_dir, vars):
        pass
