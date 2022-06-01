from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils import timezone
from .models import board
from .forms import boardForm, boardModelForm
from django.shortcuts import render,redirect, get_object_or_404


def index(request):
    return HttpResponse("Hello, World")

#보드의 홈 화면
def home(request):
    posts = board.objects.all()

    return render(request, 'polls/board.html', {'posts': posts})

#새 보드 작성
def new(request):
    return render(request, 'polls/new.html')

def create(request):
    if request.method == 'POST':
        post = board()
        post.title = request.POST['title']
        post.body = request.POST['body']
        post.date = timezone.now()
        post.save()
    return redirect('home')

def formcreate(request):
    if request.method == 'POST':
        form = boardForm(request.POST)
        if form.is_valid():
            post = board()
            post.title = form.cleaned_data['title']
            post.body = form.cleaned_data['body']
            post.save()
            return redirect('home')
    else:
        form = boardForm()
    return render(request, 'polls/form_create.html', {'form':form})

def modelformcreate(request):
    if request.method == 'POST' or request.method == 'FILES':
        form = boardModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = boardModelForm()
        return render(request, 'polls/form_create.html', {'form':form})

def detail(request, board_id):
    board_detail = get_object_or_404(board, pk=board_id)

    return render(request, 'polls/detail.html', {'board_detail':board_detail})

def delete(request, board_id):
    board_detail = board.objects.get(pk = board_id)
    board.delete(board_detail)
    return redirect('home')
