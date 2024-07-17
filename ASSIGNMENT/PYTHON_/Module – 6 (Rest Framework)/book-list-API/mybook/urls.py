from django.urls import path,include
from . import views
urlpatterns = [
    path('books/', views.booklist, name='booklist'),
    path('book/<int:book_id>/',views.book_details,name='book_details')
]
