import django
from django import forms
from .views import Team, TeamMembers

class TeamCreateForm(forms.ModelForm):

	name = forms.CharField(required=True)
	about = forms.CharField(required=True, widget=forms.Textarea)

	class Meta:
		model = Team
		fields = [ 'name','about', 'contact_email' ]
