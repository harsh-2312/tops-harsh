from django.urls import path,include
from . import views

urlpatterns = [
    path('home',views.home,name='home'),
    path('',views.login_view,name='login_view'),
    path('logout/',views.logout,name='logout'),
    # path('singup',views.singup_view,name='singup_view'),
    path('profil/',views.profile,name='profile'),
    path('member/',views.member,name='member'),
    path('delete-member/<id>/',views.delete_member,name='delete_member'),
    # path('update-member/<id>/',views.update_memberdata,name='update_memberdata'),
    path('watchmanview/',views.watchman_view,name="watchman_view"),
    path('watchman-deleted/<id>/',views.delete_watchman,name='delete_watchman'),
    path('notice-view',views.notice_view,name='notice_view'),
    path('event-view/',views.events_view,name="events_view"),
    path('visitor-view',views.visitor_view,name='visitor_view'),
    path('forgot-password/',views.forgot_password_,name='forgot_password_'),
    # path('changepassword/',views.change_password_,name='change_password_'),
]