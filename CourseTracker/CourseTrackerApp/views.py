from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.core.mail import send_mail
from django.forms import ModelForm

# Create your views here.
def about_us(request):
    return render(request, 'CourseTrackerApp/about_us.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/login')

        else:
            messages.info(request, "Invalid Credentials")
            return redirect('/login')

    else:
        return render(request, 'CourseTrackerApp/login.html')

def signin(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Is Taken')
                return redirect('/signin')

            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email id already exists')
                return redirect('/signin')

            else:
                user = User.objects.create_user(username=username, email=email, password=password1, first_name=first_name, last_name=last_name)
                user.save()

        else:
            print("not matching passwords")
            return redirect('/signin')

        message = "Hello "+username+" You have succesfully registered on our site!.\n Welcome to the community"
        print("User created")

        send_mail('You have registered on our website!',
                  message,
                  'tambetejashree123@gmail.com',
                  [email],
                  fail_silently=False)
        print("Mail Sent!")

        return redirect('/')

    else:
        return render(request, 'CourseTrackerApp/signin.html')
