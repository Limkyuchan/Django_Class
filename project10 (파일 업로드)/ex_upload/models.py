from django.db import models

# Create your models here.

class UploadFile(models.Model):
    title = models.CharField(default="제목 없음", max_length=50)
    file = models.FileField(null=True)  # 데이터베이스에 파일 저장 시 파일의 위치를 저장. 실제 파일은 다른 곳에 저장.
        # settings에 설정한 MEDIA_ROOT에서 삭제에 필요한 경로를 아는데 이 경로는 절대 경로를 의미.
        # FileField 속성 중  upload_to=""  
            # upload_to에 작성하는 경로 중 user의 계정이름 또는 시간 등 으로 경로를 지정 가능하다.
            # 그 경로의 하위경로로서 만들어질 수 있음. (하위 디렉토리 즉, 상대경로를 설정 가능)
            # upload_to=""     # MEDIA_ROOT 하위경로(계정, 날짜 등으로 폴더 구조를 관리)


    def __str__(self):     # 제목               파일명
        return f"UploadFile[title={self.title}, file={self.file}]"