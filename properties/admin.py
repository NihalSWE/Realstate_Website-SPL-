from django.contrib import admin
from .models import ContactSubmission, ContactImage,PropertyHeaderImage,Property,PropertyAgent_HeaderImage, PropertyAgent_TeamMember, PropertyAgent_CallToAction,AboutUs_HeaderImage, AboutUs_CallToAction, AboutUs_TeamMember,Home_Header, Home_HeaderImage, Home_CallToAction, Home_Testimonial,CareerApplication,Career_HeaderImage,PropertyImage,Career_Department,Portfolio





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
    list_display = ('title','category' ,'property_type', 'location', 'size_sqft', 'bedrooms', 'bathrooms','belcony','drawingroom','dyningroom','kitchen',)
    list_filter = ('property_type','category')
    search_fields = ('title', 'location')
    ordering = ('-id',)

    # Adding the PropertyImage as an inline
    class PropertyImageInline(admin.TabularInline):
        model = PropertyImage
        extra = 1  # Number of empty forms to display

    inlines = [PropertyImageInline]




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


@admin.register(Career_Department)
class Career_DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
@admin.register(CareerApplication)
class CareerApplicationAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'number', 'address', 'message','department','cv','submitted_at',)
    search_fields = ('name', 'number', 'address','department',)

    def download_cv(self, obj):
        return f'<a href="{obj.cv.url}" download>Download CV</a>'
    download_cv.allow_tags = True
    download_cv.short_description = 'CV'



@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ['id','file','uploaded_at']