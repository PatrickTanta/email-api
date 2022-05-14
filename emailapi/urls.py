from django.contrib import admin
from django.urls import path
from rest_framework import routers
from emails import views

router = routers.SimpleRouter()

router.register(r'emails', views.EmailModelViewSet, basename='emails')

urlpatterns = [
    path('admin/', admin.site.urls),
] + router.urls
