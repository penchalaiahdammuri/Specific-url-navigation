from django.urls import path
from app1.views import *
app_name='penchal'

urlpatterns=[
    path('a1/',a1,name='a1'),
    path('RRR/',RRR,name='RRR'),
    path('KGF/',KGF,name='KGF'),
]