from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from .forms import SignUpForm, EditProfileForm, PasswordChangingForm
from django.contrib import messages
from django.http import HttpResponseRedirect

class PasswordsChangeView(PasswordChangeView):
	#form_class = PasswordChangeForm
	form_class = PasswordChangingForm
	success_url = reverse_lazy('password_success')
	#success_url = reverse_lazy('home')	


def password_success(request):
	messages.success(request, ('Password was changed successfully.'))
	return render(request, 'registration/password_success.html', {})


class UserRegisterView(generic.CreateView):
	form_class = SignUpForm
	template_name = 'registration/register.html'
	success_url = reverse_lazy('login')


class UserEditView(generic.UpdateView):
	form_class = EditProfileForm
	template_name = 'registration/edit_profile.html'	
	success_url = reverse_lazy('home')
	
	def get_object(self):
		return self.request.user	

	def form_valid(self, form):
		messages.success(self.request, "Profile Updated!")
		super().form_valid(form)
		return HttpResponseRedirect(self.get_success_url())		
