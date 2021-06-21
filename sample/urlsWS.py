from django.urls import path

from sample import viewsWS as views_ws

app_name = 'sample'

urlpatterns = [
    path('', views_ws.SampleView.as_view(), name='sampleWS'),
]
