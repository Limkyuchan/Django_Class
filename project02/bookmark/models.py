from django.db import models

# Create your models here.

class Bookmark(models.Model):
    # 제목, url (== create table 과 같음)
    title = models.CharField(max_length = 100)      # blank=True, null=True : 제약조건
    url = models.URLField('url', unique = True)     # unique : 제약조건 (같은 값이 들어갈 수 없다.)

    def __str__(self):
        return f"{self.title}:{self.url}"  # Bookmark로 객체 생성 후 Bookmark 출력 시 __str__로 출력가능