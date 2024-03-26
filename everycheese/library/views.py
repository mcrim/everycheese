from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

from django.views.generic import CreateView
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Library#, Author

class LibraryListView(ListView):
    model = Library



class LibraryDetailView(DetailView):
    model = Library

class LibraryCreateView(LoginRequiredMixin, CreateView):
    model = Library
    fields = [
        'book_name',
        'description',
        'genre',
        'author_firstname',
        'author_lastname',
    ]
    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)
    
class LibraryUpdateView(LoginRequiredMixin, UpdateView):
    model = Library
    fields = [
        'book_name',
        'description',
        'genre',
        'author_firstname',
        'author_lastname',
    ]
    action = 'Update'

'''
class AuthorListView(ListView):
    model = Author
'''