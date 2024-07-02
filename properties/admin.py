from django.contrib import admin
from .models import ContactSubmission, ContactImage,PropertyHeaderImage,Property,PropertyAgent_HeaderImage, PropertyAgent_TeamMember, PropertyAgent_CallToAction,AboutUs_HeaderImage, AboutUs_CallToAction, AboutUs_TeamMember,Home_Header, Home_HeaderImage, Home_CallToAction, Home_Testimonial,CareerApplication,Career_HeaderImage





class Home_HeaderImageInline(admin.TabularInline):
    model = Home_Header.carousel_images.through
    extra = 1

@admin.register(Home_Header)
class Home_HeaderAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle')
    search_fields = ('title', 'subtitle')
    inlines = [Home_HeaderImageInline]

@admin.register(Home_HeaderImage)
class Home_HeaderImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'image')
    search_fields = ('id',)

@admin.register(Home_CallToAction)
class Home_CallToActionAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image')
    search_fields = ('title', 'description')

@admin.register(Home_Testimonial)
class Home_TestimonialAdmin(admin.ModelAdmin):
    list_display = ('author_name', 'author_designation', 'text')
    search_fields = ('author_name', 'author_designation', 'text')








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




@admin.register(Career_HeaderImage)
class Career_HeaderImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'image')
    search_fields = ('id',)

@admin.register(CareerApplication)
class CareerApplicationAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'number', 'address', 'message','cv','submitted_at',)
    search_fields = ('name', 'number', 'address',)