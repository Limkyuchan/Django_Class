from django.shortcuts import redirect, render
from django.urls import reverse
from .forms import UploadFileForm
from .models import UploadFile


def index(request):
    return render(request, 'ex_upload/index.html')


def upload(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        # input type = 'file' (input 타입이 file) => 여러개의 파일들을 받을 수 있도록 FILES
        
        if form.is_valid():     # 값에 이상이 없으면 (유효성 검사) 
            form.save()         # 저장
            return redirect(reverse('ex_upload:index'))
        
    else:
        form = UploadFileForm()
        
    return render(request, 'ex_upload/upload.html', {'form':form})


import os
from django.conf import settings

def file_list(request):
    list = UploadFile.objects.all().order_by('-pk')
    return render(request, 'ex_upload/file_list.html',{'list':list})


def delete_file(request, id):
    file = UploadFile.objects.get(pk=id)

    # 실제 업로드 된 파일도 삭제 (삭제할 때 db 뿐만 아니라 실제 파일도 삭제하기 위해서) 
    media_root = settings.MEDIA_ROOT
    remove_file = media_root + "/" + str(file.file)
    print('삭제할 파일: ', remove_file)
    
    if os.path.isfile(remove_file): # remove_file 이 존재한다면
        os.remove(remove_file)      # 실제 파일 삭제
    
    file.delete()   # DB에서 삭제 (데이터베이스에 들어있는 값을 삭제)
    
    return redirect(reverse('ex_upload:list'))
    