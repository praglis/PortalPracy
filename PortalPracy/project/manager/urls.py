from django.urls import path

from .views import (
    OffertUpdateView,
    OffertDeleteView,
    MyOffertsListView,
    RepliesView,
    ReplyDetails
)
from . import views

app_name = 'manager'
urlpatterns = [
    path('delete/<int:pk>/', OffertDeleteView.as_view(), name='manager-delete'),
    path('user/<str:username>/', MyOffertsListView.as_view(), name='manager-my'),
    path('update/<int:pk>/', OffertUpdateView, name='manager-update'),
    path('replies/<int:pk>/', RepliesView, name='manager-replies'),
    path('replies/details/<int:pk>/', ReplyDetails, name='manager-reply-details'),
]
