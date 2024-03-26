# everycheese/library/urls.py
from django.urls import path 
from . import views

app_name = "library" 
urlpatterns = [
    
    path( 
        route='',
        view=views.LibraryListView.as_view(),
        name='list' 
    ),
    path(
        route='add/',
        view=views.LibraryCreateView.as_view(),
        name='add'
    ),
    path(
        route='<slug:slug>/update/',
        view=views.LibraryUpdateView.as_view(),
        name='update'
    ),
    path(
        route='<slug:slug>/',
        view=views.LibraryDetailView.as_view(),
        name='detail'
    ),
]
'''
    path(
        route='',
        view=views.AuthorListView.as_view(),
        name='author_list'
    ),
    '''