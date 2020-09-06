from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib import messages
from .forms import URLForm
from .models import URL, create_url_id


# Create your views here.
def contraction_view(request):
    form = URLForm()

    if request.method == 'POST':
        form = URLForm(request.POST)
        link = None
        if form.is_valid():
            if request.user.is_authenticated:
                short_url = URL(user=request.user, url_id=create_url_id(), link=form.cleaned_data['link'])
                short_url.save()
                link = request.build_absolute_uri('/') + short_url.url_id
            else:
                messages.error(request, 'Вы не авторизованы.')
            return render(request, 'shortcut/base.html',
                          {
                              'form': form,
                              'link': link,
                          })


    else:

        return render(request, 'shortcut/base.html', {
            'form': form
        })


def redirect_to_url_view(request, url_id):
    url = get_object_or_404(URL, url_id=url_id)
    url.usage += 1
    url.save()
    return HttpResponseRedirect(url.link)
