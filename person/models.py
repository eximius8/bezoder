from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator
from trait.models import OneSNPTrait
from genetics.models import UserGenome

class User(AbstractUser):
    pass



class AbstractVisitor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birthday = models.DateField(blank=True)
    height = models.FloatField(blank=True, validators=[MinValueValidator(5.), MaxValueValidator(500)])

    class Meta:
        abstract = True


class GeneVisitor(AbstractVisitor):
    genome =  models.OneToOneField(UserGenome, on_delete=models.SET_NULL, blank=True, null=True)
    onensptrait = models.ManyToManyField(OneSNPTrait)



class Creator(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
