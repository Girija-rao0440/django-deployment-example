from django import template

register=template.Library()

def cut(value,arg):
    """
cuts out all value of arg
    """
    return value.replace(arg,'')

register.filter('cut',cut)
