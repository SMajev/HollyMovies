from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from hollymovies import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('index.urls')),
    
    path('movies/', include('viewer.urls')),
    path('forum/', include('forum.urls')),
    path('profile/', include('login.urls'))

]

urlpatterns += static(settings.MEDIA_URL, 
                        document_root=settings.MEDIA_ROOT
                    ) 

urlpatterns += staticfiles_urlpatterns()