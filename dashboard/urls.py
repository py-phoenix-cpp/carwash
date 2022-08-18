from django.urls import path
from dashboard.views import *

urlpatterns = [
    path('', Index, name='index'),
    path('haydovchilar/', DriversView, name='haydovchilar'),
    path('account/', Account_setting, name='account_setting'),
    path('asasd', asasd, name='asasd'),
]