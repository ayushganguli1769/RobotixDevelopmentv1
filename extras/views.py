from django.shortcuts import render
from .models import FYI,DIY
# Create your views here
def diy(request):
    obj_diy = DIY.objects.all()
    dict = {'diy':obj_diy}
    return render(request,'diy.html',context=dict)

def fyi(request):
    obj_fyi = FYI.objects.all()
    dict = {'fyi':obj_fyi}
    return render(request,'fyi.html',context=dict)
