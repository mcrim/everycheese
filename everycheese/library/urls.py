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
]
