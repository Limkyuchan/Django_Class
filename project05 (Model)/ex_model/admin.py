from django.contrib import admin

# Register your models here.

# 내가 사용하는 모델을 등록해 주면 관리자사이트에서 확인할 수 있다.

from .models import Info

admin.site.register(Info)   # 관리자 사이트에 모델 등록