from django.urls import path
from . import views

app_name = 'example'

urlpatterns = [
    path('', views.index, name='index'),
    path('infoform/', views.infoform, name='infoform'),
    path('inforesult/', views.inforesult, name='inforesult'),
    path('selectform/', views.selectform, name='selectform'),
    path('selectresult/', views.selectresult, name='selectresult'),
    path('comboform/', views.comboform, name='comboform'),
    path('comboresult/', views.comboresult, name='comboresult'),
    path('forfrom/', views.forform, name='forform'),
    path('forresult/', views.forresult, name='forresult'),
    path('lottoform/', views.lottoform, name='lottoform'),
    path('lottoresult/', views.lottoresult, name='lottoresult'),
]
