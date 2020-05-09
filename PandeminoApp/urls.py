from django.urls import path
from PandeminoApp import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('', views.api_detail_all, name='all'),
    path('<slug>/', views.api_detail_view, name='detail'),
    path('<slug>/update', views.api_update_view, name='update'),
    path('<slug>/delete', views.api_delete_view, name='delete'),
    path('create', views.api_create_view, name='create')
]

urlpatterns = format_suffix_patterns(urlpatterns)
