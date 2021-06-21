
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import RedirectView

urlpatterns = [
    re_path(r'^$', RedirectView.as_view(url='variant/')),

    re_path(r'^variant/', include('variant.urls', namespace='variant')),

    re_path(r'^ws/variant/', include('variant.urlsWS', namespace='variantWS')),
    re_path(r'^ws/sample/', include('sample.urlsWS', namespace='sampleWS')),

    path('admin/', admin.site.urls),
]