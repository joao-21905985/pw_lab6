from django.shortcuts import render
from django.urls import path
from . import views

app_name = "website"

urlpatterns = [
    path('', views.base_page_view, name='base'),
    path('naval_battle', views.html2_page_view, name='html2'),
    path('hot_girl', views.html3_page_view, name='html3'),
    path('fomeca', views.html4_page_view, name='html4')
]