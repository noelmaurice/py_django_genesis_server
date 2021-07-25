from django.urls import path

from genesis.sample import viewsWS as views_ws

app_name = 'sample'

urlpatterns = [
    path('', views_ws.SampleView.as_view(), name='get_all_samples_post_sample'),

    path('<int:pk>/', views_ws.SampleDetail.as_view(), name='get_sample'),
]
