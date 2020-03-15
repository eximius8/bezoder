from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator
from trait.models import OneSNPTrait
from genetics.models import UserGenome

class User(AbstractUser):
    pass

class AbstractVisitor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
#    birthday = models.DateField(blank=True,null=True)
#    height = models.FloatField(blank=True, validators=[MinValueValidator(5.), MaxValueValidator(500)])

    class Meta:
        abstract = True

class GeneVisitor(AbstractVisitor):
    genome =  models.OneToOneField(UserGenome, on_delete=models.SET_NULL, blank=True, null=True, related_name='geneuser')
    onensptrait = models.ManyToManyField(OneSNPTrait, blank=True)

    def __str__(self):
        return self.user.get_username()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #bio = models.TextField(blank=True)
    #image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} profile'

class NewsAuthor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.get_fullname()

class Creator(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.user.get_username()
