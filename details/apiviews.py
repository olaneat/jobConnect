from .serializers import ProfileSerializer
from .models import Profile
from rest_framework import permissions
from rest_framework import generics

class ProfileListView(generics.ListCreateAPIView):
	model =  Profile
	serializer_class = ProfileSerializer
	permission_classes = (permissions.IsAuthenticated,)

class UpdateProfileView(generics.RetrieveUpdateAPIView):
	models  = Profile
	serializer_class = ProfileSerializer
	permission_classes = (permissions.IsAuthenticated,)