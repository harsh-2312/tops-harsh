from django.contrib import admin
from django.urls import path,include
from  . import views

urlpatterns = [
    path('notslist/',views.globalenotelist),
    path('nots/<str:id>/',views.globaleNotesDetails),
    path('student/<str:student_id>/',views.studentglobelnote)
]