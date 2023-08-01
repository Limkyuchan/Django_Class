from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Board

# Create your views here.

def board(request):
    return render(request, 'board/board.html')



def list(request):
    board_list = Board.objects.all()
    context = {
        'board_list' : board_list,
    }
    return render(request, 'board/list.html', context)


def detail(request, id):
    board = Board.objects.get(id=id)
    board.incrementReadCount()
    context = {
        'board' : board,
    }
    return render(request, 'board/detail.html', context)


def update(request, id): 
    board = Board.objects.get(id=id)
    if request.method == 'GET':
        context = {
            'board' : board,
        }
        return render(request, 'board/update.html', context)
    
    elif request.method == 'POST':
        board_title = request.POST['title']
        board_writer = request.POST['writer']
        board_content = request.POST['content']
        Board.objects.filter(id=id).update(title=board_title, writer=board_writer, content=board_content)
        return HttpResponseRedirect(reverse('board:detail', args=(board.id,))) # args 값 주는 (== url의 id)
    
    
def delete(request, id):
    board = Board.objects.get(id=id)
    if request.method == 'GET':
        context = {
            'board' : board,
        }
        return render(request, 'board/delete.html', context)
        
    elif request.method == 'POST':
        board.delete()
        return HttpResponseRedirect(reverse('board:list'))
    
    
def add(request):
    if request.method == "GET":
        return render(request, 'board/add.html')
    
    elif request.method == 'POST':
        add_title = request.POST['title']
        add_writer = request.POST['writer']
        add_content = request.POST['content']
        Board.objects.create(title=add_title, writer=add_writer, content=add_content)
        return HttpResponseRedirect(reverse('board:list'))