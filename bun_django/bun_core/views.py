from django.shortcuts import render,redirect
from django.http import HttpResponse
from bun_core.models import bunbase
# Create your views here.

def home(request):
    return render(request, 'home.html', {"title":"hello world"})

def news(request):
    content=bunbase.objects.all()
    # print(bunbase.objects.get(id=1).time)
    return render(request, "news.html",{"title":"News","content":content})

def about(request):
    return render(request, "about.html")

def test(request):
    
    return render(request,"test.html",{"class":bunbase.objects.get(id=3)})

def create_(request):
    if request.method=="POST":
        title=request.POST.get("title")
        desc=request.POST.get("description")
        is_active=request.POST.get("is_active")
        image=request.FILES.get('image')
        # print(bunbase.objects.get(id=3).image.name)
        bunbase.objects.create(title=title,description=desc,is_active=is_active,image=image)
        return redirect('home')

    return render(request, "main.html",{"agree":"yes"})

def delete_(request,id):
    bunbase.objects.get(id=id).delete()
    return redirect("news")