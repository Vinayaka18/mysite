from django.contrib import admin

# Register your models here.
# yourappname/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser,Try,HtmlVideo

admin.site.register(CustomUser, UserAdmin)
admin.site.register(Try)
admin.site.register(HtmlVideo)