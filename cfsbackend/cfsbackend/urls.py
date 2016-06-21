"""cfsbackend URL Configuration."""

from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers

import officer_allocation.views
from core import views

router = routers.DefaultRouter()
router.register(r'calls', views.CallViewSet)

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/call_volume/$', views.APICallVolumeView.as_view()),
    url(r'^api/response_time/$', views.APICallResponseTimeView.as_view()),
    url(r'^api/officer_allocation/', officer_allocation.views.APIOfficerAllocationView.as_view()),
    url(r'^api/call_map/', views.APICallMapView.as_view()),
    url(r'^api/', include(router.urls)),
    url(r'^docs/', include('rest_framework_swagger.urls')),
    url(r'^$', views.LandingPageView.as_view()),
    url(r'^call_volume$', views.CallVolumeView.as_view()),
    url(r'^response_time$', views.ResponseTimeView.as_view()),
    url(r'^officer_allocation$', officer_allocation.views.OfficerAllocationDashboardView.as_view()),
    url(r'^calls$', views.CallListView.as_view()),
    url(r'^calls.csv$', views.CallExportView.as_view()),
    url(r'^call_map$', views.MapView.as_view())
]
