from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^labber/', include('labber.foo.urls')),

 
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    (r'^admin/', include(admin.site.urls)),
    
    (r'^weblog/', include('basic.blog.urls')),
    (r'^comments/', include('django.contrib.comments.urls')),
)
