from django import template

register = template.Library()

@register.filter
def truncate_words(value, num):
    words = value.split()
    if len(words) > num:
        return ' '.join(words[:num]) + '...'
    return value
