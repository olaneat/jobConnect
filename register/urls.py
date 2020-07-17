from django.urls import path, re_path, include
from . import views
from .apiviews import  UserDetail, RegistrationAPIView, LoginAPIView, FacebookLogin, TwitterLogin
from . import apiviews
from allauth.account.views import PasswordResetView
from rest_framework import routers

app_name = 'register'
urlpatterns = [
    path('<int:pk>/user-detail', UserDetail.as_view(), name='user_detail'),
    path('login', LoginAPIView.as_view(), name='login'),
    path('signup', RegistrationAPIView.as_view(), name='signup'),
    path('facebook-login', FacebookLogin.as_view(), name='fb_login'),
    path('twitter-login', TwitterLogin.as_view(), name='twitter_login'), 
   
]