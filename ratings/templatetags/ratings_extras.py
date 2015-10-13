__author__ = 'Сергей'

from django import template

from ratings.models import Rating
from ratings.forms import RatingForm

register = template.Library()

@register.assignment_tag
def get_ratings(product):
    return Rating.objects.all().filter(product=product,
                                       moderated=True)

@register.assignment_tag
def get_ratings_form(product):
    return RatingForm(initial={'product': product})