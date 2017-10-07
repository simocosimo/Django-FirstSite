from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Merch
from social.models import Profile


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
    user = request.user
    context['user'] = user
    context['merch'] = merch
    context['owned'] = False
    context['list'] = False
    if len(merch) > 1:
        context['list'] = True
    for m in user.profile.get_merchPossession():
        if merch[0] == m.merch:
            context['owned'] = True
    return render(request, 'merch_detail.html', context)


@login_required
def add_merch(request, user_id, merch_id):
    user = request.user.profile
    merch = Merch.objects.get(pk=merch_id)
    user.add_merchPossession(merch)
    return redirect('merch:merch_detail', type=int(merch.wear_type),
                                          merch_id=int(merch.pk))


@login_required
def rm_merch(request, user_id, merch_id):
    user = request.user.profile
    merch = Merch.objects.get(pk=merch_id)
    user.remove_merchPossession(merch)
    return redirect('merch:merch_detail', type=int(merch.wear_type),
                                          merch_id=int(merch.pk))
