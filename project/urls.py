from django.urls import path
from .apiviews import ProjectsListView, ProjectDetailView

app_name = 'projects'
urlpatterns = [
	path('bids-list', ProjectsListView.as_view(), name="bid"),
	path('bid-detail/<int:pk>', ProjectDetailView.as_view(), name="detail"),
]