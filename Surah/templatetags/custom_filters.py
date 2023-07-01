from django import template

register = template.Library()

@register.filter
def any_item_empty(my_list):
    return any(not item for item in my_list)