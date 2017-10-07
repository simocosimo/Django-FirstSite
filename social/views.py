from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import RELATIONSHIP_FOLLOWING


# Create your views here.
@login_required
def homepage(request, user_id, active=False):
    context = {}
    context['home'] = active
    context['amifollowing'] = False
    user = request.user
    context['user'] = user
    if not active:
        if int(user_id) == request.user.pk:
            return redirect('homepage')
        prf = User.objects.get(pk=user_id)
        context['user'] = prf
        followings = prf.profile.get_following()
        followers = prf.profile.get_followers()
        merch = prf.profile.get_merchPossession()
        if user.profile in followers:
            context['amifollowing'] = True
    else:
        followings = user.profile.get_following()
        followers = user.profile.get_followers()
        merch = user.profile.get_merchPossession()

    uf = []
    ufs = []
    for f in followings:
        uf.append(User.objects.get(pk=f.user_id))
    for fs in followers:
        ufs.append(User.objects.get(pk=fs.user_id))
    context['following'] = uf
    context['followers'] = ufs
    context['n_following'] = len(uf)
    context['n_followers'] = len(ufs)
    context['merch'] = merch
    context['n_merch'] = len(merch)
    return render(request, 'profile.html', context)


@login_required
def follow(request, user_id):
    user = request.user.profile
    prf = User.objects.get(pk=user_id).profile
    user.add_relationship(prf, RELATIONSHIP_FOLLOWING)
    return redirect('profile', user_id=int(user_id))


@login_required
def unfollow(request, user_id):
    user = request.user.profile
    prf = User.objects.get(pk=user_id).profile
    user.remove_relationship(prf, RELATIONSHIP_FOLLOWING)
    return redirect('profile', user_id=int(user_id))
