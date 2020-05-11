from django.urls import path
from registration import views
from rest_framework.urlpatterns import format_suffix_patterns

app_name = "account"

urlpatterns = [
    path('register/', views.registration_view, name="register")
]

urlpatterns = format_suffix_patterns(urlpatterns)
