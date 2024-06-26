from django.db import models

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
