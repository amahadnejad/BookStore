from django.views import generic
from django.urls import reverse_lazy

from .models import Book
from .forms import BookForm


class BookListView(generic.ListView):
    model = Book
    template_name = "books/book_list.html"


class BookDetailView(generic.DetailView):
    model = Book
    context_object_name = 'book'
    template_name = 'Books/book_detail.html'


class BookCreateView(generic.CreateView):
    model = Book
    form_class = BookForm
    template_name = 'books/book_create.html'


class BookUpdateView(generic.UpdateView):
    model = Book
    fields = ['title', 'author', 'description', 'price', ]
    template_name = "books/book_update.html"
