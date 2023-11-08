from django.urls import include, path
from django.contrib import admin

from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns


from tuto import views


router = routers.SimpleRouter()
router.register('users', views.UserViewSet)
router.register('groups', views.GroupViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('', include('snippet.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
urlpatterns = format_suffix_patterns(urlpatterns)