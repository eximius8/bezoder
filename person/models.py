from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator

class User(AbstractUser):
    pass


class Visitor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birthday = models.DateField(blank=True)
    # in cm
    height = models.FloatField(blank=True, validators=[MinValueValidator(5.), MaxValueValidator(500)])
    opensnpid = models.PositiveIntegerField(blank=True)
    sex = models.

class Creator(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
