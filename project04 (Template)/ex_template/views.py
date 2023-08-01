from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

def index(request):
    return render(request, 'ex_template/index.html')


def ex01(request):
    n1 = 100
    lst = [1,2,3]
    tup = (4,5,6)
    dic = {'a':1, 'b':2, 'c':3}
    
    context = {
        'n1' : n1,
        'lst' : lst,
        'tup' : tup,
        'dic' : dic,
    }
    return render(request, 'ex_template/ex01.html', context)    # context : 템플릿 변수


def ex02(request):
    val1 = 'hello<world><br>'
    lst = [ 'hO', 'Hi', 'weLCome']
    tup = ( 1, 2, 3)
    dic = {'aa':10, 'bb':20, 'cc':30, }
    bio = 'hi1 hi2 hi3 hi4 hi5 hi6 hi7 hi8 hi9 hi10'
    ls = [100]
    lss = [100, 200]
    data = {    'val1':val1, 'lst':lst, 'tup':tup,
                'dic':dic, 'bio':bio, 'ls':ls, 'lss':lss, }
    return render(request, 'ex_template/ex02.html', data)


class Info:
    def __init__ (self, name, age):
        self.name = name
        self.age = age
    
    def __str__ (self):
        return f"Info[name = {self.name}, age = {self.age}]"    
    
    
def ex03(request):
    name_list = ['홍길동', '이순신', '임꺽정', '강감찬']
    info_list = [
        Info('홍길동', 33),
        Info('이순신', 34),
        Info('임꺽정', 23),
        Info('강감찬', 89),
    ]
    context = {
        'name_list' : name_list,
        'info_list' : info_list,
    }
    return render(request, 'ex_template/ex03.html', context)


def ex04(request):
    name_list = ['홍길동', '이순신', '임꺽정', '강감찬']
    info_list = [
        Info('홍길동', 33),
        Info('이순신', 34),
        Info('임꺽정', 23),
        Info('강감찬', 89),
    ]
    context = {
        'value' : 100,
        'name_list' : name_list,
        'info_list' : info_list,
    }
    return render(request, 'ex_template/ex04.html', context)



from django.urls import reverse
def ex05(request):
    url_list = [
            reverse('ex_template:index'),
            reverse('ex_template:ex01'),
            reverse('ex_template:ex02'),
            reverse('ex_template:ex03'),
            reverse('ex_template:ex04'),
            reverse('ex_template:ex05path', args=(10, 'hong')),
    ]
    return render(request, "ex_template/ex05.html", 
                  {'url_list': url_list, 'n':10, 'name':'kim',})
    
    
def ex06(request):
    if request.method == 'GET':
        return render(request, 'ex_template/ex06.html')  
    elif request.method == 'POST':
        id = request.POST['id']  
        pw = request.POST['pw']
        if id == pw:
            return HttpResponse('로그인 성공')
        else:
            return HttpResponseRedirect(reverse('ex_template:ex06'))
        

def ex07(request):
    value = 100
    info = Info("홍길동", 33)
    context = {
        'value' : value,
        'info'  : info,
    }
    return render(request, 'ex_template/ex07.html', context)


def ex08(request):
    html = '''<h1>Hello</h1> 홍길동
    <script>
        alert('악의적인 동작');
    </script>
    '''
    cxt = {
        'html' : html,
    }
    return render(request, 'ex_template/ex08.html', cxt)