from django.urls import path

from genesis.analysis import viewsWS as views_ws

app_name = 'analysis'

urlpatterns = [

    # sample record
    path('sample/', views_ws.SampleView.as_view(), name='post_sample'),

]
