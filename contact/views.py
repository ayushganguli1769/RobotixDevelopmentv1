from django.shortcuts import render
from .models import Contact
# Create your views here.
def contact(request):

    if request.method == "POST":
        if request.POST['name'] and request.POST['email'] and request.POST['message']:
            obj_contact = Contact()
            obj_contact.name = request.POST['name']
            obj_contact.email = request.POST['email']
            obj_contact.message = request.POST['message']
            obj_contact.save()
            return render(request,'contact.html')
    else:
        return render(request,'contact.html')
