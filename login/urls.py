from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import (ProfileView, UserCreateView, UserUpdateView,
                        CustomLoginView, CustomLogoutView, SubmitablePasswordView,
                        UsersList, UserAdminView
                    )

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('profile/<int:pk>', ProfileView.as_view(), name='profile'),
    path('profile/sign', UserCreateView.as_view(), name='register'),
    path('profile/<int:pk>/edit', UserUpdateView.as_view(), name='user-update'),
    path('profile/<int:pk>/admin_edit', UserAdminView.as_view(), name='user-admin-update'),
    path('profile/<int:pk>/changepasswd', SubmitablePasswordView.as_view(), name='user-passwd'),
    path('profile/users', UsersList.as_view(), name='users'),
    path('', include('django.contrib.auth.urls')),
]
