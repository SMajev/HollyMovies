from django.urls import path
from .views import CategoryList, PostsList, DetailView, CategoryPostsList

urlpatterns = [
    path('categorys/', CategoryList.as_view(), name='categorys'),
    path('category_posts', CategoryPostsList.as_view(), name='category_posts'),
    path('posts/', PostsList.as_view(), name='posts'),
    path('posts/<int:pk>', DetailView.as_view(), name='post')
]