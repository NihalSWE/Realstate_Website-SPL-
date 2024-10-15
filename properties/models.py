from django.db import models
from django.utils import timezone




class Home_Header(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.TextField()
    carousel_images = models.ManyToManyField('Home_HeaderImage')

    def __str__(self):
        return self.title

class Home_HeaderImage(models.Model):
    image = models.ImageField(upload_to='header_images')

    def __str__(self):
        return f"Home_HeaderImage {self.id}"

class Home_CallToAction(models.Model):
    image = models.ImageField(upload_to='cta_images')
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    

    def __str__(self):
        return self.title

class Home_Testimonial(models.Model):
    text = models.TextField(max_length=200)
    author_name = models.CharField(max_length=255)
    author_designation = models.CharField(max_length=255)
    author_image = models.ImageField(upload_to='testimonial_images')

    def __str__(self):
        return self.author_name





class ContactSubmission(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"
    

class ContactImage(models.Model):
    image = models.ImageField(upload_to='contact_images/')

    def __str__(self):
        return f"ContactImage {self.id}"


class PropertyHeaderImage(models.Model):
    image = models.ImageField(upload_to='header_images/', null=True, blank=True)


    def __str__(self):
        return f"HeaderImage {self.id}"
    

from PIL import Image
from django.core.files import File
from io import BytesIO
from django.core.files.base import ContentFile

class Property(models.Model):
    CATEGORY_CHOICES = (
        ('P', 'Primary Project'),
        ('S', 'Secondary Project'),
        ('L', 'Land Shearing'),
        ('J', 'Joint Venture'),
    )

    PROPERTY_TYPES = [
        ('sell', 'For Sell'),
        ('sold', 'Sold'),
        ('upcoming', 'Upcoming'),
        ('completed', 'Completed'),
        ('ongoing', 'OnGoing'),
    ]

    title = models.CharField(max_length=100)
    category = models.CharField(choices=CATEGORY_CHOICES, default='J', max_length=2)
    property_type = models.CharField(max_length=10, choices=PROPERTY_TYPES, default='sell')
    location = models.CharField(max_length=255)
    image = models.ImageField(upload_to='property_images/', default="No Image Set")
    size_sqft = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    belcony = models.IntegerField(default=0)
    drawingroom = models.IntegerField(default=0)
    dyningroom = models.IntegerField(default=0)
    kitchen = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Save the object first to generate an image path

        if self.image:
            img = Image.open(self.image)

            # Define the square size
            square_size = 600  # Example size, adjust as needed

            # Resize the image to the square size
            img = img.resize((square_size, square_size), Image.LANCZOS)

            # Save the resized image back to the image field
            img_io = BytesIO()
            img.save(img_io, format='JPEG', quality=90)
            img_content = ContentFile(img_io.getvalue(), self.image.name)
            self.image.save(self.image.name, img_content, save=False)

        super().save(*args, **kwargs)  # Save the object again with the resized image




class PropertyImage(models.Model):
    property = models.ForeignKey(Property, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='property_images/')

    def __str__(self):
        return f"{self.property.title} Image"

class PropertyAgent_HeaderImage(models.Model):
    image = models.ImageField(upload_to='header_images', null=True, blank=True)

    def __str__(self):
        return f"P_A_HeaderImage {self.id}"

class PropertyAgent_TeamMember(models.Model):
    full_name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    number=models.CharField(max_length=20,null=True)
    image = models.ImageField(upload_to='team_images')
    facebook_url = models.URLField(blank=True, null=True)
    twitter_url = models.URLField(blank=True, null=True)
    instagram_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.full_name

class PropertyAgent_CallToAction(models.Model):
    image = models.ImageField(upload_to='cta_images')
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title
    


class AboutUs_HeaderImage(models.Model):
    image = models.ImageField(upload_to='header_images')

    def __str__(self):
         return f"AboutUs_HeaderImage {self.id}"

class AboutUs_CallToAction(models.Model):
    image = models.ImageField(upload_to='cta_images')
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title

class AboutUs_TeamMember(models.Model):
    name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    number = models.CharField(max_length=20, blank=True, null=True)
    image = models.ImageField(upload_to='team_images')
    facebook_url = models.URLField(blank=True, null=True)
    twitter_url = models.URLField(blank=True, null=True)
    instagram_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name



class Career_Department(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class CareerApplication(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=50)
    number = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    message = models.TextField()
    cv = models.FileField(upload_to='cvs/')
    department = models.ForeignKey(Career_Department, on_delete=models.SET_NULL, null=True, blank=True)
    submitted_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
    
class Career_HeaderImage(models.Model):
    image = models.ImageField(upload_to='header_images/')

    def __str__(self):
        return f"Career_HeaderImage {self.id}"
    



class Portfolio(models.Model):
    file = models.FileField(upload_to='portfolios/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Portfolio uploaded on {self.id}"