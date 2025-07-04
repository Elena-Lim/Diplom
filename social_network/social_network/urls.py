"""
URL configuration for social_network project.

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
from os import path
from xml.etree.ElementInclude import include

from django.conf import settings
from django.template.context_processors import static
# from django.contrib import admin
# from django.urls import path, include
# from django.conf import settings
# from django.conf.urls.static import static
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api/', include('posts.urls')),
# ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.views.generic import TemplateView
from rest_framework.authtoken import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('posts.urls')),
    path('', TemplateView.as_view(template_name='index.html'), name='home'),  # ← Новая строка
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
