from django.shortcuts import render
from django.http import JsonResponse
from django.template.loader import render_to_string
from .forms import BookForm
from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import BookForm
from .models import Book

from django.views.generic.edit import FormView

# Create your views here.

from .models import Book

def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})

class CreateBook(FormView):
    template_name = 'create.html'
    form_class = BookForm
    success_url = reverse_lazy('books:book_list')

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.save()
        return super().form_valid(form)
class EditBook(UpdateView):
    model = Book 
    fields = '__all__'
    success_url = reverse_lazy('books:book_list')
    
class BookList(ListView):
    template_name = 'book_list.html'
    model = Book



class BookDetail(DetailView):
    model = Book


# class ContactCreate(CreateView):
#     model = Contact
#     fields = '__all__'
#     success_url = reverse_lazy('contact_list')


# class ContactUpdate(UpdateView):
#     model = Contact
#     fields = '__all__'
#     success_url = reverse_lazy('contact_list')


class BookDelete(DeleteView):
    model = Book
    success_url = reverse_lazy('books:book_list')

