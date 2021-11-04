from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('index.urls')),
    path('movies/', include('viewer.urls')),
    path('forum/', include('forum.urls'))
]

