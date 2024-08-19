from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ContactSubmission, ContactImage,PropertyHeaderImage,Property,PropertyAgent_HeaderImage, PropertyAgent_TeamMember, PropertyAgent_CallToAction,AboutUs_HeaderImage, AboutUs_CallToAction, AboutUs_TeamMember,Home_Header, Home_HeaderImage, Home_CallToAction, Home_Testimonial,CareerApplication,Career_HeaderImage,PropertyImage


def home(request):
    header = Home_Header.objects.first()
    header_images = Home_HeaderImage.objects.all()
    properties = Property.objects.all()
    call_to_action = Home_CallToAction.objects.first()
    testimonials = Home_Testimonial.objects.all()

    for_sell_properties = properties.filter(property_type='sell')[:6]
    additional_sell_properties = properties.filter(property_type='sell')[6:]
    sold_properties = properties.filter(property_type='sold')[:6]

    # Get all unique locations
    unique_location_dicts = Property.objects.values('location').distinct()
    unique_locations = [loc['location'] for loc in unique_location_dicts]
    # print('unique_locations: ', unique_locations)

    # Get search parameters
    title = request.GET.get('title', '')
    property_type = request.GET.get('property_type', '')
    location = request.GET.get('location', '')

# Filter properties based on search parameters
    try:
        if title or property_type or location:
            search_input = True
        else:
            search_input = False

        if title:
            properties = properties.filter(title__icontains=title)
        if property_type:
            properties = properties.filter(property_type=property_type)
        if location:
            properties = properties.filter(location__icontains=location)
            
    except Exception as e:
        print(f"Error while filtering properties: {e}")

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
        'unique_locations': unique_locations,
        'search_input': search_input,
        'search_title': title,
        'search_property_type': property_type,
        'search_location': location,
    }
    return render(request, 'properties/home.html', context)

# def home(request):
#     header = Home_Header.objects.first()
#     header_images = Home_HeaderImage.objects.all()
#     call_to_action = Home_CallToAction.objects.first()
#     testimonials = Home_Testimonial.objects.all()

#     # Get all unique locations
#     unique_location_dicts = Property.objects.values('location').distinct()
#     unique_locations = [loc['location'] for loc in unique_location_dicts]

#     # Get search parameters
#     title = request.GET.get('title', '')
#     property_type = request.GET.get('property_type', '')
#     location = request.GET.get('location', '')

#     print(f"Search Parameters - Title: {title}, Property Type: {property_type}, Location: {location}")

#     # Initialize base queryset
#     properties = Property.objects.all()

#     # Apply search filters
#     if title:
#         properties = properties.filter(title__icontains=title)

#     if property_type:
#         properties = properties.filter(property_type=property_type)

#     if location:
#         properties = properties.filter(location__icontains=location)

#     # Separate properties into categories
#     for_sell_properties = properties.filter(property_type='sell')[:6]
#     additional_sell_properties = properties.filter(property_type='sell')[6:]
#     sold_properties = properties.filter(property_type='sold')[:6]
#     additional_sold_properties = properties.filter(property_type='sold')[6:]
#     upcoming_properties = properties.filter(property_type='upcoming')[:6]
#     additional_upcoming_properties = properties.filter(property_type='upcoming')[6:]
#     completed_properties = properties.filter(property_type='completed')[:6]
#     additional_completed_properties = properties.filter(property_type='completed')[6:]

#     print(f"for_sell_properties: {for_sell_properties}")
#     print(f"sold_properties: {sold_properties}")
#     print(f"upcoming_properties: {upcoming_properties}")
#     print(f"completed_properties: {completed_properties}")

#     context = {
#         'header': header,
#         'header_images': header_images,
#         'for_sell_properties': for_sell_properties,
#         'additional_sell_properties': additional_sell_properties,
#         'sold_properties': sold_properties,
#         'additional_sold_properties': additional_sold_properties,
#         'upcoming_properties': upcoming_properties,
#         'additional_upcoming_properties': additional_upcoming_properties,
#         'completed_properties': completed_properties,
#         'additional_completed_properties': additional_completed_properties,
#         'call_to_action': call_to_action,
#         'testimonials': testimonials,
#         'unique_locations': unique_locations,
#     }

#     print(f"Context: {context}")

#     return render(request, 'properties/home.html', context)




def career(request):
    header_image = Career_HeaderImage.objects.first()  # Retrieve header image

    context = {
        'header_image': header_image,
    }

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        number = request.POST.get('number')
        address = request.POST.get('address')
        message = request.POST.get('message')
        cv = request.FILES.get('cv')

        if name and email and number and address and message and cv:
            # Save the career application
            application = CareerApplication(
                name=name,
                email=email,
                number=number,
                address=address,
                message=message,
                cv=cv
            )
            application.save()

            # Add success message
            messages.success(request, 'Your application has been submitted successfully.')

            return redirect('career')  # Redirect to the career page
        else:
            # Add error message if form is not valid
            messages.error(request, 'Please fill out all fields.')

    return render(request, 'properties/career.html', context)




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

def primary_p(request):
    header_image = PropertyHeaderImage.objects.first()  # Assuming you have only one header image
    p_properties=Property.objects.filter(category='P').order_by('id')
    for_sell_properties = p_properties.filter(property_type='sell')[:6]
    additional_sell_properties = p_properties.filter(property_type='sell')[6:]
    sold_properties = p_properties.filter(property_type='sold')[:6]
    additional_sold_properties = p_properties.filter(property_type='sold')[6:]
    upcoming_properties = p_properties.filter(property_type='upcoming')[:6]
    additional_upcoming_properties = p_properties.filter(property_type='upcoming')[6:]
    completed_properties = p_properties.filter(property_type='completed')[:6]
    additional_completed_properties = p_properties.filter(property_type='completed')[6:]
    context = {
        'p_properties': p_properties,
        'header_image': header_image,
        'for_sell_properties': for_sell_properties,
        'additional_sell_properties': additional_sell_properties,
        'sold_properties': sold_properties,
        'additional_sold_properties': additional_sold_properties,
        'upcoming_properties': upcoming_properties,
        'additional_upcoming_properties': additional_upcoming_properties,
        'completed_properties': completed_properties,
        'additional_completed_properties': additional_completed_properties,
        }
    return render(request, 'properties/Primary_project.html',context)




def secondary_p(request):
    header_image = PropertyHeaderImage.objects.first()  # Assuming you have only one header image
    s_properties=Property.objects.filter(category='S').order_by('id')
    for_sell_properties = s_properties.filter(property_type='sell')[:6]
    additional_sell_properties = s_properties.filter(property_type='sell')[6:]
    sold_properties = s_properties.filter(property_type='sold')[:6]
    additional_sold_properties = s_properties.filter(property_type='sold')[6:]
    upcoming_properties = s_properties.filter(property_type='upcoming')[:6]
    additional_upcoming_properties = s_properties.filter(property_type='upcoming')[6:]
    completed_properties = s_properties.filter(property_type='completed')[:6]
    additional_completed_properties = s_properties.filter(property_type='completed')[6:]
    context = {
        's_properties': s_properties,
        'header_image': header_image,
        'for_sell_properties': for_sell_properties,
        'additional_sell_properties': additional_sell_properties,
        'sold_properties': sold_properties,
        'additional_sold_properties': additional_sold_properties,
        'upcoming_properties': upcoming_properties,
        'additional_upcoming_properties': additional_upcoming_properties,
        'completed_properties': completed_properties,
        'additional_completed_properties': additional_completed_properties,
        }
    return render(request, 'properties/Secondary_project.html',context)


def land_p(request):
    header_image = PropertyHeaderImage.objects.first()  # Assuming you have only one header image
    l_properties=Property.objects.filter(category='L').order_by('id')
    for_sell_properties = l_properties.filter(property_type='sell')[:6]
    additional_sell_properties = l_properties.filter(property_type='sell')[6:]
    sold_properties = l_properties.filter(property_type='sold')[:6]
    additional_sold_properties = l_properties.filter(property_type='sold')[6:]
    upcoming_properties = l_properties.filter(property_type='upcoming')[:6]
    additional_upcoming_properties = l_properties.filter(property_type='upcoming')[6:]
    completed_properties = l_properties.filter(property_type='completed')[:6]
    additional_completed_properties = l_properties.filter(property_type='completed')[6:]
    context = {
        'l_properties': l_properties,
        'header_image': header_image,
        'for_sell_properties': for_sell_properties,
        'additional_sell_properties': additional_sell_properties,
        'sold_properties': sold_properties,
        'additional_sold_properties': additional_sold_properties,
        'upcoming_properties': upcoming_properties,
        'additional_upcoming_properties': additional_upcoming_properties,
        'completed_properties': completed_properties,
        'additional_completed_properties': additional_completed_properties,
        }
    return render(request, 'properties/Land_shearing.html',context)


def join_p(request):
    header_image = PropertyHeaderImage.objects.first()  # Assuming you have only one header image
    j_properties=Property.objects.filter(category='J').order_by('id')
    for_sell_properties = j_properties.filter(property_type='sell')[:6]
    additional_sell_properties = j_properties.filter(property_type='sell')[6:]
    sold_properties = j_properties.filter(property_type='sold')[:6]
    additional_sold_properties = j_properties.filter(property_type='sold')[6:]
    upcoming_properties = j_properties.filter(property_type='upcoming')[:6]
    additional_upcoming_properties = j_properties.filter(property_type='upcoming')[6:]
    completed_properties = j_properties.filter(property_type='completed')[:6]
    additional_completed_properties = j_properties.filter(property_type='completed')[6:]
    context = {
        'j_properties': j_properties,
        'header_image': header_image,
        'for_sell_properties': for_sell_properties,
        'additional_sell_properties': additional_sell_properties,
        'sold_properties': sold_properties,
        'additional_sold_properties': additional_sold_properties,
        'upcoming_properties': upcoming_properties,
        'additional_upcoming_properties': additional_upcoming_properties,
        'completed_properties': completed_properties,
        'additional_completed_properties': additional_completed_properties,
        }
    return render(request, 'properties/join_venture.html',context)








def property(request):
    properties = Property.objects.all()
    header_image = PropertyHeaderImage.objects.first()  # Assuming you have only one header image
    for_sell_properties = properties.filter(property_type='sell')[:6]
    additional_sell_properties = properties.filter(property_type='sell')[6:]
    sold_properties = properties.filter(property_type='sold')[:6]
    additional_sold_properties = properties.filter(property_type='sold')[6:]
    upcoming_properties = properties.filter(property_type='upcoming')[:6]
    additional_upcoming_properties = properties.filter(property_type='upcoming')[6:]
    completed_properties = properties.filter(property_type='completed')[:6]
    additional_completed_properties = properties.filter(property_type='completed')[6:]
    
    context = {
        'properties': properties,
        'header_image': header_image,
        'for_sell_properties': for_sell_properties,
        'additional_sell_properties': additional_sell_properties,
        'sold_properties': sold_properties,
        'additional_sold_properties': additional_sold_properties,
        'upcoming_properties': upcoming_properties,
        'additional_upcoming_properties': additional_upcoming_properties,
        'completed_properties': completed_properties,
        'additional_completed_properties': additional_completed_properties,
    }
    return render(request, 'properties/property-list.html', context)



from django.shortcuts import render, get_object_or_404
def property_detail(request, pk):
    property = get_object_or_404(Property, pk=pk)
    additional_images = property.images.all()
    context = {
        'property': property,
        'additional_images': additional_images,
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


