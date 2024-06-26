from django.contrib import admin
from .models import ContactSubmission, ContactImage

@admin.register(ContactSubmission)
class ContactSubmissionAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'submitted_at')
    search_fields = ('name', 'email', 'subject')
    list_filter = ('submitted_at',)

@admin.register(ContactImage)
class ContactImageAdmin(admin.ModelAdmin):
    list_display = ('image',)
