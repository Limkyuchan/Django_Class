from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone

def index(request):
    now = timezone.now()
    context = {             # context를 이용해서 html 에 값을 표현하고자 할 때
        'now' : now,        # 이 값을 템플릿에서 사용할 수 있음
        'name' : '홍길동',
    }
    return render(request, 'index.html', context)    # render 함수를 사용하여 html경로를 설정