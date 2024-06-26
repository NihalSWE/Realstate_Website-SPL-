from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ContactSubmission, ContactImage,PropertyHeaderImage,Property

def home(request):
    # Your home view logic here
    return render(request, 'properties/home.html')

def about(request):
    # Your about view logic here
    return render(request, 'properties/about.html')

def property(request):
    properties = Property.objects.all()
    header_image = PropertyHeaderImage.objects.first()  # Assuming you have only one header image
    context = {
        'properties': properties,
        'header_image': header_image,
    }
    return render(request, 'properties/property-list.html', context)

def contact(request):
    latest_image = ContactImage.objects.last()  # Fetch the latest uploaded image

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        if name and email and subject and message:
            ContactSubmission.objects.create(name=name, email=email, subject=subject, message=message)
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('contact')  # Redirect to clear the form and show success message
        else:
            error_message = "All fields are required."
            return render(request, 'properties/contact.html', {'error_message': error_message, 'latest_image': latest_image})

    return render(request, 'properties/contact.html', {'latest_image': latest_image})
