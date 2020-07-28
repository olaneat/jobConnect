from django.urls import path
from .apiviews import ProjectsListView, ProjectDetailView

app_name = 'projects'
urlpatterns = [
	path('create', ProjectsListView.as_view(), name="bid"),
	path('<int:pk>/detail', ProjectDetailView.as_view(), name="detail"),
]