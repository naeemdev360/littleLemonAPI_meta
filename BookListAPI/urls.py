from django.urls import path
from . import views

urlpatterns = [
    # path('books',views.books),
    path('books',views.BookList.as_view()),
    path('books/<int:pk>',views.Book.as_view()),
    path('books2',views.books2),
    # path('books/get-books',views.books)
]
