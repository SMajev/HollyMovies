from django.urls import path
from .views import CategoryList, PostsList, DetailView, CategoryPostsList
from .forms import EmailPostForm
urlpatterns = [
    path('categorys/', CategoryList.as_view(), name='categorys'),
    path('category/<str:cat>', CategoryPostsList.as_view(), name='category_posts'),
    path('posts/', PostsList.as_view(), name='posts'),
    path('posts/<int:pk>', DetailView.as_view(), name='post'),
    path('post/share/<int:pk>', EmailPostForm.as_table() , name='email_share')
]