from django.urls import path
from registration import views
from rest_framework.urlpatterns import format_suffix_patterns

app_name = "account"

urlpatterns = [
    path('register/', views.registration_view, name="register"),
    path('accounts/', views.registration_detail_all, name="info")
]

urlpatterns = format_suffix_patterns(urlpatterns)
