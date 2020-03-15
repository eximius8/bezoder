from django.urls import path

from .views import mydna

app_name = 'genetics'

urlpatterns = [
    path('', mydna, name='mydna'),    
]
