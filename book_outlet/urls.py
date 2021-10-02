from django.urls import path 
from . import views 

urlpatterns = [
    path("", views.index),
    path("<slug:slug>", views.book_detail, name="book-detail")
    #id like the parameter in def book_detail in views.py
    #we precise int because in the initial migration file, the autofield convert automatically in integer 
]
