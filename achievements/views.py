from django.shortcuts import render
from .models import Achievements
# Create your views here.
def achievement(request):
    obj_achievements = Achievements.objects.all()
    dict = {'achievement':obj_achievements}
    return render(request,'achievements.html',context=dict)
