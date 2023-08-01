from django.contrib import admin
from .models import Bookmark

# Register your models here.

admin.site.register(Bookmark)      # 관리 사이트 등록
                                   # admin의 site에다가 Bookmark를 등록하겠다. 
