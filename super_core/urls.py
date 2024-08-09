"""
URL configuration for super_core project.

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
from django.urls import path
from django.conf.urls.static import static, settings
from super_info.views import HomeView, ContactView, PublicDetailView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', HomeView.as_view(), name = 'home-list'),
    path('contact/', ContactView.as_view(), name = 'contact-list'),
    path('public_detail/<int:pk>', PublicDetailView.as_view(), name = 'detail-list')
]

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)