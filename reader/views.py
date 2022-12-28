from django.http import HttpResponse
from django.shortcuts import render


from book.models import Book
from reader.forms import CreateReaderForm
from reader.models import Reader


def create_reader(request):
    if request.method == 'POST':
        form = CreateReaderForm(request.POST)
        if form.is_valid():
            reader_name = form.cleaned_data['name']
            reader_lastname = form.cleaned_data['lastname']
            reader = Reader.objects.create(name=reader_name, lastname=reader_lastname)
            reader.save()
            if reader_name != "" and reader_lastname != "":
                book = Book.objects.all()[len(Book.objects.all())-1]
                return HttpResponse('last added book: ' + book.name + ", Author: " + book.author)
        form = CreateReaderForm()
        return render(request, 'create_reader.html', {'form': form})

