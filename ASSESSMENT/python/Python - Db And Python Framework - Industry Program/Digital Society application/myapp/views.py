from django.shortcuts import render,redirect
from .models import society_member,SocietyWatchmen,notice_board,Event,visitor,charman
from .forms import member_profile,watchman_form,notice_form,event_form,visitor_form,charman_form
from django.core.mail import send_mail
from functools import wraps
from django.contrib import messages

# Create your views here.

def login_required(function):
    @wraps(function)
    def wrapped_func(request,*args, **kwargs):
        if(request.COOKIES.get("Charmans") and request.COOKIES.get("role")) or (request.COOKIES.get("Member") and request.COOKIES.get("role") )or(request.COOKIES.get("Watcman") and request.COOKIES.get("role")):
            return function(request,*args, **kwargs)
        return wrapped_func
        
# @login_required
def home(request):
    total_member = society_member.objects.count()
    total_watchman = SocietyWatchmen.objects.count()
    total_notice = notice_board.objects.count()
    total_event = Event.objects.count()

    context={
        'total_member':total_member,
        'total_watchman':total_watchman,
        'total_notice':total_notice,
        'total_event':total_event
    }
    return render(request,'myapp/home.html',context)

def singup_view(request):
    return render(request,'myapp/singup.html')


def login_view(request):
    if request.method=="POST":
        username_=request.POST.get('username')
        password_=request.POST.get('password')
        try:
            get_member=society_member.objects.filter(member_id=username_).first()
            if get_member:
                if get_member.password==password_:
                    print(get_member.role)
                    response = redirect("home")
                    response.set_cookie('role',get_member.role)
                    response.set_cookie('member_id',get_member.member_id)
                    response.set_cookie('name',get_member.name)
                    return response
                else:
                    pass

            get_watchman= SocietyWatchmen.objects.filter(Watchmen_id=username_).first()
            if get_watchman:
                if get_watchman.password==password_:
                    response = redirect("home")
                    response.set_cookie('role',get_watchman.role)
                    response.set_cookie('Watchmen_id',get_watchman.Watchmen_id)
                    response.set_cookie('name',get_watchman.name)
                    return response
                else:
                    print("note")
            
            get_charmans =charman.objects.filter(charman_id=username_).first()
            if get_charmans:
                if get_charmans.password == password_:
                    print('song')
                    response = redirect("home")
                    response.set_cookie('role',get_charmans.role)
                    response.set_cookie('charman_id',get_charmans.charman_id)
                    response.set_cookie('name',get_charmans.name)
                    return response
                else:
                    print('hello')
                
            return redirect('login_view')
        
        except Exception as e:
            print(e)
            return redirect('login_view')

    return render(request,'myapp/loginview.html')

# @login_required
def logout(request):
    response = redirect('login_view')
    response.delete_cookie("role")
    response.delete_cookie("name")
    response.delete_cookie("charman_id")
    response.delete_cookie("Watchmen_id")
    response.delete_cookie("member_id")
    return response

# @login_required
def forgot_password_(request):
    if request.method=="POST":
        email_ =request.POST.get("email")
        try:
            get_charman=charman.objects.get(email = email_)
            subject = "your forgot password "
            message= f"""
            your login id and password is:
            login id :{get_charman.charman_id}
            password :{get_charman.password}
            """
            from_email ='harshlimbachiya0000@gmail.com'
            recipient_list = [f"{get_charman.email}"]

            send_mail(subject,message,from_email,recipient_list)
            return redirect("login_view")
        except charman.DoesNotExist:
            print("Eroor")
    return render(request,"myapp/forgot_password.html")

# @login_required
def change_password_(request):
    return render(request, "myapp/change_p.html")

# @login_required
def profile(request):
    if request.COOKIES.get("role") == "Charmans":
        data = charman.objects.get(charman_id = request.COOKIES.get('charman_id'))
        form = charman_form(instance=data)
        if request.method=="POST":
            form = charman_form(request.POST,instance=data)
            form.is_valid()
            form.save()
            return redirect("profile")
        else:
            form = charman_form(instance=data)
    elif request.COOKIES.get("role")== "Member":
        data = society_member.objects.get(member_id=request.COOKIES.get("member_id"))
        form = member_profile(instance=data)
        if request.method=="POST":
            form = member_profile(request.POST,instance=data)
            form.is_valid()
            form.save()
            return redirect("profile")
        else:
            form=member_profile(instance=data)
    elif request.COOKIES.get("role")=="Watcman":
        data = SocietyWatchmen.objects.get(Watchmen_id=request.COOKIES.get("Watchmen_id"))
        form = watchman_form(request.POST,instance=data)
        if request.method=="POST":
            form=watchman_form(request.POST,instance=data)
            form.is_valid()
            form.save()
            return redirect("profile")
        else:
            form=watchman_form(instance=data)
    context ={
        'data':data,
        'form':form
    }
    return render(request,'myapp/profil.html',context)

# @login_required
def member(request):
    member_data= society_member.objects.all()
    if request.method=="POST":
        form_member = member_profile(request.POST)
        if form_member.is_valid():
            form_member.save()
            return redirect('member')
    else:
        form_member=member_profile()
    
    if request.GET.get('search'):
        member_data= society_member.objects.filter(name__icontains=request.GET.get('search'))

    context = {
        'member_data':member_data,
        'form_member':form_member,
        'member_search':member_data
    }
    return render(request,'myapp/member.html',context)

# def add_member(request):
#     if request.method=="POST":
#         form_member = member_profile(request.POST)
#         if form_member.is_valid():
#             form_member.save()
#             return redirect()
#     else:
#         form_member=member_profile()
    
#     context={
#         'form_member':form_member
#     }
#     return render(request, 'myapp/member.html',context)

# @login_required
def delete_member(request,id):
    delete_ = society_member.objects.get(member_id=id)
    delete_.delete()
    return redirect('member')

# @login_required
def update_memberdata(request,id):
    data_ = society_member.objects.get(member_id=id)
    if request.method=="POST":
        form_member = member_profile(request.POST,instance=data_)
        form_member.save()
        return redirect('member')
    else:
        form_member=member_profile(instance=data_)
    context={
        'form_member':form_member
    }
    return render(request,'myapp/member.html',context)

# @login_required
def watchman_view(request):
    watchman_data = SocietyWatchmen.objects.all()
    if request.method=="POST":
        form_watchman = watchman_form(request.POST)
        if form_watchman.is_valid():
            form_watchman.save()
            return redirect("watchman_view")
    else:
        form_watchman = watchman_form()

    if request.GET.get('search'):
        watchman_data=SocietyWatchmen.objects.filter(name__icontains=request.GET.get('search'))

    context ={
        'watchman_data':watchman_data,
        'form_watchman':form_watchman,
        'wacthman_search':watchman_data
    }
    return render(request,'myapp/watchman.html',context)

# @login_required
def delete_watchman(request,id):
    delete_=SocietyWatchmen.objects.get(Watchmen_id=id)
    delete_.delete()
    return redirect('watchman_view')

# @login_required
def notice_view(request):
    notice_data= notice_board.objects.all()
    if request.method == "POST":
        form_notice = notice_form(request.POST,request.FILES)
        form_notice.is_valid()
        form_notice.save()
    else:
        form_notice = notice_form()
    if request.GET.get("search"):
        notice_data=notice_board.objects.filter(title__icontains=request.GET.get('search'))

    context={
        "notice_data":notice_data,
        'form_notice':form_notice
    }
    return render(request,'myapp/notice.html',context)

# @login_required
def events_view(request):
    event_data= Event.objects.all()
    if request.method=="POST":
        form_events = event_form(request.POST,request.FILES)
        form_events.is_valid()
        form_events.save()
    else:
        form_events = event_form()
    if request.GET.get("search"):
        event_data=Event.objects.filter(title__icontains=request.GET.get('search'))

    context={
        "event_data":event_data,
        "form_events":form_events
    }
    return render(request,'myapp/event.html',context)

# @login_required
def visitor_view(request):
    visitor_data = visitor.objects.all()
    if request.method=="POST":
        form_visitor = visitor_form(request.POST)
        form_visitor.is_valid()
        form_visitor.save()
    else:
        form_visitor=visitor_form()
    
    if request.GET.get('search'):
        visitor_data=visitor.objects.filter(name__icontains=request.GET.get('search'))

    context= {
        'visitor_data':visitor_data,
        'form_visitor':form_visitor,
        'visitor_search':visitor_data

    }
    return render(request,'myapp/visitor.html',context)