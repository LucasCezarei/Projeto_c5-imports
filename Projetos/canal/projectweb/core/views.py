from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Roupas


# Create your views here.
@login_required(login_url='/login/')
def register_roupas(request):
    roupas_id = request.GET.get('id')
    if roupas_id:
        roupas = Roupas.objects.get(id=roupas_id)
        if roupas.user == request.user:
            return render(request, 'register-roupas.html', {'roupas':roupas})
    return render (request, 'register-roupas.html')

#Cadastrar roupas
@login_required(login_url='/login/')
def set_roupas(request):
    marca = request.POST.get('marca')
    descricao = request.POST.get('descricao')
    telefone = request.POST.get('telefone')
    email = request.POST.get('email')
    file = request.FILES.get('file')
    user = request.user
    roupas_id = request.POST.get('roupas_id')
    if roupas_id:
        roupas = Roupas.objects.get(id=roupas_id)
        if user == roupas.user:
            roupas.email = email
            roupas.telefone = telefone
            roupas.marca = marca
            roupas.descricao = descricao 
            if file:
                roupas.photo = file
            roupas.save()
    else:
        roupas = Roupas.objects.create(email=email, telefone=telefone, marca=marca, descricao=descricao,
                                user=user, photo=file)
    url = '/roupas/detail/{}/'.format(roupas.id)
    return redirect(url)

#Delete da roupa
@login_required(login_url='/login/')
def delete_roupas(request, id):
    roupas = Roupas.objects.get(id=id)
    if roupas.user == request.user:
        roupas.delete()
    return redirect('/')

#Cadastro das roupas 
@login_required(login_url='/login/')
def list_all_roupas(request):
    roupas = Roupas.objects.filter(active=True)
    return render(request, 'list.html', {'roupas':roupas})

#Listagem da roupa do usuario
def list_user_roupas(request):
    roupas = Roupas.objects.filter(active=True, user=request.user)
    return render(request, 'list.html', {'roupas':roupas})

#Detalhe das roupas 
def roupas_detail(request, id):
    roupas=Roupas.objects.get(active=True, id=id)
    return render(request, 'roupas.html', {'roupas':roupas})

#Saida do Usuario
def logout_user(request):
    print(request.user)
    logout(request)
    return redirect('/login/')


#Requi do usuario
def login_user(request):
    return render(request, 'login.html')

#Verificador do login
@csrf_protect
def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Usuario e senha invalidos')
            return redirect ('/login/')

