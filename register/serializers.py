from rest_framework import serializers
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework_jwt.settings import api_settings
from register.models import CustomUser
from details.models import Profile
from project.serializers import BidSerializer,ProjectDetialSerializer
from details.serializers import ProfileSerializer 

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(write_only=True)
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)
    def validate(self, data):
        email = data.get('email', None)
        password = data.get('password', None)

        if email is None:
            raise serializers.ValidationError(
                'An email address is required to log in.'
            )

        if password is None:
            raise serializers.ValidationError(
                'A password is required to log in.'
            )

        user = authenticate(email=email, password=password)

        if user is None:
            raise serializers.ValidationError(
                'A user with this email and password was not found.'
            )

        if not user.is_active:
            raise serializers.ValidationError(
                'This user has been deactivated.'
            )

        return {
            'email':user.email,
            'token': user.token,
            'username': user.username
        }


class RegistrationSerializer(serializers.ModelSerializer):    
    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True,
    )

    token = serializers.CharField(max_length=255, read_only=True)
    bid = serializers.StringRelatedField(many=True, read_only=True)
    profile = ProfileSerializer(read_only=True)
    project = serializers.StringRelatedField(read_only=True, many=True)

    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'password', 'token', 'project', 'profile', 'bid')


    '''
        def create(self, validated_data):
                     return CustomUser.objects._create_user(**validated_data)'''


    '''def create(self, validated_data):
                        profile_data = validated_data.pop('profile')
                        user = CustomUser.objects.create(**validated_data)
                        userProfile = Profile.objects.create(**validated_data)
                        return user'''

    def create(self, **validated_data):
        user = CustomUser.objects._create_user(
        email = validated_data['email'],
        username = validated_data['username'],
                        #profile = validated_data['profile'],
                        #project = validated_data['project'],
                        #bid = validated_data['bid']
                                    
        )            
        profile_data = validated_data.pop('profile')
                          
        user_profile = Profile.objects.create(
            user = user,
            firstName = profile_data['firstName'],
            surname = profile_data['surname'],
            dp = profile_data['dp'],
            gender = profile_data['gender'],
            profession = profile_data['profession'],
            address = profile_data['address'],
            city = profile_data['city'],
            phoneNumber = profile_data['phoneNumber'],
            yearOfExperience = profile_data['yearOfExperience'],
            qualification = profile_data['qualification'],
        ) 
        return user
    
            
    
        
    

        
    

    '''def update(self, instance, validated_data):
                    profile_data = validated_data.pop('profile')
                    instance.firstName = validated_data.get('firstName', instance.firstName)
                    instance.surname = validated_data.get('surname', instance.surname)
                    
                    if not instance.profile:
                        Profile.objects.create(user=instance, **profile_data)
                    instance.profile.uid
                    instance.profile.yearOfExperience = validated_data.get('yearOfExperience', instance.yearOfExperience)
                    instance.profile.profession = validated_data.get('profession', instance.profession)
                    instance.profile.city = validated_data.get('city', instance.city)
                    instance.profile.address = validated_data.get('address', instance.address)
                    instance.profile.phoneNumber = validated_data.get('phoneNumber', instance.phoneNumber)
                    instance.profile.dp = validated_data.get('dp', instance.dp)
                    instance.profile.qualifcation = validated_data.get('qualifcation', instance.qualification)
                    instance.profile.gender = validated_data.gender('gender', instance.gender)
                    instance.save()'''