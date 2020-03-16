"""projectweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from core import views
from django.views.generic import RedirectView
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
from . import settings

#CAMINHO PARA CADA BOTAO
urlpatterns = [
    path('admin/', admin.site.urls),
    path('roupas/all/', views.list_all_roupas),
    path('roupas/user/', views.list_user_roupas),
    path('roupas/detail/<id>/', views.roupas_detail),
    path('login/', views.login_user),
    path('login/submit', views.submit_login),
    path('logout/', views.logout_user),
    path('roupas/register/', views.register_roupas),
    path('roupas/register/submit', views.set_roupas),
    path('roupas/delete/<id>/', views.delete_roupas),
    path('', RedirectView.as_view(url='roupas/all/'))
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)