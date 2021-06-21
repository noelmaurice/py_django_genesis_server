from django.urls import path

from variant import views as variant_views

app_name = 'variant'

urlpatterns = [
    path('', variant_views.index, name='index'),
]
