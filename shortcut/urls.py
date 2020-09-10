from django.urls import path
from .views import contraction_view, redirect_to_url_view

app_name = 'shortcut'

urlpatterns = [
    path('', contraction_view, name="short"),
    path('<str:url_id>', redirect_to_url_view, name='url_redirect'),
]

