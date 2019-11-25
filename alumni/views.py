from django.shortcuts import render
from .models import Alumni
# Create your views here.
def alumni(request):
    obj_alumni = Alumni.objects.all()
    obj_year = []
    for i in obj_alumni:obj_year.append(i.year)
    new_lst = list(set(obj_year))
    new_lst.sort()
    dict = {'alum':obj_alumni,'year':new_lst}
    return render(request,'alumni.html',context=dict)
