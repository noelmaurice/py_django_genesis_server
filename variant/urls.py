from django.urls import path

from variant import views as views

app_name = 'variant'

urlpatterns = [
    # home path
    path('', views.index, name='index'),
]
