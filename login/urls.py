from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import ProfileView

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/<int:pk>', ProfileView.as_view(), name='profile'),
    path('', include('django.contrib.auth.urls')),
]
