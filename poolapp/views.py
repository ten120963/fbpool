from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Pick, Week, Team, Winner, User
from .forms import PickForm, EditForm, WinnerForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

'''
def home(request):
	return render(request, 'home.html', {})
'''


class HomeView(ListView):
	model = User
	template_name = 'home.html'
	ordering = ['profile__status', 'first_name']
		   
	def get_context_data(self, *args, **kwargs):
		week_menu = Week.objects.all()
		context = super(HomeView, self).get_context_data(*args, **kwargs)
		context["week_menu"] = week_menu
		return context	

		
class StatusView(ListView):
	model = User
	template_name = 'status.html'
	ordering = ['profile__status', 'first_name']


class WinnerListView(ListView):
	model = Winner
	template_name = 'winner_list.html'
	ordering = ['week']


class WinnerView(SuccessMessageMixin, CreateView):
	model = Winner
	form_class = WinnerForm
	template_name = 'winner.html'	
	
	def get_success_message(self, cleaned_data):		
		#return "Winner has been added"	
		team = cleaned_data['team']
		week = cleaned_data['week']
		msg = team + ' has been added as a winner for Week ' + str(week)		
		messages.add_message(self.request, messages.INFO, msg)	

	
def WeekView(request, week):
	week_posts = Pick.objects.order_by('team').filter(week=week)
	if not week_posts:		
		messages.success(request, ('There are no picks entered for this week.'))
		return redirect('home')
	else:
		return render(request, 'weeks.html', {'week': week, 'week_posts': week_posts})		
	

'''
def WeekListView(request):
	week_menu_list = Week.objects.all()
	return render(request, 'week_list.html', {'week_menu_list': week_menu_list})		
'''


def TeamView(request, team):
	team_posts = Pick.objects.order_by('week').filter(team=team.title().replace('-', ' '))
	return render(request, 'teams.html', {'team': team.title().replace('-', ' '), 'team_posts': team_posts})


def AuthorView(request, author):		
	author_posts = Pick.objects.order_by('week').filter(author__username=author)
	return render(request, 'player.html', {'author': author, 'author_posts': author_posts})					


'''
def TeamListView(request):
	team_menu_list = Team.objects.order_by('team')
	return render(request, 'team_list.html', {'team_menu_list': team_menu_list})		
'''


class AddPickView(SuccessMessageMixin, CreateView):
	model = Pick
	form_class = PickForm
	template_name = 'add_pick.html'
	#fields = '__all__'
	#fields = ('week', 'author')	

	'''
	def get_context_data(self, *args, **kwargs):
		week_menu = Week.objects.all()
		context = super(AddPickView, self).get_context_data(*args, **kwargs)
		context["week_menu"] = week_menu
		return context	
	'''

	def get_success_message(self, cleaned_data):
		team = cleaned_data['team']
		week = cleaned_data['week']
		msg = team + ' has been added for Week ' + str(week)	
		messages.add_message(self.request, messages.INFO, msg)
    

class UpdatePickView(SuccessMessageMixin, UpdateView):
	model = Pick
	form_class = EditForm
	template_name = 'update_pick.html'
	#fields = ['week', 'author', 'team']

	'''   
	def get_context_data(self, *args, **kwargs):
		week_menu = Week.objects.all()
		context = super(UpdatePickView, self).get_context_data(*args, **kwargs)
		context["week_menu"] = week_menu
		return context	
	'''
	
	def get_success_message(self, cleaned_data):
		team = cleaned_data['team']
		week = cleaned_data['week']
		msg = 'Pick has been updated to ' + team + ' for Week ' + str(week)	
		messages.add_message(self.request, messages.INFO, msg)
	

class DeletePickView(DeleteView):
	model = Pick	
	template_name = 'delete_pick.html'	
	success_url = reverse_lazy('home')		
	success_message = "Week %(week)s Team %(team)s was removed successfully"

	'''
	def get_context_data(self, *args, **kwargs):
		week_menu = Week.objects.all()
		context = super(DeletePickView, self).get_context_data(*args, **kwargs)
		context["week_menu"] = week_menu
		return context	
	'''
		
	def delete(self, request, *args, **kwargs):
		obj = self.get_object()
		messages.success(self.request, self.success_message % obj.__dict__)
		return super(DeletePickView, self).delete(request, *args, **kwargs)


def CalculateView(request):
	if request.method == "POST":

		calc_week = request.POST['week']

		all_picks = Pick.objects.filter(week=calc_week)
		all_winners = Winner.objects.filter(week=calc_week)
		
		#picks_list = []
		#player_list = []
		#winner_list = []
		#status_list = []

		for item in all_picks:
			#picks_list.append(item.team)			
			#player_list.append(item.author)

			for winner in all_winners:
				#winner_list.append(winner.team)	

				if item.team == winner.team:
					week_status = 'GOOD'					
					break
				else:
					week_status = 'BAD'				
			
			user = User.objects.get(username=item.author)
			user_status = user.profile.status

			if user_status == 'IN' and week_status == 'GOOD':
				status = 'IN'	
			elif user_status == 'IN' and week_status == 'BAD':	
				status = 'LOSS'	
			elif user_status == 'LOSS' and week_status == 'GOOD':	
				status = 'LOSS'		
			elif user_status == 'LOSS' and week_status == 'BAD':	
				status = 'OUT'				
			else:
				status = 'OUT'	
				
			#status_list.append(status)		
			user.profile.status = status
			user.save()			
		'''	
		return render(request, 'list_stats.html', {'picks_list': picks_list, 
			'player_list': player_list,
			'winner_list': winner_list,
			'status_list': status_list,
			})	
		'''
		#status_msg = 'Stats have been generated'
		messages.success(request, ('Stats have been generated.'))

		#return render(request, 'list_stats.html', {'status_msg': status_msg})
		return render(request, 'list_stats.html', {})	

	else:
		return render(request, 'calculate.html', {})


def WinnerWeekView(request):
	if request.method == "POST":		
		winner_week = request.POST['week']
		all_winners = Winner.objects.filter(week=winner_week)
		if not all_winners:		
			messages.success(request, ('There are no winners entered for Week ' + str(winner_week)))
			return redirect('winner_week')
		else:			
			return render(request, 'winner_week.html', {'all_winners': all_winners})	
	else:		
		return render(request, 'winner_list.html', {})		
