from django.conf.urls import url,include
from django.urls import path
from . import views

app_name = 'books'
urlpatterns = [
    path('', views.BookList.as_view(), name='book_list'),
    path('book_create', views.CreateBook.as_view(), name='book_create'),
    path('update/<int:pk>', views.EditBook.as_view(), name='book_update'),
    path('delete/<int:pk>', views.BookDelete.as_view(), name='book_delete'),
    path('book/<int:pk>', views.BookDetail.as_view(), name='book_detail'),

]
