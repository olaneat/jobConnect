from .apiviews import ProfileListView, UpdateProfileView
from django.urls import path

app_name = 'detail'
urlpatterns = [
	path('create', ProfileListView.as_view(), name='create-profile'),
	path('update/<str:username>', UpdateProfileView.as_view(), name='update-profile'), 

]