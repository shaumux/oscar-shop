from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from oscar.app import application

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'clothshop.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^i18n/', include('django.conf.urls.i18n')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'', include(application.urls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
