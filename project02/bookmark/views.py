from django.shortcuts import render
# from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from bookmark.models import Bookmark

# Create your views here.

# view 함수에서 request는 필수!
# 모델에 접근해서 db정보를 가지고 와서 그 정보를 template을 통해 사용자에게 제공

def index(request):
    print("index 요청됨")
    
    # print(reverse('bookmark:index'))
    # print(reverse('bookmark:regist'))
    # print(reverse('bookmark:reg_proc'))
    
    bookmark_list = Bookmark.objects.all()
    
    # result=""
    # for bookmark in bookmark_list:
    #     print(f"{bookmark.id}. {bookmark.title} : {bookmark.url}")
    #     result += f"{bookmark.id}. {bookmark.title} : {bookmark.url}" + '<br>'
    
    context = {
        'result': bookmark_list,
        'name' : '홍길동',
        }

    return render(request, "bookmark/index.html", context)
    
    
def regist(request):
    return render(request, "bookmark/regist.html")
       
    
def regist_proc(request):
    title = request.POST['title']       # POST 형식 중 키의 값이 title
    url = request.POST['url']
    print(f"{title}, {url}")
    bk = Bookmark(title=title, url=url)
    bk.save()                           # db 값 저장
    return HttpResponseRedirect("/bookmark/")   
    # HttpResponseRedirect : 다시 요청하는 과정. 등록이 끝나고 다시 bookmark로 이동하도록 요청.
    