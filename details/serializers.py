from .models import Profile
from rest_framework import serializers
from register.serializers import RegistrationSerializer

class ProfileSerializer(serializers.ModelSerializer):
	user = RegistrationSerializer()
	class Meta:
		models = Profile
		exclude = ('__all__',)

