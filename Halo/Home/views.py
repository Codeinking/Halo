from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
# Create your views here.
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'index.html')






def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']


        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return redirect('signup')
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('signup')
            else:
                user = User.objects.create_user( username=username,  password=password1, email=email,
                                                )
                user.save();
                return redirect('login')


        else:
            messages.info(request, 'Password Not Matching')
            return redirect('signup')
        return redirect('/')

    else:
        return render(request, 'signup.html')


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(email=email, password=password)

        if user is not None:
            auth.login(request, user)
            username = user.username
            return render(request, '/')
        else:
            messages.info(request, 'invalid credential')
            return redirect('login')


    else:
        return render(request, 'login.html')

