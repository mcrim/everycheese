# everycheese/cheeses/urls.py
from django.urls import path 
from . import views

app_name = "cheeses" 

urlpatterns = [
    path( 
        route='',
        view=views.CheeseListView.as_view(),
        name='list' 
    ),
    # URL Pattern for the CheeseDetailView
    path(
        route = 'add/',
        view = views.CheeseCreateView.as_view(),
        name = 'add'
    ),
    path(
        route='<slug:slug>/update/', 
        view=views.CheeseUpdateView.as_view(), 
        name='update'
    ),
    path(
        route='<slug:slug>/',
        view=views.CheeseDetailView.as_view(),
        name='detail'
    ),
    path(
        route='',
        view=views.BookListView.as_view(),
        name='list'
    ),
    path(
        route='authors',
        view=views.AuthorListView.as_view(),
        name='author_list'
    ),
    
]

