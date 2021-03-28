from django.db import models
# from .validators import notes_file_size, videos_file_size, password_size
# from .validators import password_size
# Create your models here.

class Student_Signin(models.Model):
    username = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    password1 = models.CharField(max_length=50)
    password2 = models.CharField(max_length=50)
    def __str__(self):
        return self.username

class Teacher_Signin(models.Model):
    username = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    password1 = models.CharField(max_length=50)
    password2 = models.CharField(max_length=50)
    def __str__(self):
        return self.username

class Upload_Files(models.Model):
    lecture_no = models.IntegerField()
    topic_name = models.CharField(max_length=200)
    video_file = models.FileField(upload_to="videos/")
    notes_file = models.FileField(upload_to="notes/")
