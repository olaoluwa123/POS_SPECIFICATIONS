from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('next_page', views.next_page, name='next_page'),
]
