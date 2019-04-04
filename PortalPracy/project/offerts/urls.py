from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('<int:joboffert_id>/', views.details, name = 'details'),
    
]