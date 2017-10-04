from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def homepage(request, user_id, active=False):
    context = {}
    context['home'] = active
    user = request.user
    context['user'] = user
    if not active:
        if int(user_id) == request.user.pk:
            return redirect('homepage')
        prf = User.objects.get(pk=user_id)
        context['user'] = prf
        followings = prf.profile.get_following()
        followers = prf.profile.get_followers()
    else:
        followings = user.profile.get_following()
        followers = user.profile.get_followers()

    uf = []
    ufs = []
    merch = user.profile.get_merchPossession()
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
