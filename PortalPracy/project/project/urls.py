"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

from sign_in import views as sign_in_views
from offerts import views as offerts_views
from django.contrib.auth import views as auth_views

from django.conf import settings
from django.conf.urls.static import static

from sign_in.views import LogoutView

admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls, name='administrator'),
    path('offerts/', include('offerts.urls')),
    path('manage/', include('manager.urls')),
    path('search/', include('search.urls')),
    path('sign_in/', include('sign_in.urls')),
    path('', offerts_views.home, name='home'),
    path('register/', sign_in_views.register, name ='register'),
    path('profile/', sign_in_views.profile, name ='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='sign_in/login.html'), name='login'),
    path('logout/', LogoutView, name='logout'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
