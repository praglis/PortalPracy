from django.urls import path

from . import views

app_name = 'sign_in'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('signup', views.signup, name = 'signup'),
]
