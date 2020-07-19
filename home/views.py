from django.shortcuts import render, HttpResponse
from home.models import Contact

def home(request):
    return render(request, 'home/home.html')

def about(request):
    return render(request, 'home/about.html')

def projects(request):
    return render(request, 'home/projects.html')

def contact(request):
    if request.method=="POST":
        name = request.POST['name']
        email = request.POST['email']
        desc = request.POST['desc']
        contact = Contact(name=name, email=email, desc=desc)
        contact.save()
    return render(request, 'home/contact.html')
