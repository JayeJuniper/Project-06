from django.urls import include, path
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('', include(('minerals.urls', 'minerals'),
                               namespace='minerals')),
    path('admin/', admin.site.urls),
]

urlpatterns += staticfiles_urlpatterns()
