from django.urls import path
from dashboard.views import *

urlpatterns = [
    path('', Index, name='index'),
    path('add-client/', addClientView, name='add-client'),
    path('client/', Clients, name='client'),
    path('list-clients/', listClientsView, name='list-clients'),
    path('login/', Login, name='login'),
    path('logout/', LogoutView, name='logout'),
]