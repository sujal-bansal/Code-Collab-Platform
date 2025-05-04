from django.contrib import admin
from .models import Group,UserProfile, Code

admin.site.register(Group)
admin.site.register(Code)
admin.site.register(UserProfile)