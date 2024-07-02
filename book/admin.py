from django.contrib import admin
from book.models import Author, Book, Comment

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Comment)
