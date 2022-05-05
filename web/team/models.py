from django.db import models
from django.contrib.auth.models import User

import uuid

class TeamManager(models.Manager):
	pass 

class Team(models.Model):
	team_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	invite_id = models.UUIDField(default=uuid.uuid4)

	name = models.CharField(max_length=255, null=True, blank=True)
	owner = models.ForeignKey(User, on_delete=models.CASCADE)

	about = models.TextField(null=True, blank=True)

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	contact_email = models.EmailField(null=True, blank=True)

	objects = TeamManager()

	class Meta:
		db_table = 'team'
		verbose_name = 'Team'
		verbose_name_plural = 'Team'

