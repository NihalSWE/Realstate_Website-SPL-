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