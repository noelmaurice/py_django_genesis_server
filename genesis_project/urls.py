from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import RedirectView

from genesis.variant import urls as variantUrls, urlsWS as variantUrlsWS
from genesis.analysis import urlsWS as analysisUrlsWS

urlpatterns = [
    re_path(r'^$', RedirectView.as_view(url='variant/')),

    # variants
    re_path(r'^variant/', include(variantUrls, namespace='variant')),

    # variant web services
    re_path(r'^ws/variant/', include(variantUrlsWS, namespace='variantWS')),

    # analysis web services
    re_path(r'^ws/analysis/', include(analysisUrlsWS, namespace='analysisWS')),

    # admin web site
    path('admin/', admin.site.urls),

]
