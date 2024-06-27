from django.db import models




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
    
class Property(models.Model):
    PROPERTY_TYPES = [
        ('sell', 'For Sell'),
        ('sold', 'Sold'),
    ]
    
    title = models.CharField(max_length=100)
    property_type = models.CharField(max_length=4, choices=PROPERTY_TYPES, default='sell')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=255)
    image = models.ImageField(upload_to='property_images/')
    size_sqft = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()

    def __str__(self):
        return self.title


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