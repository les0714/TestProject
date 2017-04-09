from django.conf.urls import patterns, include, url
from django.contrib import admin
from appointment import views as appointment_views

admin.autodiscover()

urlpatterns = patterns('',
    # url(r'^firstapp/', include('firstapp.urls', namespace="firstapp")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^appointment', appointment_views.appointment_page ),
    url(r'', appointment_views.index_page ),
)
