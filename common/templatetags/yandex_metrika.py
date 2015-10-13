__author__ = 'Сергей'

from django import template

register = template.Library()

@register.inclusion_tag('common/yandex_metrika.html')
def yandex_metrika(counter_id, **kwargs):
    result = kwargs
    result['id'] = counter_id
    return result
