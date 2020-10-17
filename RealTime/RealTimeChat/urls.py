from django.urls import path
from django.contrib import admin
from .views import login,logging,student,administrator

urlpatterns=[
    path('admin/',admin.site.urls),
    path('login/',login,name='login'),
    path('logging/',logging,name='logging'),
    path('login/<str:data>',login,name='login'),
    path('student/',student,name='student'),
    path('administrator/',administrator,name='administrator'),
]