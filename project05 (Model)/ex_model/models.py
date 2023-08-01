from django.db import models

# Create your models here.

class Info(models.Model):       # 모델을 상속받아서 정의 (모델은 기본적으로 id가 있음)
    name = models.CharField(max_length=20)              # 한 줄 짜리 자료형
    age = models.IntegerField(null=False)               # (제약 조건)
    intro = models.TextField()                          # 여러줄 자료를 받는 자료형
    regdate = models.DateTimeField(auto_now=True)       # 자동으로 현재 시간 추가   
    
    def __str__(self):                  # 객체가 가지는 값을 문자열로 출력
        return f"Info[id={self.id}, name={self.name}, age={self.age}...]"        