from django.shortcuts import render
from .models import Event,Workshop
# Create your views here.
def event(request):
    obj_event = Event.objects.all()
    obj_work = Workshop.objects.all()
    dict = {'Event':obj_event, 'Workshop':obj_work}
    return render(request,'events.html',context=dict)
