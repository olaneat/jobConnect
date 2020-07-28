from django.db import models
from register.models import CustomUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from .constants import GENDER
# Create your models here.

class Profile(models.Model):
	user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
	firstName = models.CharField(max_length=255, blank=True, null=True)
	surname = models.CharField(max_length=255, blank=True, null=True)
	yearOfExperience = models.PositiveIntegerField(default=1)
	profession = models.CharField(max_length=250, blank=True, null=True)
	dp = models.URLField(blank=True, null=True)
	qualification = models.CharField(max_length=255, blank=True, null=True)
	phoneNumber = models.CharField(max_length=255, blank=True, null=True)
	city = models.CharField(max_length=255, blank=True, null=True)
	address = models.CharField(max_length=255, blank=True, null=True)
	gender = models.CharField(max_length=255, choices=GENDER)
	
	class Meta:
		ordering = ('surname', '-firstName', )
		verbose_name = 'Profile'
		verbose_name_plural = 'Profiles'


	def __str__(self):
		return self.user.username


@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()