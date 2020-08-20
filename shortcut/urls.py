from django.urls import path
from .views import contraction, redirect_to_url

app_name = 'shortcut'

urlpatterns = [
    path('', contraction, name="contraction"),
    path('<str:url_id>', redirect_to_url, name='url_redirect'),
]
