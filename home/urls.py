from django.urls import path
from .views import home, my_logout

urlpatterns = [
    path('logout/', my_logout, name='logout'),
    path('', home, name='minha_home'),
]