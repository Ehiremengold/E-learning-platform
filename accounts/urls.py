from django.urls import path
from .views import registration_view, login_view, logout_view, update_account_view, profile_display


urlpatterns = [
    path('create-account/', registration_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('update-profile/', update_account_view, name='updateprofile'),
    path('profile/', profile_display, name='profile'),
]