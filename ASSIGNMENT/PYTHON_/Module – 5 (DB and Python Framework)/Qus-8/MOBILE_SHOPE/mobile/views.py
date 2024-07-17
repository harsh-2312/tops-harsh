from django.shortcuts import render,redirect
from .models import ProductCategory,singupdata
from .forms import mobileform,Brandform,Mobiledata
from functools import wraps
# Create your views here.

def login_required(funtion):
    @wraps(funtion)
    def wrapped(request,*args, **kwargs):
        if request.COOKIES.get("userid") and request.COOKIES.get("name"):
            return funtion(request,*args, **kwargs)
        else:
            return redirect('login')
    return wrapped

@login_required
def home(request):
    mobiledata= ProductCategory.objects.all()
    brand_ = Brandform()
    product =Mobiledata()

    if request.method == "POST":
        brand_ = Brandform(request.POST)
        if brand_.is_valid():
            brand_.save()
            return redirect('home')
    else:
        brand_ = Brandform()

    if request.method == "POST":
        product =Mobiledata(request.POST,request.FILES)
        if product.is_valid():
            product.save()
            return redirect('home')
    else:
        product = Mobiledata()

    if request.GET.get('search'):  #for search
        mobiledata = ProductCategory.objects.filter(model_name__icontains=request.GET.get('search'))
    context = {
        'mobile_deta' : mobiledata,
        'brand_data':brand_,
        'add_product':product,
    }
    return render(request,'mobile/home.html',context)

@login_required
def add_data(request):
    if request.method == "POST":
        form = mobileform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
            return redirect('home')
    else:
        form = mobileform()
    
    context = {
        'form': form
    }
    return render(request, 'mobile/add_data.html', context)

@login_required
def delete_data(request,id):
    delete_ = ProductCategory.objects.get(product_id=id)
    delete_.delete()
    return redirect('home')

@login_required
def update_data(request,id):
    data = ProductCategory.objects.get(product_id=id)
    if request.method == 'POST':
        form = mobileform(request.POST, instance=data)
        form.save()
        return redirect('home')
    else:
        form = mobileform(instance=data)
    
    context = {
        'form': form
    }
    return render(request, 'mobile/add_data.html', context)

def singup(request):
    if request.method=="POST":
        name_ = request.POST.get('name')
        number_ = request.POST.get('number')
        email_ = request.POST.get('email')

        singup_data = singupdata(
            name = name_,
            mobile = number_,
            email = email_,
        )
        singup_data.save()
        return redirect('login')
    return render(request,'mobile/singup.html')

def login(request):
    msg = ''
    if request.method=="POST":
        user_id_= request.POST.get('Username')
        password_ = request.POST.get('password')
        get_data= singupdata.objects.get(user_id=user_id_)
        if get_data.password==password_:
            respons = redirect('home') 
            respons.set_cookie('userid',get_data.user_id)
            respons.set_cookie('name',get_data.name)
            return respons
        else:
            msg = 'error'
    context = {
        'msg' : msg
    } 
    return render(request,'mobile/login.html',context)

@login_required
def logout(request):
    respons= redirect('login')
    respons.delete_cookie('userid')
    respons.delete_cookie("name")
    return respons