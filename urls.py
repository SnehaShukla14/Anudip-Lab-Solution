# from django.contrib import admin
# from django.urls import path
# from home import views

# urlpatterns = [
#     path("", views.index, name='home'),
#     path("about", views.about, name='about'),
#     path("services", views.services, name='services'),
#     path("contact", views.contact, name='contact'),
# ]

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClientViewSet, ProjectViewSet

router = DefaultRouter()
router.register(r'clients', ClientViewSet)
router.register(r'projects', ProjectViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),  # Add this line
]


