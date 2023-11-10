from django.urls import path, include

from django.contrib import admin
from rest_framework import routers
from snippet import views

# Create a router and register our viewsets with it.
router = routers.SimpleRouter()
router.register('snippet', views.SnippetViewSet,basename="snippet")
router.register('users', views.UserViewSet,basename="user")

# The API URLs are now determined automatically by the router.
urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', include(router.urls)),
]
