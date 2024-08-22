from django.shortcuts import render

# Create your views here.

def student_login_view(request):
    return render(request,'student/student_login.html')
