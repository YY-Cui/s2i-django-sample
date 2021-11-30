from django.conf import settings
from django.contrib import admin
from django.urls import include, path

from testapp.views import index

urlpatterns = [
    path('', index, name='home'),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
