from typing import Any, Dict
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from .forms import BoardForm
from .models import Board



# ListView
from django.views.generic import ListView
class BoardList(ListView):
    model = Board
    ordering = ['-pk']      # pk 값으로 내림차순 정렬
    # template_name = 'board/board_list.html'
   
   
    
# CreateView
from django.views.generic import CreateView
class BoardCreate(CreateView):
    model = Board
    form_class = BoardForm
    template_name = 'board/board_create.html'
    success_url = reverse_lazy('board:list')    # 클래스 멤버, _lazy: 예약해 두는 것 
    
    # # 같은 form을 사용할 때 저장된 값을 따로 사용하기 위해서(create, update 같은 form 사용 시)
    # def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
    #     context = super().get_context_data(**kwargs)
    #     context['button_label'] = '등록'
    #     return context
        
    

# DetailView
from django.views.generic import DetailView
class BoardDetail(DetailView):
    model = Board
    # template_name = 'board/board_detail.html'
    
    # 조회수 증가 기능 적용
    def get_object(self):   # 재정의한다(오버라이딩)
        object = super().get_object()
        object.incrementReadCount()
        # object = Board.objects.get(id=self.kwargs['pk'])
        # object.incrementReadCount()
        return object
    
    
    
# UpdateView
from django.views.generic import UpdateView
class BoardUpdate(UpdateView):
    model = Board
    form_class = BoardForm          # 보여질 내용 설정
    template_name = 'board/board_update.html'
    success_url = ''
    # success_url = reverse_lazy('board:list')    # 수정 후 목록으로 리다이렉트 응답
    
    def get_object(self):   # 재정의한다(오버라이딩)
        object = Board.objects.get(id=self.kwargs['pk'])
        self.success_url += '/board/' + str(object.id) + '/detail/'
        return object
    
    # def get_success_url(self):
    #     print(self.object.id)
    #     reverse('board:detail', args=(self.object.id,))

    # # 같은 form을 사용할 때 저장된 값을 따로 사용하기 위해서(create, update 같은 form 사용 시)
    # def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
    #     context = super().get_context_data(**kwargs)
    #     context['button_label'] = '수정'
    #     return context
    

# DeleteView
from django.views.generic import DeleteView
class BoardDelete(DeleteView):
    model = Board
    # template_name = "board/board_confirm_delete.html"
    success_url = reverse_lazy('board:list')