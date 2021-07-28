from django.urls import path

from genesis.analysis import viewsWS as views_ws

app_name = 'analysis'

urlpatterns = [

    path('sample/', views_ws.SampleDetail.as_view(), name='post_sample'),
    path('sample_tag/', views_ws.SampleTagDetail.as_view(), name='post_sample_tag'),
    path('provider/', views_ws.ProviderDetail.as_view(), name='post_provider'),
    path('instrument/', views_ws.InstrumentDetail.as_view(), name='post_instrument'),
    path('run/', views_ws.RunDetail.as_view(), name='post_run'),
    path('run_tag/', views_ws.RunTagDetail.as_view(), name='post_run_tag'),
    path('result/', views_ws.ResultDetail.as_view(), name='post_result'),
    path('software/', views_ws.SoftwareDetail.as_view(), name='post_software'),
    path('analysis/', views_ws.AnalysisDetail.as_view(), name='post_analysis'),
    path('result_consumer/', views_ws.ResultConsumerDetail.as_view(), name='post_result_consumer'),
    path('sample_result/', views_ws.SampleResultDetail.as_view(), name='post_sample_result'),
    path('run_sample/', views_ws.RunSampleDetail.as_view(), name='post_run_sample'),

]
