from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def homepage(request):
    user = request.user
    followings = user.profile.get_following()
    uf = []
    for f in followings:
        uf.append(User.objects.get(pk=f.user_id))
    return render(request, 'home.html', {'active': user,
                                         'following': uf})


def detail_view(request, user_id):
    user = User.objects.get(pk=user_id)
    return render(request, 'profile.html', {'user': user})
