from django.urls import path
from .views import Index
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', Index.as_view(), name='index')
] 
urlpatterns += staticfiles_urlpatterns()