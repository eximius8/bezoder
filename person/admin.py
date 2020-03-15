from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, GeneVisitor, Creator, Profile

admin.site.register(User, UserAdmin)
admin.site.register(GeneVisitor)
admin.site.register(Creator)
admin.site.register(Profile)
