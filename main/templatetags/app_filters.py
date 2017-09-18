from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter(name='prepend_media')
@stringfilter
def prepend_media(value):
    """
    Prepends value with static dir if not external url.
    """
    if value[:4] != 'http':
        return '/uploads/' + value
    else:
        return value
