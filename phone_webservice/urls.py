"""webservice URL Configuration

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
from django.db.models import base
from webservice.views import CreateUserView, CustomerViewSet, PhoneDetailsViewSet, PhoneRepairsViewSet, PhoneRequestViewSet, PhoneReviewsViewSet, PhoneTransactionsViewSet, PhoneViewSet, ProfileViewSet
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

router = routers.DefaultRouter()
router.register(r'customer', CustomerViewSet)
router.register(r'phone', PhoneViewSet)
router.register(r'phone-details', PhoneDetailsViewSet)
router.register(r'phone-transactions', PhoneTransactionsViewSet)
router.register(r'phone-repairs', PhoneRepairsViewSet)
router.register(r'phone-reviews', PhoneReviewsViewSet)
router.register(r'phone-request', PhoneRequestViewSet)
router.register(r'profile', ProfileViewSet)
router.register(r'register', CreateUserView, basename='register')



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', include(router.urls)),
    url(r'^api-token-auth/', obtain_jwt_token),
    url(r'^api-token-refresh/', refresh_jwt_token),
]
