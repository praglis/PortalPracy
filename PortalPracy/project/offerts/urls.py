from django.urls import path
from .views import (
    OffertListView,
    OffertDetailView,
    OffertUpdateView,
    OffertDeleteView,
    MyOffertsListView
)
from . import views

app_name = 'offerts'

urlpatterns = [
    path('', OffertListView.as_view(), name = 'index'),
    path('update/<int:pk>/', OffertUpdateView.as_view(), name='offert-update'),
    path('details/<int:pk>/', OffertDetailView.as_view(), name = 'offertDetails'),
    path('delete/<int:pk>/', OffertDeleteView.as_view(), name='offert-delete'),
    path('myofferts/', MyOffertsListView.as_view(), name='offert-my'),
]
