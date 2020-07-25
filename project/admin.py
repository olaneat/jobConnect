from django.contrib import admin
from .models import Project, Bid
# Register your models here.

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
	fields = ['title']
	search_fields = ['title', 'jobLocation']


@admin.register(Bid)
class BidAdmin(admin.ModelAdmin):
	fields = ['projects']
	search_fields = ['bidDetail']