from django.urls import path
from .views import CategoryList, DetailView, CategoryPostsList, AddPostForm, AddCommentForm

urlpatterns = [
    path('', CategoryList.as_view(), name='categorys'),
    path('<str:cat>', CategoryPostsList.as_view(), name='category_posts'),
    path('post/<int:pk>', DetailView.as_view(), name='post'),
    path('add/', AddPostForm.as_view(), name='add_post'),
]