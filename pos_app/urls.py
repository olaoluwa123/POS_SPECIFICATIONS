from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('nextpage.html', views.next_page, name='next_page'),
]
