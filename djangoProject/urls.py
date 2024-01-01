"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.views.generic import TemplateView
from rest_framework import routers, serializers, viewsets
from userLocation import views as userLocationViews
from restAPI import views as restApiViews
from weather import views as weatherApiViews
from hikeTracking import views as hikeViews
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

router = routers.DefaultRouter()
router.register(r'users', restApiViews.UserViewSet)
router.register(r'groups', restApiViews.GroupViewSet)
router.register(r'ElectoralDistricts', weatherApiViews.ElectoralDistrictsViewSet)
router.register(r'Counties', weatherApiViews.CountiesViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path("updatedb/", userLocationViews.update_location, name="updatedb"),
    path("", TemplateView.as_view(template_name="home.html"), name="home"),  # new
    #path('', include('posts.urls')),
    path('', include(router.urls)),
    path('', include('pwa.urls')),
    path("api/v1/", include('location.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('trail_tracking/', include('hikeTracking.urls')),
    path('golfCourse/', include('golfCourses.urls')),
]
urlpatterns += staticfiles_urlpatterns()
