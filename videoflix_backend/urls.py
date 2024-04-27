"""
URL configuration for videoflix_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include

from videoflix.views import LoginView, RegisterView, PasswordResetView, PasswortResetUrlView, ActivateNewAccountView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LoginView.as_view()),
    path('register/', RegisterView.as_view()),
    path('password_reset/', PasswortResetUrlView.as_view(), name='reset_password'),
    path('password_reset/<str:encoded_pk>/<str:token>/', PasswordResetView.as_view(), name='reset_password'),
    path('account_activation/<str:encoded_pk>/', ActivateNewAccountView.as_view(), name='activate_account'),
]
