from django.urls import path
from . import views

urlpatterns = [
    path('',views.employee_login_view,name='employee_login_view'),
    path('dasboard/',views.employee_dashboard,name='employee_dashboard'),
    path('logout/',views.employee_logout,name='employee_logout'),
    path('chengepassword/',views.chenge_password,name='chenge_password'),
    path('add_student/',views.add_student,name='add_student'),
    path('delet-student/<student_id>/',views.delete_student,name='delete_student'),
    path('update/<student_id>',views.update_student,name='update_student'),
]