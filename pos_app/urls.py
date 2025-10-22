from django.urls import path
from . import views
app_name = 'pos_app'
urlpatterns = [
    path('', views.intro, name='intro'),
    path('nextpage/', views.next_page, name='next_page'),
    path('Introduction/', views.intro, name='intro'),
    path('External_types/', views.external_types, name='external_types'),
    path('External_message_types/', views.external_message_types_layouts, name='external_message_types_layouts'),
    path('data_element/', views.data_element, name='data_element'),
    path('key_management/', views.key_management, name='key_management')
]
