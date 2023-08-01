from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from random import randint

# Create your views here.

def index(request):
    return render(request, 'example/index.html')



def infoform(request):
    return render(request, 'example/infoform.html')

def inforesult(request):
    id = request.POST['id']
    pw = request.POST['pw']
    msg = request.POST['message']
    context = {
        'id' : id,
        'pw' : pw,
        'msg' : msg,
    }
    return render(request, 'example/inforesult.html', context)



def selectform(request):
    return render(request, 'example/selectform.html')

def selectresult(request):
    edu = request.POST['education']
    nat = request.POST['nation']
    inter = request.POST['interest']
    context = {
        'edu' : edu,
        'nat' : nat,
        'inter' : inter,
    }
    return render(request, 'example/selectresult.html', context)



def comboform(request):
    return render(request, 'example/comboform.html')

def comboresult(request):
    site = request.POST['site']
    return HttpResponseRedirect(site)
    
    # < value를 안 썼을 때 >
    # if site == '네이버':
    #     return HttpResponseRedirect("https://naver.com")
    # elif site == '다음':
    #     return HttpResponseRedirect("https://daum.net")
    # elif site == '구글':
    #     return HttpResponseRedirect("https://google.com")
    # elif site == '유튜브':
    #     return HttpResponseRedirect("https://youtube.com")
    


def forform(request):
    return render(request, 'example/forform.html')

def forresult(request):
    number = int(request.POST['num'])
    a = 0
    for i in range(1, number+1):
        a += i
        
    context = {
        'a' : a,
        'number' : number,
    }
    return render(request, 'example/forresult.html', context)



def lottoform(request):
    return render(request, 'example/lottoform.html')

def lottoresult(request):
    number = int(request.POST['num'])
    
    total_list = []
    for i in range(number):
        li = []
        sort_li = []
        while len(li) < 6:
            su = randint(1,45)
            if su not in li:
                li.append(su)
        sort_li = sorted(li, key=lambda x:x)
        total_list.append(sort_li)
    context = {
        'total_list' : total_list,
    }        
            
    return render(request, 'example/lottoresult.html', context)