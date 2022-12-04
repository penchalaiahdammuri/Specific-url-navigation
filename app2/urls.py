from django.urls import path
from app2.views import *
app_name='raja'
urlpatterns=[
    path('a2/',a2,name='a2'),
    path('DJ/',DJ,name='DJ'),
    path('HIT2/',HIT2,name='HIT2'),
]