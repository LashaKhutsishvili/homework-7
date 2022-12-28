from django.http import HttpResponse
from django.shortcuts import render
from book.models import Book
from book.forms import CreateBookForm


def create_book(request):
    if request.method == "POST":
        form = CreateBookForm(request.POST)
        if form.is_valid():
            book_name = form.cleaned_data['name']
            book_author = form.cleaned_data['author']
            book = Book.objects.create(name=book_name, author=book_author)
            book.save()
            return HttpResponse('Book ' + book_name + "was created (Author - " + str(book_author)+")")
        form = CreateBookForm()
        return render(request, 'create_book.html', {'form': form})


