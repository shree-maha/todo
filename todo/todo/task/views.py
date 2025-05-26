from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import *
# Create your views here.
def index(request):
    tasks = task.objects.all()  # Capital 'T' in Task

    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('index')  # Use 'index' as the URL name for redirect
    context = {'tasks': tasks, 'form': form}
    return render(request, "list.html", context)
def update(request,pk):
    tasks=task.objects.get(id=pk)
    form=TaskForm(instance=tasks)
    if request.method=="POST":
        form=TaskForm(request.POST,instance=tasks)
        if form.is_valid():
            form.save()
        return redirect("index")
        
    context={'form':form}
    return render(request,"update.html",context)
def delete(request,pk):
    item=task.objects.get(id=pk)
    if request.method=="POST":
        item.delete()
        return redirect("index")
    context={'item':item}
    return render(request,"delete.html",context)