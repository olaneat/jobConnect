from .serializers import ProfileSerializer
from .models import Profile
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework import generics
from .exceptions import ProfileDoesNotExit
from rest_framework.response import Response

class ProfileListView(generics.ListCreateAPIView):
	permission_classes = (IsAuthenticatedOrReadOnly,)
	queryset =  Profile.objects.all()
	serializer_class = ProfileSerializer

	def perform_create(self, serializer):
		serializer.save(user=self.request.user)

class UpdateProfileView(generics.RetrieveUpdateDestroyAPIView):
	permission_classes = (IsAuthenticated,)
	queryset  = Profile.objects.all()
	#serializer_class = ProfileSerializer

	def retrieve(self, username, request, *args, **kwargs):
		try:
			profile = Profile.objects.select_related('user').get(
				user__username =username
			)
		except Profile.DoesNotExist:
			raise valueError('User profile does not exist')
		
		serializer = self.serializer_class(Profile)

		return Response(serializer.data, status=status.HTTP_200_Ok)


class ProfileDetailView(generics.RetrieveUpdateDestroyAPIView):
	permission_classes = [IsAuthenticatedOrReadOnly]
	queryset = Profile.objects.all()
	serializer_class = ProfileSerializer 	