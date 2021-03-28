from django.contrib import admin

# Register your models here.
from .models import Student_Signin, Teacher_Signin, Upload_Files
admin.site.register(Upload_Files),
admin.site.register(Student_Signin),
admin.site.register(Teacher_Signin),

