from rest_framework import serializers
from register.serializers import RegistrationSerializer
from .models import Bid, Project



class ProjectDetialSerializer(serializers.ModelSerializer):
	user = RegistrationSerializer(many=True, read_only=True)
	class Meta:
		models = Project
		fields = '__all__'

class BidSerializer(serializers.ModelSerializer):
	user =RegistrationSerializer(many=True, read_only=True)
	job = ProjectDetialSerializer(read_only=True, many=True)
	class Meta:
		model = Bid
		fields = ('user', 'job', 'bidDetail')


