from django.contrib import admin
from .models import ContactSubmission, ContactImage,PropertyHeaderImage,Property,PropertyAgent_HeaderImage, PropertyAgent_TeamMember, PropertyAgent_CallToAction,AboutUs_HeaderImage, AboutUs_CallToAction, AboutUs_TeamMember





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
    list_display = ('id','image',)
@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('title', 'property_type', 'price', 'location', 'size_sqft', 'bedrooms', 'bathrooms')
    list_filter = ('property_type',)
    search_fields = ('title', 'location')
    ordering = ('-id',)





@admin.register(PropertyAgent_HeaderImage)
class PropertyAgent_HeaderImageAdmin(admin.ModelAdmin):
    list_display = ('id','image')
@admin.register(PropertyAgent_TeamMember)
class PropertyAgent_TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'designation', 'number','image')
@admin.register(PropertyAgent_CallToAction)
class PropertyAgent_CallToActionAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'description')







@admin.register(AboutUs_HeaderImage)
class AboutUs_HeaderImageAdmin(admin.ModelAdmin):
    list_display = ('id','image')
@admin.register(AboutUs_CallToAction)
class AboutUs_CallToActionAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image')
@admin.register(AboutUs_TeamMember)
class AboutUs_TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'designation', 'number', 'image')