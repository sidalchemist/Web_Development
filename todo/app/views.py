from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Todo
from .forms import TodoForm
# Create your views here.


def todo_list(request):
    todo = Todo.objects.all()
    context = {
        "todo_list":todo   
    }

    return render(request,"listall.html",context)

def todo_details(request, id):
    todo = Todo.objects.get(id=id)
    context = {
        "todo":todo
    }
    return render(request,"todo_detail.html",context)

def todo_create(request):
    form = TodoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/')
        
    context = {'form': form}
    return render(request,"todo_create.html",context)

def todo_update(request, id):
    todo = Todo.objects.get(id=id)
    todo1 = Todo.objects.all()
    form = TodoForm(request.POST or None,instance=todo)
    if form.is_valid():
        form.save()
        return redirect('/')
        
    context = {'form': form,'todo':todo1}
    return render(request,"todo_update.html",context)
def todo_delete(request,id):
    todo = Todo.objects.get(id=id)
    todo.delete()
    return redirect('/')
    

