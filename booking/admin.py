from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Service, Booking


# Register your models here.
@admin.register(Service)
class ServiceAdmin(SummernoteModelAdmin):
    list_display = ('name', 'active', 'created_on')
    search_fields = ['name', 'description']
    list_filter = ('active', 'created_on')
    summernote_fields = ('description', )


@admin.register(Booking)
class BookingAdmin(SummernoteModelAdmin):
    list_display = ("client", 'dog_name', 'service', 'date', 'time', 'canceled')
    search_fields = ['client', 'service', 'date', 'dog_name']
    list_filter = ['service', 'date', 'time', 'canceled', 'created_on', 'client']
    summernote_fields = ('additional_notes', )
