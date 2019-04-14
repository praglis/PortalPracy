from django.urls import path
from .views import OffertCreateView
from . import views

app_name = 'add'
urlpatterns = [
    #path('', views.offert, name='offert'),
    #path('offert/', views.offert, name='offert'),
    path('offert/', OffertCreateView.as_view(), name='offert'),
    path('form/', views.form, name='form'),
    path('apply/', views.apply, name='apply'),
]
