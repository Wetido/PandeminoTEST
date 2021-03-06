from django.urls import include, path
from rest_framework import routers
from PandeminoApp import views
from django.contrib import admin


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/', include('PandeminoApp.urls'),  name='PandeminoApp_api' ),
    path('api/registration/', include('registration.urls'), name='registration_api'),
    path('admin/', admin.site.urls),
]
