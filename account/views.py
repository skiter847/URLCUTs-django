from django.shortcuts import render, redirect, reverse, get_object_or_404
from geoip2.errors import AddressNotFoundError
from .forms import UserRegistrationForm, UserLoginForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from shortcut.models import URL


# Create your views here.
def login_view(request):
    form = UserLoginForm(request)

    if request.method == 'POST':
        form = UserLoginForm(request, request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            if cd['user']:
                login(request, cd['user'])

            return redirect(reverse("shortcut:short"))

    return render(request, 'account/login.html', {
        'form': form
    })


def register_view(request):
    form = UserRegistrationForm()

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            User.objects.create_user(username=cd['username'], password=cd['password'])
            return redirect(reverse("account:login"))

    return render(request, 'account/register.html',
                  {
                      'form': form,
                  })


def logout_view(request):
    logout(request)
    return redirect(reverse("account:login"))


def profile_view(request, url_id=None):
    user = get_object_or_404(User, pk=request.user.pk)
    user_urls = user.url_set.all()

    url = None

    if url_id:
        url = get_object_or_404(URL, url_id=url_id)

    return render(request, 'account/profile.html', {
        'user_urls': user_urls,
        'url': url
    })
