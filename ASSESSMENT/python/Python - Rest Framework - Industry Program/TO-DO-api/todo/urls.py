from django.urls import path,include

from . import views

urlpatterns = [
    path("tasks/",views.task_list,name='task_list'),
    path('task/<int:id>/',views.task_details)
]