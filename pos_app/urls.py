from django.urls import path
from . import views
urlpatterns = [
    path('home/', views.home, name='home'),
    path('home/nextpage.html', views.next_page, name='next_page'),
]