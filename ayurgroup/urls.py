from django.conf.urls import include, url
from oscar.app import application
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'helper/', include('integration.urls')),
    url(r'', include(application.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
