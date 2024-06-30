from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ContactSubmission, ContactImage,PropertyHeaderImage,Property,PropertyAgent_HeaderImage, PropertyAgent_TeamMember, PropertyAgent_CallToAction,AboutUs_HeaderImage, AboutUs_CallToAction, AboutUs_TeamMember,Home_Header, Home_HeaderImage, Home_CallToAction, Home_Testimonial


def home(request):
    header = Home_Header.objects.first()
    header_images = Home_HeaderImage.objects.all()
    properties = Property.objects.all()
    call_to_action = Home_CallToAction.objects.first()
    testimonials = Home_Testimonial.objects.all()

    for_sell_properties = properties.filter(property_type='sell')[:6]
    additional_sell_properties = properties.filter(property_type='sell')[6:]
    sold_properties = properties.filter(property_type='sold')[:6]

    context = {
        'header': header,
        'header_images': header_images,
        'for_sell_properties': for_sell_properties,
        'additional_sell_properties': additional_sell_properties,
        'sold_properties': sold_properties,
        'call_to_action': call_to_action,
        'testimonials': testimonials,
    }
    return render(request, 'properties/home.html', context)








def about(request):
    header_image = AboutUs_HeaderImage.objects.first()
    cta = AboutUs_CallToAction.objects.first()
    team_members = AboutUs_TeamMember.objects.all()

    context = {
        'header_image': header_image,
        'cta': cta,
        'team_members': team_members,
    }
    return render(request, 'properties/about.html',context)

def property(request):
    properties = Property.objects.all()
    header_image = PropertyHeaderImage.objects.first()  # Assuming you have only one header image
    for_sell_properties = properties.filter(property_type='sell')[:6]
    additional_sell_properties = properties.filter(property_type='sell')[6:]
    sold_properties = properties.filter(property_type='sold')[:6]
    context = {
        'properties': properties,
        'header_image': header_image,
        'for_sell_properties': for_sell_properties,
        'additional_sell_properties': additional_sell_properties,
        'sold_properties': sold_properties,
    }
    return render(request, 'properties/property-list.html', context)

from django.shortcuts import render, get_object_or_404
def property_detail(request, pk):
    property = get_object_or_404(Property, pk=pk)
    context = {
        'property': property
    }
    return render(request, 'properties/property_detail.html', context)


# # for seracarh-bar
# -------------------

# def property_list(request):
#     properties = Property.objects.all()
    
#     keyword = request.GET.get('keyword', '').strip()
#     property_type = request.GET.get('property_type', '').strip()
#     location = request.GET.get('location', '').strip()
    
#     print(f"Initial QuerySet: {properties}")  # Debug: Initial QuerySet

#     if keyword:
#         properties = properties.filter(title__icontains=keyword)
#         print(f"Filtered by keyword '{keyword}': {properties}")  # Debug: After keyword filter
    
#     if property_type:
#         properties = properties.filter(property_type=property_type)
#         print(f"Filtered by property_type '{property_type}': {properties}")  # Debug: After property_type filter
    
#     if location:
#         properties = properties.filter(location__icontains=location)
#         print(f"Filtered by location '{location}': {properties}")  # Debug: After location filter
    
#     context = {
#         'properties': properties,
#         'keyword': keyword,
#         'property_type': property_type,
#         'location': location,
#     }
#     print(f"Context: {context}")  # Debug: Final context before rendering
#     return render(request, 'properties/property-list.html', context)

def propertyAgent(request):
    header_image = PropertyAgent_HeaderImage.objects.first()
    team_members = PropertyAgent_TeamMember.objects.all()
    cta = PropertyAgent_CallToAction.objects.first()

    context = {
        'header_image': header_image,
        'team_members': team_members,
        'cta': cta,
    }
    return render(request, 'properties/property-agent.html', context)


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
