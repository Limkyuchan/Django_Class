from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.urls import reverse
from django.utils import timezone

####################################################################################

# [ 쿠키 ]  ex) 쿠폰과 같은 개념
# HTTP는 정보를 저장하지 않음. 쿠키를 이용해서 브라우저에 조각을 저장.
# 쿠키는 서버가 만들고 응답 헤더에 response 한다. request할 때 쿠키 값을 같이 전송
# 쿠키 = 클라이언트에 저장하는 데이터 조각, 클라이언트와 서버간에 값을 유지한다.

# [ 세션 ]  ex) 사장이 기록하고 있는 단골손님의 얼굴을 기억
# 역할: 클라이언트를 구분 (브라우저를 식별할 수 있다)
# 서버가 값을 생성. request할 때 세션 값을 같이 전송
# 브라우저별로 값이 서로 달라 서버는 어느 브라우저가 요청하는지 구분 하여 식별한다.
# > 요청 정보를 확인하고 누가 요청하는지 식별할 수 있다.(누군지 확인하고 해당 기록을 사용)
# >> 로그인을 유지하는데 세션을 사용할 수 있음

####################################################################################


# request 에서 쿠키, 세션 확인 (값 없으면 빈 딕셔너리 출력)
def index(request):             
    print(request.COOKIES)              # 쿠키 확인 (빈 딕셔너리 {} 출력됨 )
    print(request.session)              # 세션 확인
    print(request.session.session_key)  # 세션 아이디(키) 확인 (None 출력됨), 서버가 갖는 고유한 값!!
    # request.session['now'] = input('now입력: ')   # now값 확인
    context = {
        'cookies':request.COOKIES,
    }
    return render(request, 'ex_cookie/index.html', context)


# 세션 쿠키
def session_cookie(request):
    response = HttpResponse('세션 쿠키 생성')
    
    if not request.COOKIES.get('mycookie'):
        cname = 'mycookie'              
        cval = timezone.now()
        response.set_cookie(cname, cval)    # 세션 쿠키를 생성(브라우저 끄면 사라짐)
        
    return response


# 영구 쿠키 (만료 시간(유효시간)이 지나면 사라짐)
def permanent_cookie(request):
    response = HttpResponse('영구(permanent) 쿠키 생성')
    
    if not request.COOKIES.get('mycookie2'):
        cname = 'mycookie2'              
        cval = timezone.now().day
        response.set_cookie(
            cname,
            cval,
            max_age=60  # 초 단위 이므로 60*60*24*365 와 같은 방식으로 설정
        )   # 영구 쿠키 (max_age를 설정한 쿠키)
        
    return response


# 로그인 시 id 저장방법(아이디 기억하기) >> 쿠키 이용
def login(request): 
    if request.method == 'GET':
        remember_id = request.COOKIES.get('id', '')     # 쿠키 중에 id가 있는지를 확인 (있으면 id값 이용, 없으면 '')
        return render(request, 'ex_cookie/login.html', {'remember_id':remember_id})
    
    else:
        id = request.POST['id']
        pw = request.POST['pw']
        remember = request.POST.get('remember', '')     # remember 값 없을때 request.POST[]로 값 빼면 에러발생!
        response = HttpResponse('로그인 성공!')          # 에러 방지 위해 remember 값 이용 시 .get()을 이용하여 값을 추출
        if id == pw:       
            request.session['login_user'] = id          # ID를 세션에 저장
            
            # 로그인 성공 시 remember를 확인
            if remember == '':                          # remember 값이 없으면(아이디 기억하기 선택 안할 시) 기억하지 않겠다.
                response.delete_cookie('id')            # 응답 자료 중 id의 쿠키를 제거
            else:                                       # remember 값이 존재하면(아이디 기억하기 선택 시) 영구쿠키를 생성
                response.set_cookie('id', id, max_age=60*60)
  
            return response
        
        else:
            # 로그인 실패 시 해당 페이지 재요청
            return render(request, 'ex_cookie/login.html')
        
        
# 로그아웃 시 저장된 세션 삭제
def logout(request):                        # 세션과 관련된 모든 정보 삭제
    request.session.flush()                 # 세션 삭제, 쿠키에 들어간 sessionid 삭제
    response = redirect(reverse('ex_cookie:index'))
    return response                         