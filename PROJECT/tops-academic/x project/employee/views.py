from django.shortcuts import render,redirect
from .models import Employee,Student
from django.contrib import messages
from .forms import studentform

from functools import wraps

def login_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.COOKIES.get('employee_id'):
            return view_func(request,*args, **kwargs)
        else:
            return redirect("employee_login_view")
    return _wrapped_view


def employee_login_view(request):
    if request.method == 'POST':
        employee_id_ = request.POST['employee_id']              
        password_ = request.POST['password']
        try:
            get_employee = Employee.objects.get(employee_id=employee_id_)
            if get_employee.password == password_:
                messages.success(request,"You are logged in")
                response = redirect("employee_dashboard")
                response.set_cookie('employee_id', get_employee.employee_id)
                response.set_cookie('employee_name', f'{get_employee.first_name} {get_employee.last_name}')
                response.set_cookie('role',get_employee.role.name)
                return response
            else:
                messages.error(request, 'Employee ID or Password does not match.')
                return redirect('employee_login_view')
        except Employee.DoesNotExist:
            messages.error(request, 'Employee does not exist.')
            return redirect('employee_login_view')
        except Exception as err:
            messages.error(request, f'ERROR : {err}')
            return redirect('employee_login_view')
        
    return render(request,'employee/employee_login.html')


@login_required
def employee_dashboard(request):
    students_objects = Student.objects.all()

    context = {
        "student" : students_objects
    }
    return render(request,"employee/employee_dashboard.html",context)

@login_required
def employee_logout(request):
    response = redirect('employee_login_view')
    response.delete_cookie('employee_id')
    response.delete_cookie('employee_name')
    messages.success(request,'You have successfully logged out.')
    return response

@login_required
def chenge_password(request):   
    employee_id_ = request.COOKIES.get('employee_id')
    get_employee = Employee.objects.get(employee_id=employee_id_)
    if request.method=="POST":
        old_password =request.POST["old Password"]
        new_password =request.POST["New Password"]
        confirm_Password=request.POST["Confirm Password"]

        if old_password != get_employee.password:
            messages.error(request,'old password incorrect')
            return redirect('chenge_password')
        
        if new_password != confirm_Password:
            messages.error(request,'new and confirm password not match')
            return redirect('chenge_password')
        
        if old_password == new_password:
            messages.error(request,'new and old password same')
            return redirect('chenge_password')
        
        get_employee.password = new_password
        get_employee.save()

        response = redirect('employee_login_view')
        response.set_cookie('employee_id',get_employee.employee_id)
        response.set_cookie('password',get_employee.password)

        messages.success(request, 'password has been updated successfully')
        return redirect('employee_login_view')

    return render(request,'employee/change_password.html')

@login_required
def add_student(request):
    if request.method=="POST":
        form = studentform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_dashboard')
        
    else:
        form = studentform()

    context ={

        'form' : form
    }
    messages.success(request, 'student add')
    return render(request, 'employee/add_employee.html',context)

def delete_student(request,student_id):
    data = Student.objects.get(id=student_id)
    data.delete()
    messages.success(request, 'student deleted')
    return redirect('employee_dashboard')

def update_student(request, student_id):
    data = Student.objects.get(id=student_id)
    if request.method=="POST":
        form = studentform(request.POST,instance=data)
        form.save()
        return redirect("employee_dashboard")
    else:
        form = studentform(instance=data)

    context = {
        'form' : form
    }
    messages.success(request, 'student data updated')
    return render(request ,'employee/add_employee.html',context)
