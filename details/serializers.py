from .models import Profile
from .constants import GENDER
from rest_framework import serializers


class ProfileSerializer(serializers.ModelSerializer):
	username = serializers.CharField(source='user.username', read_only=True)
	email = serializers.EmailField(source='user.email', read_only=True)
	gender = serializers.ChoiceField(choices = GENDER)
	
	class Meta:
		model = Profile
		fields = (
			'username', 'surname', 'firstName', 'yearOfExperience', 
			'profession', 'qualification', 'phoneNumber', 
			 'city', 'address','dp', 'gender', 'email'
		 )

	def get_image(self, obj):
		if obj.dp:
			return self.dp

