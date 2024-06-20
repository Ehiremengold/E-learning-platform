from django.urls import path
from .views import landingpage, about, index


urlpatterns = [
    path('', landingpage, name='landingpage'),
    path('home/', index, name='home'),
    path('about/', about, name='about'),
]
