from .apiviews import ProfileListView, UpdateProfileView, ProfileDetailView
from django.urls import path

app_name = 'detail'
urlpatterns = [
	path('create', ProfileListView.as_view(), name='create-profile'),
	path('<int:id>/detail', ProfileDetailView.as_view(), 'profile-detail'),
	path('update/<str:username>', UpdateProfileView.as_view(), name='update-profile'), 

]