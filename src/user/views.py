from email import message
from django.shortcuts import render, redirect
from .forms import UserCreationForm, LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from blog.models import Post


def register(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'تهانينا {username} لقد تمت عملية التسجيل بنجاح')
            return redirect('home')
    else:
        form = UserCreationForm()


    return render(request, 'user/register.html',{
        'title':'التسجيل',
        'form' :form,
    })


def login_user(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.warning(request,'هناك خطأ في اسم المستخدم وكلمة المرور.')

    return render(request, 'user/login.html',{
        'title':'تسجيل الدخول',
    })

def logout_user(request):
    logout(request)
    return render(request, 'user/logout.html',{
            'title':'تسجيل الخروج',
        })


def profile(request):
    posts = Post.objects.filter(author =request.user)

    return render(request, 'user/profile.html', {
        'title': 'الملف الشخصي',
        'posts': posts,
    })
   