from django.urls import path

from . import views

app_name = 'add'
urlpatterns = [
    path('', views.offert, name='offert'),
    path('offert/', views.offert, name='offert'),
    path('form/', views.form, name='form'),
    path('apply/', views.apply, name='apply'),
]
