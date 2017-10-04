from django.shortcuts import render
from .models import Merch


# Create your views here.
def get_merch(type, merch_id=None):
    if merch_id is None:
        return Merch.objects.filter(
            wear_type=type)
    else:
        return Merch.objects.filter(
            wear_type=type,
            pk=merch_id)


def merch_detail(request, type, merch_id=None):
    context = {}
    merch = get_merch(type, merch_id)
    context['merch'] = merch
    context['list'] = False
    if len(merch) > 1:
        context['list'] = True
    return render(request, 'merch_detail.html', context)
