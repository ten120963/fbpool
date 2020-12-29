from django import forms
from .models import Pick, Week, Team, Winner
from django.core.exceptions import ValidationError

#choices = [('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')]
choices = Week.objects.all().values_list('week', 'week')
choice_list = []

choices_teams = Team.objects.all().values_list('team', 'team')
choice_teams_list = []

for item in choices:
	choice_list.append(item)

for item_team in choices_teams:
	choice_teams_list.append(item_team)

choice_teams_list.sort()

class PickForm(forms.ModelForm):
	class Meta:
		model = Pick
		fields = ('week', 'author', 'team')

		widgets = {
			'week': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
			'author': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'user_box', 'type':'hidden'}),
			#'author': forms.Select (attrs={'class': 'form-control'}),
			'team': forms.Select(choices=choice_teams_list, attrs={'class': 'form-control'}),
		}

	def clean_team(self):
		team = self.cleaned_data.get('team')
		author = self.cleaned_data.get('author')

		if (team == ""):
			raise forms.ValidationError('Team name can not be left blank.')
		
		for instance in Pick.objects.all():
			if instance.author == author and instance.team == team:
				raise forms.ValidationError('You have already used that team!')
			
		return team				

class WinnerForm(forms.ModelForm):
	class Meta:
		model = Winner
		fields = ('week', 'team')

		widgets = {
			'week': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
			'team': forms.Select(choices=choice_teams_list, attrs={'class': 'form-control'}),
		}

	def clean_team(self):
		week = self.cleaned_data.get('week')
		team = self.cleaned_data.get('team')

		'''
		if (team == "Arizona"):
			raise forms.ValidationError('Team name can not be left blank.')
		'''

		for instance in Winner.objects.all():
			if instance.week == week and instance.team == team:
				raise forms.ValidationError('You have already used that team!')
			
		return team					

class EditForm(forms.ModelForm):
	class Meta:
		model = Pick
		fields = ('week', 'author', 'team')

		widgets = {
			'week': forms.Select (choices=choice_list, attrs={'class': 'form-control'}),
			'author': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'user_box', 'type':'hidden'}),
			#'author': forms.Select (attrs={'class': 'form-control'}),
			'team': forms.Select(choices=choice_teams_list, attrs={'class': 'form-control'}),
		}	
	
	def clean_team(self):
		team = self.cleaned_data.get('team')
		author = self.cleaned_data.get('author')
		
		for instance in Pick.objects.all():
			if instance.author	== author and instance.team == team:
				raise forms.ValidationError('You have already used that team!')	
	
		return team				