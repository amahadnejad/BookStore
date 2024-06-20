from django.views import generic

from .models import Book


class BookListView(generic.ListView):
    model = Book
    template_name = "books/book_list.html"


class BookDetailView(generic.DetailView):
    model = Book
    context_object_name = 'book'
    template_name = 'Books/book_detail.html'
