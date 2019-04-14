from django.urls import path
from .views import OffertListView
from . import views

app_name = 'offerts'

urlpatterns = [
    path('', OffertListView.as_view(), name = 'index'),
    path('details/<int:offert_id>/', views.details, name = 'details'),

]
