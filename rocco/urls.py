from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns

# URL for language switching (not prefixed)
urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
]

# i18n prefixed URLs
urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('', include('company.urls')),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)