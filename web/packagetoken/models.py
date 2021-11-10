from django.db import models
from django.contrib.auth.models import User

import uuid

# Create your models here.
class PackageToken(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	token = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, verbose_name="ID")
	due_date = models.DateTimeField(null=True, blank=True)

	class Meta:
		db_table = 'packagetokens'
		verbose_name = 'Package Tokens'
		verbose_name_plural = 'Package Tokens'
