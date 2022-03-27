from django.urls import path

from . import views

app_name = 'core'
urlpatterns = [
    path('', views.app_list_view, name='app_list'),
    path('<slug:slug>', views.app_detail_view, name='app_deatail')
]





