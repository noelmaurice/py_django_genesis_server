from django.urls import path

from variant import views as views
from variant import viewsWS as views_ws

app_name = 'variant'

urlpatterns = [
    path('', views.index, name='index'),

]
