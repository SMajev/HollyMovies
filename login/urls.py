from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import (ProfileView, UserCreateView, UserUpdateView,
                        CustomLoginView, CustomLogoutView
                    )

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('profile/<int:pk>', ProfileView.as_view(), name='profile'),
    path('profile/sign', UserCreateView.as_view(), name='register'),
    path('profile/<int:pk>/edit', UserUpdateView.as_view(), name='user-update'),
    path('', include('django.contrib.auth.urls')),
]
