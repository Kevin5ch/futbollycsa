"""futbollarti URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.conf import settings
from torneo.views import fixture, index, posiciones, resultados, blog, torneo


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('fixture/', fixture, name="fixture"),
    path('posiciones/', posiciones, name="posiciones"),
    path('resultados/', resultados, name="resultados"),
    path('blog/', blog, name="blog"),
    path('torneo/', torneo, name="torneo"),
]

#Config for image upload in develop mode
if settings.DEBUG:
  from django.conf.urls.static import static
  urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)