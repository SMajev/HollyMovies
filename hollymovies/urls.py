from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from hollymovies import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('index.urls')),
    
    path('movies/', include('viewer.urls')),
    path('forum/', include('forum.urls')),
    path('log/', include('login.urls'))

]

urlpatterns += static(settings.MEDIA_URL, 
                        document_root=settings.MEDIA_ROOT
                    )