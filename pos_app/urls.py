from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('page2', views.next_page, name='next_page'),
]
