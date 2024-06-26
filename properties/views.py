from django.shortcuts import render

# Create your views here.

def base(request):
    return render(request, 'properties/base.html')
def home(request):
    return render(request, 'properties/home.html')
def about(request):
    return render(request, 'properties/about.html')
def property(request):
    return render(request, 'properties/property-list.html')
def contact(request):
    return render(request, 'properties/contact.html')