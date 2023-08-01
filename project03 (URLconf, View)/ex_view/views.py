from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from django.shortcuts import render
# 템플릿을 선택해서 응답을 줄 때 render를 사용
from django.urls import reverse
# URL reverse : 앱의 urls.py 에서 {앱 이름 : name} 에 맞는 url 경로를 가져옴. --> template에서 주로 사용


## views.py 코드 작성 시 exurls.py에 꼭 연결해주어야 한다!!!! ## 


# 1) 함수형 뷰
def index(request):
    
    # 1. 서버 요청 잘 들어오는지 확인.
    # print("클라이언트로부터 요청을 받음")
    # print("===========================")
    # print(f"GET : {request.GET}")      # 요청 파라미터가 들어감.
    # print(f"POST : {request.POST}")    # GET 활용하면 GET으로 POST 활용하면 POST 딕셔너리로 작성됨
    # print(f"get_host : {request.get_host()}")
    # print(f"get_port : {request.get_port()}")
    # print("===========================")
    
    # 2. HTMl코드를 view 함수에서 직접 작성
    # response_body = """
    #     <!DOCTYPE html>
    #     <html>
    #         <head>
    #             <title>Index</title>
    #         </head>
    #         <body>
    #             <h1>메인입니다.</h1>
    #         </body>
    #     </html>   
    # """
    
    # 3. Template를 활용하여 HTML 코드 작성
    now = timezone.now()
    print("현재 시간: ", now)
    print(reverse("exview:index"))       # exurls.py 에서 name을 이용하여 작성 (app_name으로 활용, app_name:"name")                        
    print(reverse("exview:get1"))        # "exview:index" -> url을 찾아오기 위함                       
    print(reverse("exview:get2", args=(11,22,"hell")))  # get2는 인자에 대한 파라미터가 추가로 필요                           
                                 
    return render(request, "ex_view/index.html", {'now1':now})   
                                    # 앞의now1은 템플릿 안의 index.html에서 사용할 이름(변수)


# GET1 에 대한 함수
def get1(request):
    print("get1/ 요청 들어옴")
    #print(request.GET)             # n1, n2, n3의 딕셔너리 값이 출력됨 (모든 자료는 문자열)
    keys = request.GET.keys()
    print(int(request.GET['n1']) + int(request.GET['n2']))  # 문자열이기 때문에 정수자료형으로
    for key in keys:
        value = request.GET[key]
        print(f"{key} : {value}")   # request에서 GET의 key와 value값을 출력 
    return HttpResponse('get1')


# GET2 에 대한 함수 (경로변수)
def get2(request, n1, n2, n3):  # 경로변수에 있는 값이 해당 위치에 저절로 들어간다.
    print("n1: ", n1)
    print("n2: ", n2)
    print("n3: ", n3)
    print(n1 + n2)
    return HttpResponse('get2')


# POST1 에 대한 함수
def post1(request):
    print("post1/ 요청 들어옴")
    keys = request.POST.keys()      # POST 방식이기 때문에 request.POST로
    print(int(request.POST['n1']) + int(request.POST['n2']))  
    for key in keys:
        value = request.POST[key]
        print(f"{key} : {value}")  
    return HttpResponse('post1')


# POST2에 대한 함수 (경로변수)
def post2(request, msg, n):         # index.html 에서 get2 에 대한 hello, 123을 받기 위한 파라미터
    print("post2/ 요청 들어옴")
    print("msg: ", msg)             # 경로에 들어있는 변수 값
    print("n: ", n)
    keys = request.POST.keys()      
    print(int(request.POST['n1']) + int(request.POST['n2']))  
    for key in keys:
        value = request.POST[key]
        print(f"{key} : {value}")  
    return HttpResponse('post2')


# 함수 하나로 GET과 POST를 한 곳에서 처리
def getpost1(request):
    print(request.method)              # 요청 메소드로 구분할 수 있다. (GET과 POST를 구분!)
    if request.method == 'GET':
        print("GET요청에 대한 처리")    # 사용자 입력 폼을 보여줌.  ex) login
    elif request.method == "POST":
        print("POST요청에 대한 처리")   # 입력값을 처리하는 용도    ex) login process
    return HttpResponse("getpost1") 




# 2) 클래스형 뷰      
from django.views.generic import View       # ★★ generic View : 일반화된 View

class ExamGet3(View):   # View를 상속
    def get(self, request):         # View가 가지고 있는 것을 오버라이딩 한 개념.
        print("get3/ 요청 들어옴")
        keys = request.GET.keys()
        print(int(request.GET['n1']) + int(request.GET['n2']))  
        for key in keys:
            value = request.GET[key]
            print(f"{key} : {value}")  
        return HttpResponse('get3')
    
    
class ExamGet4(View):   
    def get(self, request, n1, n2, n3):     # get 요청을 처리할 때는 get 매서드가 처리한다.
        print("n1: ", n1)                   # get 으로 함수 작성해야 한다.
        print("n2: ", n2)
        print("n3: ", n3)
        print(n1 + n2)
        return HttpResponse('get4')


class ExamPost3(View):
    def post(self, request):                # post 요청을 처리할 때는 post 매서드가 처리한다.
        print("post3/ 요청 들어옴")          # post 으로 함수 작성해야 한다
        keys = request.POST.keys()    
        print(int(request.POST['n1']) + int(request.POST['n2']))  
        for key in keys:
            value = request.POST[key]
            print(f"{key} : {value}")  
        return HttpResponse('post3')

 
class ExamPost4(View):
    def post(self, request, msg, n):        
        print("post4/ 요청 들어옴")
        print("msg: ", msg)                 # 경로에 들어있는 변수 값
        print("n: ", n)
        keys = request.POST.keys()      
        print(int(request.POST['n1']) + int(request.POST['n2']))  
        for key in keys:
            value = request.POST[key]
            print(f"{key} : {value}")  
        return HttpResponse('post4')


class ExamGetPost(View):
    
    def get(self, request):                 # 입력 폼
        print("GET요청 동작")
        return HttpResponse("getpost2/(GET)")

    def post(self, request):                # 입력 값 처리
        print("POST요청 동작")
        user = request.POST["user"]
        pwd = request.POST["pwd"]
        if user == pwd:
            print("로그인 성공")
            return HttpResponse("getpost2/(POST)")
        else:
            print("로그인 실패(다시 폼 전송)")
            # return HttpResponseRedirect("/ex_view/")
            return HttpResponseRedirect(reverse('exview:index'))    # reverse 활용하여 경로 표현
