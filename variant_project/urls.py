
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import RedirectView

urlpatterns = [
    re_path(r'^$', RedirectView.as_view(url='variant/')),

    re_path(r'^sample/', include('sample.urls', namespace='sample')),
    re_path(r'^variant/', include('variant.urls', namespace='variant')),

    path('admin/', admin.site.urls),
]