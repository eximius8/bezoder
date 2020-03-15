from django import forms
from django.contrib.auth import get_user_model
from person.models import GeneVisitor
from .models import UserGenome


class MyDNAUpdateForm(forms.ModelForm):

    class Meta:
        model = UserGenome
        fields = ['genomefile', 'opensnpid']
