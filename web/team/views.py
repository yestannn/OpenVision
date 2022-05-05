from django.shortcuts import render, reverse, get_object_or_404, redirect
from django.views.generic import (
	ListView, DetailView,
	CreateView, UpdateView,
	DeleteView, FormView
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
from django.core.exceptions import PermissionDenied
from django.contrib import messages

from .models import Team, TeamMembers
from .forms import TeamCreateForm

# Create your views here.

class TeamCreateView(UpdateView, LoginRequiredMixin):
	model = Team
	template_name = 'team/team_create.html'
	form_class = TeamCreateForm

	def form_valid(self, form):
		form.instance.owner = self.request.user
		return super().form_valid(form)

	def get_success_url(self):
		return reverse('team-detail', kwargs={'pk': self.object.pk})

class TeamCreateView(CreateView, LoginRequiredMixin):
	model = Team
	template_name = 'team/team_create.html'
	form_class = TeamCreateForm

	def form_valid(self, form):
		form.instance.owner = self.request.user
		return super().form_valid(form)

	def get_success_url(self):
		team_members = TeamMembers(team=self.object)
		team_members.save()
		team_members.members_set.add(self.request.user)
		return reverse('team-detail', kwargs={'pk': self.object.pk})

class TeamDetailView(DetailView, UserPassesTestMixin, LoginRequiredMixin):
	model = Team
	template_name = 'team/team_detail.html'
	context_object_name = 'team'

	def dispatch(self, request, *args, **kwargs):
		team = self.get_object()
		if not TeamMembers.objects.filter(team=team, members_set=self.request.user).exists():
			messages.error(request, 'You are not able to see this team.')
			raise PermissionDenied
		return super().dispatch(request,*args,**kwargs)

def joinToTeam(request, invite_id=None):
	if Team.objects.filter(invite_id=invite_id).exists():
		team = get_object_or_404(Team, invite_id=invite_id)
		team.team_members.members_set.add(request.user)
		messages.error(request, 'You are joined to team')
		return redirect('team-detail', pk=team.pk)
	messages.error(request, 'Invalid link')
	return redirect('base', pk=team.pk)








