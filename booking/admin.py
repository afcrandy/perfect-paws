from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Service


# Register your models here.
@admin.register(Service)
class ServiceAdmin(SummernoteModelAdmin):
    list_display = ('name', 'active', 'created_on')
    search_fields = ['name', 'description']
    list_filter = ('active', 'created_on')
    summernote_fields = ('description', )
