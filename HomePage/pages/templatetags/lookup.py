from django import template
register = template.Library()

@register.filter
def lookup_name(value, arg):
    return value[arg].name
    
@register.filter
def lookup_link(value, arg):
    return value[arg].link