from django.urls import path, re_path, include
from usuarios import views
from rest_framework.routers import DefaultRouter
# Create a router and register our viewset with it
router = DefaultRouter()
router.register(r'usuarios', views.UsuarioViewSet)
# The API URLs are now determined automatically by the router.
# urlpatterns = router.urls
urlpatterns = [
    path('', include(router.urls)),
    re_path('register/', views.register, name='register'),
    re_path('login/', views.login, name='login'),
    re_path('profile/', views.user_profile, name='user_profile'),
]   
