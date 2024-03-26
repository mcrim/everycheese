from django.shortcuts import render

from django.views.generic import ListView, DetailView
from .models import Library

class LibraryListView(ListView):
    model = Library