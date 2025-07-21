from django.urls import path
from tareas import views
from rest_framework.routers import DefaultRouter
# Create a router and register our viewset with it
router = DefaultRouter()
router.register(r'tareas', views.TareaViewSet)
# The API URLs are now determined automatically by the router.
urlpatterns = router.urls