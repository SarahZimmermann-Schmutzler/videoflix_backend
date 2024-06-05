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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from videoflix.views import ForgottenPasswordView, LoginView, RegisterView, ActivateNewAccountView, ResetPasswordView, LogoutView, VideosView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view()),
    path('account_activation/', ActivateNewAccountView.as_view()),
    path('forgotten_password/', ForgottenPasswordView.as_view()),
    path('reset_password/', ResetPasswordView.as_view()),
    path('logout/<userId>/', LogoutView.as_view()),
    path('__debug__/', include('debug_toolbar.urls')),
    path('django-rq/', include('django_rq.urls')),
    path('api/videos/', VideosView.as_view()),
    path('api/videos/<videoId>/', VideosView.as_view()),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) + staticfiles_urlpatterns()
