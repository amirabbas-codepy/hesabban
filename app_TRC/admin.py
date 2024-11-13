from django.contrib import admin
from app_TRC.models import Trancion
@admin.register(Trancion)
class Trancionadmin(admin.ModelAdmin):
    list_display = ['descripition', 'user_TRC']

# admin.site.register(Trancion, Trancionadmin)
