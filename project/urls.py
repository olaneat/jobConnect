from django.urls import path
from .apiviews import (
	ProjectsListView, 
	ProjectDetailView,
	CreateProjectsView,
	DeleteProjectView)

app_name = 'projects'
urlpatterns = [
	path('create', CreateProjectsView.as_view(), name="create-project"),
	path('list', ProjectsListView.as_view(), name='projects-list'),
	path('<int:pk>/detail', ProjectDetailView.as_view(), name="detail"),
	path('<int:pk>/detail', DeleteProjectView.as_view(), name="detail"),

]