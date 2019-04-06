from django.urls import path

from . import views

app_name = 'my_offerts'
urlpatterns = [
    path('', views.index, name = 'index'),
]
