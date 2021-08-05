from django.urls import path, re_path

from genesis.analysis import viewsWS as views_ws

app_name = 'analysis'

urlpatterns = [

    # post
    path('sample/', views_ws.SampleDetail.as_view(), name='post_sample'),

    # put : the parent of the sample is modified
    path('sample/<int:pk>/parent/', views_ws.SampleDetail.as_view(), name='put_sample_parent'),

    # post
    path('sample_tag/', views_ws.SampleTagDetail.as_view(), name='post_sample_tag'),

    # post
    path('provider/', views_ws.ProviderDetail.as_view(), name='post_provider'),

    # post
    path('instrument/', views_ws.InstrumentDetail.as_view(), name='post_instrument'),

    # post
    path('run/', views_ws.RunDetail.as_view(), name='post_run'),

    #post
    path('run_tag/', views_ws.RunTagDetail.as_view(), name='post_run_tag'),

    # post
    path('result/', views_ws.ResultDetail.as_view(), name='post_result'),

    # put
    path('result/<int:pk>/', views_ws.ResultDetail.as_view(), name='put_result'),

    # post
    path('software/', views_ws.SoftwareDetail.as_view(), name='post_software'),

    # post
    path('analysis/', views_ws.AnalysisDetail.as_view(), name='post_analysis'),

    # post
    path('result_consumer/', views_ws.ResultConsumerDetail.as_view(), name='post_result_consumer'),

    # post
    path('sample_result/', views_ws.SampleResultDetail.as_view(), name='post_sample_result'),

    # post
    path('run_sample/', views_ws.RunSampleDetail.as_view(), name='post_run_sample'),

]
