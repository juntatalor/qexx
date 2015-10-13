from django.template.loader import render_to_string
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from ratings.forms import RatingForm


@require_POST
@login_required
def add_rating(request):

    result = {}

    rating_form = RatingForm(request.POST)

    if rating_form.is_valid():
        new_rating = rating_form.save(commit=False)
        new_rating.user = request.user
        new_rating.save()

    result['html'] = render_to_string('ratings/rating_form.html', {
        'rating_form': rating_form,
        'success': rating_form.is_valid()
    })

    return JsonResponse(result)
