from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

# Create your views here.

from django.utils import timezone
from .models import Info

# def list(request):
#     info_list = Info.objects.all()
#     context = {
#         'info_list' : info_list,
#     }
#     return render(request, 'ex_model/list.html', context)


def index(request):
    info_list = Info.objects.all()
    cxt = {
        'info_list' : info_list,
        }
    return render(request, 'ex_model/index.html', cxt)


def detail(request, id):
    info_nobody = Info.objects.get(id=id)
    context = {
        'info_nobody' : info_nobody,
    }
    return render(request, 'ex_model/detail.html', context)

      
def addform(request):
    
    if request.method == "GET":
        return render(request, 'ex_model/addform.html')
        
    elif request.method == "POST":
        info_name = request.POST['name']
        info_age = request.POST['age']
        info_intro = request.POST['intro']
        Info.objects.create(name=info_name, age=info_age, intro=info_intro)
        return HttpResponseRedirect(reverse('ex_model:index'))


def editform(request, id):
    
    if request.method == "GET":
        info_nobody = Info.objects.get(id=id)
        context = {
            'info_nobody' : info_nobody,
        }
        return render(request, 'ex_model/editform.html', context)
    
    elif request.method == "POST":
        info_name = request.POST['name']
        info_age = request.POST['age']
        info_intro = request.POST['intro']
        Info.objects.filter(id=id).update(name=info_name, age=info_age, intro=info_intro)
        return HttpResponseRedirect(reverse('ex_model:index'))


def deleteform(request, id):
    
    if request.method == "GET":
        info_nobody = Info.objects.get(id=id)
        context = {
            'info_nobody' : info_nobody,
        }
        return render(request, 'ex_model/deleteform.html', context)
    
    elif request.method == "POST":
        Info.objects.get(id=id).delete()
        return HttpResponseRedirect(reverse('ex_model:index'))