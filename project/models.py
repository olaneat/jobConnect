from django.db import models
from register.models import CustomUser

# Create your models here.

class Project(models.Model):
	title = models.CharField(max_length=255, blank=True, null=True)
	user = models.ForeignKey(CustomUser, related_name="project", on_delete=models.CASCADE)
	description = models.TextField(blank=True, null=True, )
	budget = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
	jobLocation = models.CharField(max_length=255, blank=True, null=True)
	bidDeadline = models.DateField(blank=True, null=True)
	skillRequired = models.TextField()
	created = models.DateField(auto_now=True)

	class Meta:
		verbose_name = 'Project Detail'
		verbose_name_plural = 'Project Details'

	def __str__(self):
		return self.title

class Bid(models.Model):
	user = models.ForeignKey(CustomUser, related_name="bid", on_delete=models.CASCADE)
	projects = models.ForeignKey(Project, related_name="bid", on_delete=models.CASCADE)
	bidDetail = models.TextField()
	created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.user.username

	class Meta:
		ordering = ('-user',)
		verbose_name = "Bid"
		verbose_name_plural = "Bids"