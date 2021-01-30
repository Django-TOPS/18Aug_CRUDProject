from django.shortcuts import render,HttpResponse,redirect
from .models import Student
from .forms import StudentForm

# Create your views here.

def indexpage(request):
    #data={'stdata':Student.objects.all}
    if request.method=='POST':
        stfrm=StudentForm(request.POST)
        if stfrm.is_valid():
            stfrm.save()
        else:
            print(stfrm.errors)
    else:
        stfrm=StudentForm()
    return render(request,'index.html',{'stdata':Student.objects.all,'stfrm':stfrm})

def update(request,id):
    if request.method=='POST':
        stfrm=StudentForm(request.POST)
        id=Student.objects.get(id=id)
        if stfrm.is_valid():
            stfrm=StudentForm(request.POST, instance=id)
            stfrm.save()
            return redirect('index')
        else:
            print(stfrm.errors)
    else:
        stfrm=StudentForm()
    return render(request,'update.html',{'stfrm':stfrm,'stdata':Student.objects.get(id=id)})
    
def delete(request,id):
    id=Student.objects.get(id=id)
    id.delete()
    return redirect('index')
