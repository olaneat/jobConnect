from django.contrib import admin
from .models import Profile
# Register your models here.

@admin.register(Profile)
class ProfileAdminModel(admin.ModelAdmin):
	fields = ['user', 'firstName' ]
	search_fields = ['surname']