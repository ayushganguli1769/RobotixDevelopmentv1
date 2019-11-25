from django.shortcuts import render
from .models import Convenor,Coordinator,HeadCoordinator,Manager
# Create your views here.
def about(request):
    obj_conv = Convenor.objects.all()
    obj_head = HeadCoordinator.objects.all()
    obj_manager = Manager.objects.all()
    obj_Cord = Coordinator.objects.all()
    dict = {'Convenor':obj_conv, 'Head':obj_head, 'Manager':obj_manager,'Cord':obj_Cord}
    return render(request,'aboutus.html',context=dict)
