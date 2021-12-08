from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import (ProfileView, UserCreateView, UserUpdateView,
                        CustomLoginView, CustomLogoutView, SubmitablePasswordView,
                        UsersList, UserAdminView, CustomUserDeleteView, AdminPasswordView
                    )

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('<int:pk>', ProfileView.as_view(), name='profile'),
    path('sign', UserCreateView.as_view(), name='register'),
    path('<int:pk>/edit', UserUpdateView.as_view(), name='user-update'),
    path('<int:pk>/admin_edit', UserAdminView.as_view(), name='user-admin-update'),
    path('<int:pk>/admin_del', CustomUserDeleteView.as_view(), name='user-admin-delete'),
    path('<int:pk>/changepasswd', SubmitablePasswordView.as_view(), name='user-passwd'),
    path('<int:pk>/adminpasswd', AdminPasswordView.as_view(), name='admin-passwd'),
    path('users', UsersList.as_view(), name='users'),
    path('', include('django.contrib.auth.urls')),
]
