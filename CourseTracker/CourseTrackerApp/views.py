from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.core.mail import send_mail
from django.core.files.storage import FileSystemStorage
from django.forms import ModelForm

# Create your views here.
from django.shortcuts import render, HttpResponse, redirect
from .models import Student_Signin, Teacher_Signin, Upload_Files

def homepage(request):
    return render(request, 'CourseTrackerApp/homepage.html')

def student_videolecture(request):
    all_files = Upload_Files.objects.all()
    return render(request, 'CourseTrackerApp/student_videolecture.html', {"files":all_files})

def student_branches(request):
    return render(request, 'CourseTrackerApp/student_branches.html')

def teacher_branches(request):
    return render(request, 'CourseTrackerApp/teacher_branches.html')

def search(request):
    search_term = request.GET['search_term']
    all_files = Upload_Files.objects.filter(topic_name__icontains=search_term)
    return render(request, 'CourseTrackerApp/student_lectures_list.html', {'all_files': all_files})

def student_subjects(request):
    return render(request, 'CourseTrackerApp/student_subjects.html')

def student_sem(request):
    return render(request, 'CourseTrackerApp/student_sem.html')

def teacher_subjects(request):
    return render(request, 'CourseTrackerApp/teacher_subjects.html')

def teacher_sem(request):
    return render(request, 'CourseTrackerApp/teacher_sem.html')

def student_lectures_list(request):
    files = Upload_Files.objects.all()
    return render(request, 'CourseTrackerApp/student_lectures_list.html', {"files": files})

def teachers_lectures_list(request):
    files = Upload_Files.objects.all()
    return render(request, 'CourseTrackerApp/teachers_lectures_list.html', {"files": files})

def teacher_videolecture(request):
    files = Upload_Files.objects.all()
    if request.method == "POST":
        lecture_no = request.POST['lecture_no']
        topic_name = request.POST['topic_name']
        video_file = request.FILES['video_file']
        notes_file = request.FILES['notes_file']

        if Upload_Files.objects.filter(lecture_no=lecture_no).exists():
            messages.info(request, 'Lecture Is Already Uploaded')
            return redirect('/teacher_videolecture')

        elif Upload_Files.objects.filter(topic_name=topic_name).exists():
            messages.info(request, 'Topic Exists Already')
            return redirect('/teacher_videolecture')

        elif Upload_Files.objects.filter(video_file=video_file).exists():
            messages.info(request, 'Video File Exists Already')
            return redirect('/teacher_videolecture')

        elif Upload_Files.objects.filter(notes_file=notes_file).exists():
            messages.info(request, 'Notes Are Uploaded Already')
            return redirect('/teacher_videolecture')

        else:
            file = Upload_Files.objects.create(lecture_no=lecture_no, topic_name=topic_name, video_file=video_file, notes_file=notes_file)

            file.save()
            return redirect('/confirm')

    return render(request, 'CourseTrackerApp/teacher_videolecture.html', {"files":files})

def confirm(request):
    return render(request, 'CourseTrackerApp/confirm.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def student_login(request):
    student = Student_Signin.objects.all()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        if Student_Signin.objects.filter(username=username, password1=password):
            return redirect('/student_branches')

        else:
            messages.info(request, "Invalid Credentials")
            return redirect('/student_login')

    else:
        return render(request, 'CourseTrackerApp/student_login.html', {"student": student})

def student_signin(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1 == password2:
            if Student_Signin.objects.filter(username=username).exists():
                messages.info(request, 'Username Is Taken')
                return redirect('/student_signin')

            elif Student_Signin.objects.filter(email=email).exists():
                messages.info(request, 'Email id already exists')
                return redirect('/student_signin')

            else:
                student = Student_Signin.objects.create(username=username, email=email, password1=password1, password2=password2, first_name=first_name, last_name=last_name)
                student.save()

        else:
            print("not matching passwords")
            return redirect('/student_signin')

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
        return render(request, 'CourseTrackerApp/student_signin.html')

def teacher_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        if Teacher_Signin.objects.filter(username=username, password1=password):
            teacher = Teacher_Signin.objects.get(username=username)
            return redirect('/teacher_branches')

        else:
            messages.info(request, "Invalid Credentials")
            return redirect('/teacher_login')

    else:
        return render(request, 'CourseTrackerApp/teacher_login.html')

def teacher_signin(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1 == password2:
            if Teacher_Signin.objects.filter(email=email).exists():
                messages.info(request, 'Email id already exists')
                return redirect('/teacher_signin')

            else:
                teacher = Teacher_Signin.objects.create(username=username, email=email, password1=password1,
                                                        password2=password2, first_name=first_name, last_name=last_name)
                teacher.save()

        else:
            print("not matching passwords")
            return redirect('/teacher_signin')

        message = "Hello " + username + " You have succesfully registered on our site!.\n Welcome to the community"
        print("User created")

        send_mail('You have registered on our website!',
                  message,
                  'tambetejashree123@gmail.com',
                  [email],
                  fail_silently=False)
        print("Mail Sent!")

        return redirect('/teacher_branches')

    else:
        return render(request, 'CourseTrackerApp/teacher_signin.html')
