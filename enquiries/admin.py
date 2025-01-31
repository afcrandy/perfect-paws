from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Enquiry


# Register your models here.
@admin.register(Enquiry)
class EnquiryAdmin(SummernoteModelAdmin):
    list_display = ('enquirer_name', 'enquirer_email', 'read', 'created_on')
    search_fields = ['enquirer_name', 'enquirer_email', 'content']
    list_filter = ('enquirer_email', 'read', 'created_on')
    summernote_fields = ('content', )
