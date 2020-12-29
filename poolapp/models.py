from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib import messages

class Week(models.Model):
	week = models.IntegerField()

	def __str__(self):
		return str(self.week) 

	def get_absolute_url(self):
		#return reverse('week_detail', args=(str(self.id)))		
		return reverse('home')


class Profile(models.Model):
	user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)	
	status = models.TextField(default="IN")
	
	def __str__(self):
		return str(self.user) + " | " + self.status	
	
	@receiver(post_save, sender=User)
	def create_profile(sender, instance, created, **kwargs):
		if created:
			Profile.objects.create(user=instance)

	@receiver(post_save, sender=User)
	def save_profile(sender, instance, **kwargs):
		instance.profile.save()	
	

class Team(models.Model):
	team = models.CharField(max_length=255)

	def __str__(self):
		return str(self.team) 

	def get_absolute_url(self):
		#return reverse('week_detail', args=(str(self.id)))		
		return reverse('home')		


class Pick(models.Model):
	week = models.IntegerField()
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	team = models.CharField(max_length=255)
	pick_date = models.DateField(auto_now_add=True)	

	def __str__(self):
		return str(self.week) + " | " + str(self.author) + " | " + self.team 
	
	def get_absolute_url(self):		
		return reverse('home')
		

class Winner(models.Model):
	week = models.IntegerField()
	team = models.CharField(max_length=255)
	
	def __str__(self):
		return str(self.week) + " | " + self.team 

	def get_absolute_url(self):
		#return reverse('week_detail', args=(str(self.id)))		
		return reverse('add_winners')		