from django.shortcuts import redirect, render
from .models import Post

def index(request):
    mem=Post.objects.all()
    return render(request,'index.html',{'mem':mem})

def add(request):
    return render(request,'add.html')

def addrec(request):
    x=request.POST['name surname']
    y=request.POST['title']
    z=request.POST['content']
    mem=Post(firstname=x,lastname=y,country=z)
    mem.save()
    return redirect("/")

def delete(request,id):
    mem=Post.objects.get(id=id)
    mem.delete()
    return redirect("/")

def update(request,id):
    mem=Post.objects.get(id=id)
    return render(request,'update.html',{'mem':mem})

def uprec(request,id):
    x=request.POST['name surname']
    y=request.POST['title']
    z=request.POST['content']
    mem=Post.objects.get(id=id)
    mem.firstname=x
    mem.lastname=y
    mem.country=z
    mem.save()
    return redirect("/")
