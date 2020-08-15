from django.shortcuts import render, HttpResponse
from home.models import Contact

def home(request):
    if request.method=="POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        desc = request.POST['desc']
        contact = Contact(name=name, email=email, desc=desc)
        contact.save()
    return render(request, 'home/home.html')

def masks(request):
    return render(request, 'home/masks.html')
