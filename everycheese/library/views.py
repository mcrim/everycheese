from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

from django.views.generic import CreateView
from django.views.generic import ListView, DetailView
from .models import Library

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