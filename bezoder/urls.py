from django.conf.urls import url, include
from django.contrib import admin
import person.views as person_views
from django.contrib.auth import views as auth_views



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('', include('home.urls')),
    url('traits', include('trait.urls')),
    url('login', auth_views.LoginView.as_view(template_name='person/login.html'), name='login'),
    url('register', person_views.register, name='register'),
    url('logout', auth_views.LogoutView.as_view(template_name='person/logout.html'), name='logout'),
    url('profile', person_views.profile, name='profile'),
#    url('', include('home.urls')),
#    url('', include('home.urls')),
]

'''
1 Symbol
2 Slogan
3 Surprise
4 Salient
5 Story

'''
