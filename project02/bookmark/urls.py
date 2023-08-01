from django.urls import path
from . import views

app_name = 'bookmark'               # namespace

urlpatterns = [
    path('', views.index, name="index"),        # name은 각 url의 이름   ex) index -> ""
    path('regist/', views.regist, name="regist"),
    path('regist_proc/', views.regist_proc, name="reg_proc"),
]
