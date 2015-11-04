from django import template
from pygments import highlight
from pygments.formatters import HtmlFormatter
from pygments.lexers import get_lexer_by_name, guess_lexer
import markdown as md

register = template.Library()

@register.filter
def markdown(arg):
    """Filter arg through markdown

    :arg: markdown string
    :returns: html

    """
    extentions = ['codehilite', 'fenced_code']
    extention_configs = {
            'codehilite':
            {
                'css_class': 'codehilite',
                'pygments_style': 'trac',
                'noclasses': 'True'
                }
            }
    return md.markdown(arg, extentions, extention_configs)
