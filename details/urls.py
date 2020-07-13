from .apiviews import ProfileListView
from django.urls import path

app_name = 'detail'
urlpatterns = [
	path('create', ProfileListView.as_view(), name='create-profile'),

]