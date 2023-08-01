from django.urls import path
from . import views

app_name = "exview"     # views.py 안의 reverse 에서 해당 url 찾는 용도로 사용됨 (각 함수의 name과 함께 사용)

urlpatterns = [

    # 함수형 뷰 (views의 함수를 선택)           # name 속성을 작성 : views.py 에서 reverse를 사용하기 위함!!
    path('', views.index, name="index"),
    path('get1/', views.get1, name="get1"),                              # views.py 에서 get1 함수를 생성해야 오류발생 X
    path('get2/<int:n1>/<int:n2>/<str:n3>', views.get2, name="get2"),    # get2에 대해 경로변수로 표현(숫자, 숫자, 문자)
    path('post1/', views.post1),
    path('post2/<str:msg>/<int:n>/', views.post2),                       # 경로변수 활용
    path('getpost1/', views.getpost1),
    
    
    # 클래스형 뷰                                # 함수형 뷰는 해당 함수를 바로 호출하지만,
    path('get3/', views.ExamGet3.as_view()),    # 클래스형 뷰 사용 시 .as_view() 를 붙여야 한다.
    path('get4/<int:n1>/<int:n2>/<str:n3>', views.ExamGet4.as_view()),
    path('post3/', views.ExamPost3.as_view()),
    path('post4/<str:msg>/<int:n>/', views.ExamPost4.as_view()),
    path('getpost2/', views.ExamGetPost.as_view()),   
]