from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .forms import URLForm
from .models import URL, create_url_id


# Create your views here.
def contraction(request):
    form = URLForm()
    if request.method == 'POST':
        form = URLForm(request.POST)
        if form.is_valid():
            short_url = URL(url_id=create_url_id(), link=form.cleaned_data['link'])
            short_url.save()
            absolute_uri = request.build_absolute_uri() + short_url.url_id
            return render(request, 'shortcut/base.html',
                          {
                              'form': form,
                              'absolute_uri': absolute_uri,
                          })


    else:

        return render(request, 'shortcut/base.html', {
            'form': form
        })


def redirect_to_url(request, url_id):
    url = get_object_or_404(URL, url_id=url_id)
    url.usage += 1
    url.save()
    return HttpResponseRedirect(url.link)
