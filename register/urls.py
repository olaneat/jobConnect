from django.urls import path, re_path, include
from . import views
from .apiviews import  UserDetail, RegistrationAPIView, LoginAPIView
from . import apiviews
from rest_framework import routers

app_name = 'register'
urlpatterns = [
    path('<int:pk>/user-detail', UserDetail.as_view(), name='user_detail'),
    path('login', LoginAPIView.as_view(), name='login'),
    path('signup', RegistrationAPIView.as_view(), name='signup'), 
    

]