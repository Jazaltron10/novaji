from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet
from onlineform import views
from django.contrib.auth import views as auth_views



router = DefaultRouter()
router.register('users', views.UserViewSet, basename='user')
urlpatterns = [
    # path('', include(router.urls)),
    path('login', auth_views.LoginView.as_view(), {'template_name': 'onlineform/login.html'}, name='login'),   
    path('logout', auth_views.LogoutView.as_view(), name='logout')    
]
