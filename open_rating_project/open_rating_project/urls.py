from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
                       
                         # open rating                                                                                                                                                  
         url(r'^open-rating$', 'open_rating_project.open_rating.views.index'),

    # Example:
    # (r'^open_rating_project/', include('open_rating_project.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
)
