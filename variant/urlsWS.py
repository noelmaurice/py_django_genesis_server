from django.urls import path

from variant import viewsWS as views_ws

app_name = 'variant'

urlpatterns = [

    path('', views_ws.VariantView.as_view()),
]