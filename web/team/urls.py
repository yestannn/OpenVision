from django.urls import path
from .views import TeamDetailView, TeamCreateView, joinToTeam

urlpatterns = [
	path('<uuid:pk>', TeamDetailView.as_view(), name='team-detail'),
	path('create', TeamCreateView.as_view(), name='team-create'),
	path('join/<uuid:invite_id>', joinToTeam, name='team-join')
]