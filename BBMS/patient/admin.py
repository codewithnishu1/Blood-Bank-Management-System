from django.contrib import admin

from Bloodmanager.models import admini

# Register your models here.
@admin.register(admini)
class adminiAdmin(admin.ModelAdmin):
    list_display = ("name", "email")
