from rest_framework import generics
from .models import Project, Bid
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly
from .serializers import ProjectDetialSerializer, BidSerializer
from rest_framework import filters

class ProjectsListView(generics.ListCreateAPIView):
	permission_classes = (IsAuthenticatedOrReadOnly,)
	serializer_class = ProjectDetialSerializer
	queryset = Project.objects.all()

class ProjectDetailView(generics.RetrieveUpdateDestroyAPIView):
	permission_classes = (IsAuthenticatedOrReadOnly,)	
	serializer_class = ProjectDetialSerializer
	queryset = Project.objects.all()


class ProjectSearchSerializer(generics.ListCreateAPIView):
	permission_classes = (AllowAny,)
	search_fields = ['job_location', 'skill_required']
	filter_backends = (filters.SearchFilter,)
	serializer_class = ProjectDetialSerializer
	queryset = Project.objects.all()


class CreateBidApi(generics.ListCreateAPIView):
	permission_classes = [IsAuthenticatedOrReadOnly]
	serializer_class = BidSerializer
	queryset = Bid.objects.all()

