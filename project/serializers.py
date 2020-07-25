from rest_framework import serializers
from .models import Bid, Project



class BidSerializer(serializers.ModelSerializer):
	class Meta:
		model = Bid
		fields = ('user', 'job', 'bidDetail')


class ProjectDetialSerializer(serializers.ModelSerializer):
	bid = BidSerializer(many=True, read_only=True)
	class Meta:
		model = Project
		fields = ('title', 'user', 'bid', 'description', 'jobLocation',  'skillRequired')

