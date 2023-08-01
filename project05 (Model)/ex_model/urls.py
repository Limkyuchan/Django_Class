from django.urls import path
from . import views

app_name = 'ex_model'

urlpatterns = [
    # path('list/', views.list, name="list"),
    path('', views.index, name="index"),
    path('addform/', views.addform, name="addform"),
    path('detail/<int:id>/', views.detail, name="detail"),
    path('editform/<int:id>/', views.editform, name="editform"),
    path('deleteform/<int:id>/', views.deleteform, name="deleteform"),
]
