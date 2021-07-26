from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import RedirectView

urlpatterns = [
    re_path(r'^$', RedirectView.as_view(url='variant/')),

    # variants
    re_path(r'^variant/', include('genesis.variant.urls', namespace='variant')),

    # variant web services
    re_path(r'^ws/variant/', include('genesis.variant.urlsWS', namespace='variantWS')),

    # sample web services
    re_path(r'^ws/sample/', include('genesis.sample.urlsWS', namespace='sampleWS')),

    # analysis web services
    re_path(r'^ws/analysis/', include('genesis.analysis.urlsWS', namespace='analysisWS')),

    # admin web site
    path('admin/', admin.site.urls),

]
