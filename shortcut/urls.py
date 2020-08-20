from django.urls import path
from .views import shortly, redirect_to_url

app_name = 'shortcut'

urlpatterns = [
    path('', shortly, name='index'),
    path('<str:url_id>', redirect_to_url, name='url_redirect'),
]
