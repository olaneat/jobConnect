from .models import Profile
from .constants import GENDER
from register.models import CustomUser
from rest_framework import serializers


class ProfileSerializer(serializers.ModelSerializer):
	id = serializers.IntegerField(source = 'pk', read_only = True)
	user = serializers.CharField(source='user.username', read_only=True)
	username = serializers.CharField(source = 'user.username', read_only = True)
	email = serializers.CharField(source = 'user.email', read_only=True)
    
	class Meta:
		model = Profile
		fields = ('id', 'email', 'username', 'yearOfExperience',
		 	'qualification', 'profession', 'phoneNumber',
      		'city', 'address', 'surname', 'firstName', 'dp', 
   			'gender', 'user'
		)

	def create(self, validated_data, instance=None):
		user = validated_data.pop('user')
		user = CustomUser.objects.create(**validated_data)
		profile, created_profile = Profile.objects.update_or_create(user=user, **validated_data)
		return profile

	def get_username(self, obj):
		return self.obj.username

	def get_email(self, obj):
		return self.obj,email

	'''def update(self, validated_data, instance):
					" instance of user profile from Profile.objects.get(user=user)"
					instance.gender = validated_data.get('gender', instance.gender)
					instance.yearOfExperience = validated_data.get('yearOfExperience', instance.yearOfExperience)
					instance.phoneNumber = validated_data.get('phoneNumber', instance.phoneNumber)
					instance.firstName = validated_data.get('firstName', instance.firstName)
					instance.surname = validated_data.get('surname', instance.surname)
					instance.profession = validated_data.get('profession', instance.profession)
					instance.qualification = validated_data.get('qualification', instance.qualification)
					instance.address = validated_data.get('address', instance.address)
					instance.city = validated_data.get('city', instance.city)
					instance.dp = validated_data.get('dp', instance.dp)
					instance.save()
					return instance'''

	def get_image(self, obj):
 		if obj.dp:
 			return self.dp
