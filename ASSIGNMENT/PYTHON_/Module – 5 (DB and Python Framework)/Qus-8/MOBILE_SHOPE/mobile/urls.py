from django.urls import path
from . import views

urlpatterns = [
    path('home',views.home,name='home'),
    path('add-data/',views.add_data,name='add_data'),
    path('delete/<id>/',views.delete_data,name='delete_data'),
    path('update/<id>/',views.update_data,name='update_data'),
    path('login/',views.login,name='login'),
    path('',views.singup,name='singup'),
    path('logout/',views.logout,name='logout'),
]






