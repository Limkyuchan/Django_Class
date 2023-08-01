import datetime
from django.db import models
from django.utils import timezone

# Create your models here.

# ORM 

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    
    def __str__(self):
        return self.question_text
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) 
    # CASCADE : Question 항목이 삭제될 경우 해당 Question을 Foreign 하고 있는 Choice 또한 삭제되도록 함.
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.choice_text

# Model 변경 시
# 1. (models.py 에서) 모델을 변경합니다.
# 2. python manage.py makemigrations을 통해 이 변경사항에 대한 마이그레이션을 만드세요.
# 3. python manage.py migrate 명령을 통해 변경사항을 데이터베이스에 적용하세요