from django.urls import path
from .views import CategoryList,  DetailView, CategoryPostsList, ShareForm, AddPostForm

urlpatterns = [
    path('', CategoryList.as_view(), name='categorys'),
    path('<str:cat>', CategoryPostsList.as_view(), name='category_posts'),
    # path('posts/', PostsList.as_view(), name='posts'),
    path('posts/<int:pk>', DetailView.as_view(), name='post'),
    path('add/', AddPostForm.as_view(), name='add_post'),
    path('post/share/<int:pk>', ShareForm.as_view() , name='email_share')
]