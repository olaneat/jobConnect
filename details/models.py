from django.db import models
from register.models import CustomUser
from django.db.models.signals import post_save, pre_delete
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


'''@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance=None, created=False, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()'''

@receiver(pre_delete, sender=CustomUser)
def delete_user_profile(sender, instance=None, **kwargs):
	if instance:
		profile = Profile.objects.get(user=instance)
		profile.delete()