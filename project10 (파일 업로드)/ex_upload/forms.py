from django import forms
from .models import UploadFile

class UploadFileForm(forms.ModelForm):
    class Meta:
        model = UploadFile
        fields = ['title', 'file']
    
    # 1. 파일이 없어도 업로드 되도록 (파일에 대해 필수가 아님을 설정)
    file = forms.FileField(required=False)
    
    # 2. 
    # def __init__(self):
    #     super(UploadFileForm, self).__init__()
    #     self.fields['file'].required = False