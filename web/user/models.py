from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
	location = models.CharField(max_length=64, blank=True)
	status = models.CharField(max_length=16, blank=True)
	AVATAR = (
        (1, 1), (2, 2),
        (3, 3), (4, 4),
        (5, 5), (6, 6),
        (7, 7), (8, 8),
    )

	avatar = models.PositiveSmallIntegerField(choices=AVATAR, default=1)