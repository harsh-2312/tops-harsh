from django.urls import path
from . import views

urlpatterns = [
    path('',views.employee_login_view,name='employee_login_view'),
    path('dasboard/',views.employee_dashboard,name='employee_dashboard'),
    path('student-view/',views.student_view,name='student_view'),
    path("employee-profile/",views.employee_profile_view,name='employee_profile_view'),
    path('logout/',views.employee_logout,name='employee_logout'),
    path('chengepassword/',views.chenge_password,name='chenge_password'),
    path('add_student/',views.add_student,name='add_student'),
    path('delet-student/<student_id>/',views.delete_student,name='delete_student'),
    path('update/<student_id>',views.update_student,name='update_student'),
    path('batch-view/',views.Batch_view,name="Batch_view"),
    path('student-profile/<student_id>/',views.student_profile_view,name='student_profile_view'),
    path('student-payment/',views.student_payment_entry,name='student_payment_entry'),
    path('batch-action/<str:batch_id>/',views.batch_action_view,name="batch_action_view"),
    path('mybatch/',views.mybatchView,name="mybatchView"),
    path('add-global-note/',views.add_global_note,name="add_global_note"),
    path('update-global-none/',views.update_global_note,name="update_global_note"),
    path('delete-globale-note/<str:note_id>/',views.delete_global_note,name="delete_global_note"),
]