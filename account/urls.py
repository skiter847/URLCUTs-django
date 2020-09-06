from django.urls import path
from .views import logout_view, register_view, login_view, profile_view

app_name = 'account'

urlpatterns = [
    path('sign_in/', login_view, name='login'),
    path('sign_up/', register_view, name='register'),
    path('logout/', logout_view, name='logout'),
    path('profile/', profile_view, name='profile'),
    path('profile/<str:url_id>', profile_view, name='profile_by_detail')
]
