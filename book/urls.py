from django.urls import path
from book.views import home, books, author
urlpatterns = [
    path('', home, name='home'),
    path("books/", books, name='books'),
]
