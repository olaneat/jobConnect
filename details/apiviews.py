from .serializers import ProfileSerializer
from .models import Profile
from rest_framework import permissions
from rest_framework import generics
from .exceptions import ProfileDoesNotExit
from rest_framework.response import Response

class ProfileListView(generics.ListCreateAPIView):
	queryset =  Profile.objects.all()
	serializer_class = ProfileSerializer
	#permission_classes = (permissions.IsAuthenticated,)

class UpdateProfileView(generics.RetrieveAPIView):
	queryset  = Profile.objects.all()
	#serializer_class = ProfileSerializer
#	permission_classes = (permissions.IsAuthenticated,)

	def retrieve(self, username, request, *args, **kwargs):
		try:
			profile = Profile.objects.select_related('user').get(
				user__username =username
			)
		except Profile.DoesNotExist:
			raise valueError('User profile does not exist')
		
		serializer = self.serializer_class(Profile)

		return Response(serializer.data, status=status.HTTP_200_Ok)