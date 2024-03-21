from django.shortcuts import render, redirect
from crudApp.models import UserCrud

def home(request):
    user_det = UserCrud.objects.all()
    return render(request, 'crudApp/index.html', context={'user': user_det})

def add(request):
    return render(request, 'crudApp/add.html')

def addrec(request):
    a = request.POST['first']
    b = request.POST['last']
    c = request.POST['country']
    user = UserCrud(firstname = a, lastname = b, country = c)
    user.save()
    return redirect('/')

def update(request, id):
    user_det = UserCrud.objects.get(id=id)
    return render(request, 'crudApp/update.html', context={'user': user_det})

def updaterec(request, id):
    a = request.POST['first']
    b = request.POST['last']
    c = request.POST['country']
    data = UserCrud.objects.get(id=id)
    data.firstname = a
    data.lastname = b
    data.country = c
    data.save()
    return redirect('/')

def delete(request, id):
    pk = UserCrud.objects.get(id=id)
    pk.delete()
    return redirect('/')