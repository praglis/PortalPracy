from django.urls import path

from . import views

app_name = 'add'
urlpatterns = [
    path('', views.index, name='index'),
    path('apply/', views.apply, name='apply'),
]
