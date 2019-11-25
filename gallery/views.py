from django.shortcuts import render
from .models import Gallery
# Create your views here.
def gallery(request):
    obj_gallery = Gallery.objects.all()
    dict = {'gallery':obj_gallery}
    return render(request,'gallery.html',context=dict)
