from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'properties/index.html')
def about(request):
    return render(request, 'properties/about.html')
def property(request):
    return render(request, 'properties/property-list.html')
def contact(request):
    return render(request, 'properties/contact.html')