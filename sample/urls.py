from django.urls import path

from sample import views_ws as sample_views_ws


app_name = 'sample'

urlpatterns = [
    path('ws/', sample_views_ws.SampleView.as_view()),
]
