from django.contrib import admin
from .models import *
# # Register your models here.
# admin.site.register(Admin)

@admin.register(Admin)
class AdminAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'password','gender']