from django.urls import path
from .views import OffertListView, OffertDetailView, OffertCreateView, ApplicationCreateView, ApplicationFormCreateView, ApplicationAnswersView,ApplyView
from . import views

app_name = 'offerts'

urlpatterns = [
    path('', OffertListView.as_view(), name = 'index'),
    path('details/<int:pk>/', OffertDetailView, name = 'offert_details'),
    path('new_offert/', OffertCreateView, name='new_offert'),
    path('application_form/', ApplicationFormCreateView, name='application_form'),
    path('set_answers/', ApplicationAnswersView, name='set_answers'),
    path('apply/<int:pk>', ApplyView, name='apply'),
]
