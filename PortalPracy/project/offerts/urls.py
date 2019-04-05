from django.urls import path

from . import views

app_name = 'offerts'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('details/<int:offert_id>/', views.details, name = 'details'),

]
