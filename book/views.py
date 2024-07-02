from django.shortcuts import render
from book.models import Book


def home(request):
    return render(request, 'home.html')


def books(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'books.html', context=context)


def author(request):
    return render(request, 'author.html')
