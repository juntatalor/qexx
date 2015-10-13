__author__ = 'Сергей'

from django.contrib.sites.shortcuts import get_current_site


def current_site(request):
    site = get_current_site(request)
    detailed_site = getattr(site, 'detailedsite', None)
    return {'site': site,
            'detailed_site': detailed_site}
