from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from mysite import views

urlpatterns = [
    path('', views.index, name='index'),
    path('generate_graph/', views.generate_graph, name='generate_graph'),
    path('admin/', admin.site.urls),
]

# Add the following line at the end of the file to serve media files during development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
