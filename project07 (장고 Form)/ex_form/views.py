from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from .models import Person


def index(request):
    return render(request, 'ex_form/index.html')


# 1. form을 직접 생성
def exam01(request):
    if request.method == 'POST':
        name = request.POST['name']
        age = request.POST['age']
        print('요청 처리: ', name, age)
        Person(name=name, age=age).save()         # 모델에 입력 값 저장
        return HttpResponse('처리 완료!')
    
    else:
        return render(request, 'ex_form/exam01_form.html')


# 2. 장고 form 생성
from .forms import PersonForm

def exam02(request):
    if request.method == 'POST':
        personForm = PersonForm(request.POST)   # POST로 들어온 값을 파라미터로 뽑지 않아도 장고 PersonForm에서 알아서 세팅(name, age)을 해줌 
        if personForm.is_valid():               # 유효성 검증 (정상적인 값이 입력되었는지?) 
            # 요청 값이 정상적인지 검증하는 작업을 가짐. 문제가 없으면 cleaned_data에 값을 담는다.
            name = personForm.cleaned_data['name']     # cleaned_data (= 딕셔너리) 에 저장된 값을 꺼낸다.
            age = personForm.cleaned_data['age']     
            Person(name=name, age=age).save()
            return HttpResponse('처리 완료!')
        else:                                   # 유효하지 않다면 personForm에 error(에러) 메세지가 포함된다.
            return render(request, 'ex_form/exam02_form.html', {'form':personForm})
        
    else:
        form = PersonForm()     # 객체 생성
        return render(request, 'ex_form/exam02_form.html', {'form':form})



# 3. 모델을 이용한 form
from .forms import PersonModelForm

def exam03(request):
    if request.method == 'POST':
        form = PersonModelForm(request.POST)
        if form.is_valid():
            form.save()         # 값을 꺼낼 필요가 없다. 그냥 form을 저장. 모델로 만들어진 form으로 바로 저장.
            return HttpResponse('처리 완료!')
    
    else:
        form = PersonModelForm()
        
    return render(request, 'ex_form/exam03_form.html', {'form':form})


#####################################################################

# 장고 Generic View

from django.views.generic import View   # 클래스 뷰 사용시 View를 상속
from django.shortcuts import redirect, reverse

class MyView1(View):    # 클래스 뷰
    
    def get(self, request):         # GET 요청일 때 동작하는 메소드
        form = PersonModelForm()
        return render(request, 'ex_form/exam04_form.html', {'form':form})
    
    def post(self, request):        # POST 요청일 때 동작하는 메소드
        form = PersonModelForm(request.POST)
        if form.is_valid():
            form.save()             # 모델form 이라 바로 save 가능
            return redirect(reverse('ex_form:index'))
        
        return render(request, 'ex_form/exam04_form.html', {'form':form})
    
    
    
class MyView2(View):
    # 장고가 지원하는 Generic View(일반형 뷰)에서 아래와 같은 설정만 해주면 장고가 알아서 다 해줌
    form_class = PersonModelForm
    initial = {
        'name' : '이름',
        'age' : 0,
    }
    template_name = 'ex_form/exam04_form.html'
    
    def get(self, request):       
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})
    
    def post(self, request):        
        form = PersonModelForm(request.POST)
        if form.is_valid():
            form.save()            
            return redirect(reverse('ex_form:index'))
        
        return render(request, self.template_name, {'form':form})



# FormView  (앱이름/모델명_form.html)
from django.views.generic import FormView   # 저장하는 기능은 없음

class MyView3(FormView):
    form_class = PersonModelForm
    template_name = 'ex_form/exam04_form.html'
    success_url = '/ex/'    # 성공하면 redirect 할 수 있도록 설정
                            # success_url 에서는 < 하드코딩 > 만을 사용해야 된다.
                            # 사용할 경우 success_url = revese('ex_form:index') 는 사용 불가!
                            # success_url = reverse_lazy('ex_form:index')로 사용이 가능하다.
    
    def form_valid(self, form):
        print('데이터가 유효하면')
        m = Person(**form.cleaned_data)     # 유효하면 값을 저장
        m.save()
        
        return super().form_valid(form)
    
    

# CreateView    (앱이름/모델명_form.html)
from django.views.generic import CreateView     # 입력 값 저장하는 기능을 포함(get, post 모두 처리 가능)

class MyView4(CreateView):                      # 객체 생성, 입력된 데이터가 있으면 값을 알아서 저장
    model = Person                             
    form_class = PersonModelForm                 
    # template_name = 'ex_form/exam04_form.html'  
        # 위의 경로를 지정하지 않으면 장고에서 앱이름/모델명_form.html 을 알아서 찾게 되어있다.
        # =>  templates/ex_form/person_form.html 을 찾게 되어 있음
    success_url = '/ex/'
    
    

# DetailView    (앱이름/모델명_detail.html)
from django.views.generic import DetailView

class MyView5(DetailView):
    model = Person
    # template_name = 'ex_form/person_detail.html'      # 지정하지 않아도 알아서 경로를 찾는다.



# ListView      (앱이름/모델명_list.html)
from django.views.generic import ListView

class MyView6(ListView):
    model = Person
    # template_name = 'ex_form/person_list.html'        # 경로 자동으로 찾음!
    
    

# UpdateView    (앱이름/모델명_form.html)
from django.views.generic import UpdateView

class MyView7(UpdateView):  # 기존의 값을 이용해서 
    model = Person
    form_class = PersonModelForm
    # template_name = 'ex_form/person_form.html'
    success_url = '/ex/exam08/'                         ## 해당 하드코딩 변경 시 강사님 코드 참고

    def get_object(self):   # detail 화면으로 이동하기 위해 pk값을 사용하기 위한 함수 정의(재정의)
        print('update 처리')
        object = Person.objects.get(pk=self.kwargs['pk'])
        self.success_url += str(object.id) + '/'
        return object
    


# [ 상황에 따라 재정의(오버라이딩)가 필요할 수 있는 메서드들 ]
# get_context_data()
# get_queryset()
# get_form_class()
# form_valid()
# form_invalid()
# get_success_url



# DeleteView    (앱이름/모델명_confirm_delete.html)
from django.views.generic import DeleteView

class MyView8(DeleteView):
    model = Person          # 어디에서 삭제할건지 정함
    # template_name = "ex_form/person_confirm_delete.html"
    success_url = reverse_lazy('ex_form:exam09')        # reverse 함수에 lazy를 함께 쓰면 사용 가능