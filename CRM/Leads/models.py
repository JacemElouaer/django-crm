from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    # abstract class is more flexible with  modification and adding
    pass


class Lead(models.Model):
    SOURCE_CHOICE = [
        ('Youtube', 'Youtube')
    ]
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    age = models.IntegerField(default=0)
    agent = models.ForeignKey("Agent", on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name + self.last_name


class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

