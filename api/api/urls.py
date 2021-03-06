"""api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls import url, include
from django.conf.urls.static import static
from rest_framework import routers
from SongsApp.views import SongViewSet
from django.conf import settings

router = routers.DefaultRouter()
router.register('songs', SongViewSet, basename='songs') # 127.0.0.1:8000/songs/ -> ROUTES 

urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    #path('employees/', EmployeeDetail.as_view()),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
