from django.urls import path

from variant import viewsWS as views_ws

app_name = 'variant'

urlpatterns = [

    path('',
         views_ws.VariantView.as_view(),
         name='all_variants'),

    # <SERVER>/ws/variant/filters/splTOTO/
    path('filters/<str:sample_name>/',
         views_ws.find_distinct_filters,
         name='find_dictinct_filters'),

    # <SERVER>/ws/variant/node_value/splTOTO/annot.changes.HGVS/524G>A/
    path('node_value/<str:sample_name>/<str:node>/<str:value>/',
         views_ws.find_node_value,
         name='find_node_contains_value'),

    # <SERVER>/ws/variant/frequency/splTOTO/40/gt/
    path('frequency/<str:sample_name>/<int:frequency>/<str:comparator>/',
         views_ws.find_frequency,
         name='find_variants_with_frequency')
]
