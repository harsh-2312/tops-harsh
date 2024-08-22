from django.shortcuts import render,redirect
from .models import Employee,Batch,Technology 
from .models import AssignBatch
from django.contrib import messages
from student.forms import studentform
from student.models import Student,StudentProfile,StudentAddress,StudentCourse,StudentPayment,StudentPaymentEntry

from functools import wraps
from django.urls import reverse
from decimal import Decimal
import requests

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
    total_student = Student.objects.count()
    

    context ={
        'total_student':total_student
    }
    return render(request,"employee/employee_dashboard.html",context)

@login_required
def employee_profile_view(request):

    return render(request,"employee/profile.html")

@login_required
def Batch_view(request):
    batches = Batch.objects.all()
    get_student= AssignBatch.objects.all()
    context = {
        "batches":batches,
        "get_student":get_student
    }
    return render(request,"employee/batch_view.html",context)

#  if request.COOKIES.get('role') == 'counsellor':
#         batches = Batch.objects.all()
#     elif request.COOKIES.get('role') == '':
#         get_employee = Employee.objects.get(faculty_id = request.COOKIES.get("employee_id"))
#         batches = Batch.objects.filter(faculty_id_id = get_employee.employee_id)
#     get_student = AssignBatch.objects.all()
#     context = {
#         'batches' : batches,
#         'students' : get_student
#     }
#     return render(request,"employee/employee_batch_view.html",context)


@login_required
def student_view(request):
    students_objects = Student.objects.all()
    if request.method =="POST":
        student_form = studentform(request.POST)
        student_form.is_valid()
        student_form.save()
        return redirect("student_view")
    else:
        student_form = studentform()

    if request.GET.get("search"):
        students_objects = Student.objects.filter(student_id__icontains = request.GET.get("search"))
    context = {
        "student" : students_objects,
        "student_form": student_form,
    }
    return render(request,"employee/student_view.html",context)

@login_required
def student_profile_view(request,student_id):
    context = {}

    try:
        student_data = Student.objects.get(student_id=student_id)
        context["student_data"] = student_data
    except Student.DoesNotExist:
        context['student'] = {
            'status_code' : 404,
            'message' : 'student data not found'
        }
    try:
        student_profile = StudentProfile.objects.get(student_id_id =student_id)
        context['student_profile'] = student_profile
    except StudentProfile.DoesNotExist:
        context['student_profile'] = {
            'status_code' : 404,
            'message' : 'student profile not found'
        }
    try:
        student_address = StudentAddress.objects.get(student_id_id = student_id)
        context['student_address'] = student_address
    except StudentAddress.DoesNotExist:
        context['student_address'] = {
            'status_code' : 404,
            'message' : 'student address not found'
        }
    try:
        student_course = StudentCourse.objects.get(student_id_id = student_id)
        context['student_course'] = student_course
    except StudentCourse.DoesNotExist:
        context['student_course'] = {
            'status_code' : 404,
            'message' : 'student course not found'
        }
    try:
        student_payment = StudentPayment.objects.get(student_id_id = student_id)
        context['student_payment'] = student_payment
    except StudentPayment.DoesNotExist:
        context['student_payment'] = {
            'status_code' : 404,
            'message' : 'student payment not found'
        }
    try:
        student_payment_entry = StudentPaymentEntry.objects.filter(student_id_id = student_id)
        context['student_payment_entry'] = student_payment_entry
    except StudentPayment.DoesNotExist:
        context['student_payment_entry'] = {
            'status_code' : 404,
            'message' : 'student payment entry not found'
        }
    return render(request,"employee/student_profile_view.html",context)

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

def update_student(request,id):
    data = Student.objects.get(student_id=id)
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

def student_payment_entry(request):
    
    if request.method=="POST":
        student_id_ = request.POST.get('student_id')
        proof_ = request.FILES.get('proof')
        paid_date_ = request.POST.get('date')
        installment_ = request.POST.get('installment')
        print('********')
        print(student_id_)

        student_payment_object = StudentPayment.objects.get(student_id_id=student_id_)
        print(student_payment_object)
        if Decimal(installment_) > student_payment_object.remaining_fees:
            messages.error(request,"payment should be less or equal to remaining fees")

        StudentPaymentEntry.objects.create(
            student_id_id = student_id_,
            proof = proof_,
            paid_date = paid_date_,
            installment = Decimal(installment_)
        )
        messages.success(request,f"{installment_} Rs. Payment Added to {student_id_} Account")
        return redirect(reverse("student_profile_view" ,args=[student_id_]))

def batch_action_view(request,batch_id):
    batch= Batch.objects.get(batch_id=batch_id)
    get_student= AssignBatch.objects.filter(batch_id=batch_id)
    context = {
        "batch":batch,
        "students":get_student
    }
    url = "http://127.0.0.1:4000/notslist/"
    response = requests.get(url)
    print(response)
    # student_notes = {}  
    if response.status_code==200:
        # print(response.json())
        for data in response.json()["data"]:
            print(data["student_id"])
    return render(request ,"employee/batch_action.html" ,context)

def mybatchView(request):
    mybatch= Batch.objects.get(faculty_id_id = request.COOKIES.get("employee_id"))
    students = AssignBatch.objects.filter(batch_id_id = mybatch.batch_id)
    student_notes = []
    for student in students:
        url = f"http://127.0.0.1:4000/student/{student.student_id_id}"
        response = requests.get(url)
        if response.status_code==200:
            for data in response.json()["data"]:
                print(response.json()["data"])
                student_notes.append(data)
    notes = sorted(student_notes,key=lambda x : x["created_at"])[::-1]
    print(student_notes)
    context = {
        'mybatch':mybatch,
        'students':students,
        'notes' : notes
    }
    return render(request,"employee/my_batch.html",context)


def add_global_note(request):
    if request.method=="POST":
        student_id_ = request.POST.get("student_id")
        comment_ = request.POST.get("comment")
        data = {
            "student_id" : student_id_,
            "comment" : comment_
        }
        url = "http://127.0.0.1:4000/notslist/"
        response = requests.post(url,data=data)
        print(response.status_code)
        if response.status_code==201:
            messages.success(request,f"Globalnote added for {student_id_}")
        else:
            messages.error(request,response.json()["error"])
    
    return redirect("mybatchView")


def update_global_note(request):
    if request.method=="POST":
        note_id_ = request.POST.get("note_id")
        comment_ = request.POST.get("comment")
        url =f" http://127.0.0.1:4000/nots/{note_id_}/"
        data = {
            "comment":comment_,
        }
        response = requests.patch(url,data=data)
        if response.status_code==202:
            messages.success(request,f"Global Note Updated Successfully of {response.json()["data"]["student_id"]}")
        else:
            messages.error(request,f"{response.json()["massege"]}")
    return redirect("mybatchView")

def delete_global_note(request,note_id):
    url =f" http://127.0.0.1:4000/nots/{note_id}/"
    response = requests.delete(url)
    if response.status_code==204:
        messages.success(request,"Global Note Deleted Successfully")
    else:
        messages.error(request,response.json()["message"])
    
    return redirect("mybatchView")



