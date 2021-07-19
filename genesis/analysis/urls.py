from django.urls import path

from genesis.variant import views as views

app_name = 'analysis'

urlpatterns = [
    # home analysis path
    path('', views.index, name='index'),
]
