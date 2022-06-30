from django.contrib import admin

from .models import Myfirst

@admin.register(Myfirst)
class Myfirst(admin.ModelAdmin):
    pass

