from django.contrib import admin
from .models import ContactSubmission, ContactImage,PropertyHeaderImage,Property

@admin.register(ContactSubmission)
class ContactSubmissionAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'submitted_at')
    search_fields = ('name', 'email', 'subject')
    list_filter = ('submitted_at',)

@admin.register(ContactImage)
class ContactImageAdmin(admin.ModelAdmin):
    list_display = ('image',)


@admin.register(PropertyHeaderImage)
class PropertyHeaderImageAdmin(admin.ModelAdmin):
    list_display = ('image',)

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('title', 'property_type', 'price', 'location', 'size_sqft', 'bedrooms', 'bathrooms')
    list_filter = ('property_type',)
    search_fields = ('title', 'location')
    ordering = ('-id',)