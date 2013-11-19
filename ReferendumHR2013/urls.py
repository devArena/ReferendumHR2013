from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ReferendumHR2013.views.home', name='home'),
    # url(r'^ReferendumHR2013/', include('ReferendumHR2013.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    (r'^facebook/', include('django_facebook.urls')),
    (r'^accounts/', include('django_facebook.auth_urls')),
    (r'^referendum/', include('referendum.urls', namespace="referendum")),
)
