__author__ = 'Сергей'

from django import template

register = template.Library()


class ExtraPluralizeNode(template.Node):
    def __init__(self, s, p1, p2, num):
        self.s, self.p1, self.p2, self.num = s, p1, p2, template.Variable(num)

    def render(self, context):

        try:
            num = self.num.resolve(context)
        except template.VariableDoesNotExist:
            raise template.TemplateSyntaxError('Неверный формат количества')

        # 1 питон, 2 питона, 5 питонов, 11 питонов
        if num % 10 == 1 and num % 100 != 11:
            return self.s
        elif num % 10 in [2, 3, 4] and num % 100 not in [12, 13, 14]:
            return self.p1
        else:
            return self.p2


@register.tag
def extra_pluralize(parser, token):
    try:
        tag_name, s, p1, p2, num = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError('Недостаточно аргументов для тега extra_pluralize')

    return ExtraPluralizeNode(s, p1, p2, num)
