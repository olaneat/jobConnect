from rest_framework import generics
from .models import Project, Bid
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import ProjectDetialSerializer, BidSerializer
from rest_framework import filters

class ProjectsListView(generics.ListCreateAPIView):
	serializer_class = ProjectDetialSerializer
	queryset = Project.objects.all()
	#permission_classes = (IsAuthenticated,)

class ProjectDetailView(generics.RetrieveDestroyAPIView):
	serializer_class = ProjectDetialSerializer
	queryset = Project.objects.all()
	#permission_classes = (IsAuthenticated)


class ProjectSearchSerializer(generics.ListCreateAPIView):
	search_fields = ['job_location', 'skill_required']
	filter_backends = (filters.SearchFilter,)
	serializer_class = ProjectDetialSerializer
	permission_classes = (AllowAny,)
	queryset = Project.objects.all()

