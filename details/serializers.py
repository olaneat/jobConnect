from .models import Profile
from .constants import GENDER
from rest_framework import serializers
from register.serializers import RegistrationSerializer

class ProfileSerializer(serializers.ModelSerializer):
	user = RegistrationSerializer(read_only=True)
	gender = serializers.ChoiceField(choices = GENDER)
	class Meta:
		model = Profile
		fields = '__all__'

