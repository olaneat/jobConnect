from .serializers import ProfileSerializer
from .models import Profile
from rest_framework import permissions
from rest_framework import generics
from .exceptions import ProfileDoesNotExit
from rest_framework.response import Response

class ProfileListView(generics.ListCreateAPIView):
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
	queryset =  Profile.objects.all()
	serializer_class = ProfileSerializer

class UpdateProfileView(generics.RetrieveAPIView):
	permission_classes = (permissions.IsAuthenticated,)
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