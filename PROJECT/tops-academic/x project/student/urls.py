
from django.urls import path,include
from . import views

urlpatterns = [
    path('stdent-login',views.student_login_view)
    
]