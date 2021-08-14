from django.conf.urls import include, url

from rest_framework import routers

from ghostapi.views import PostsViewSet

router = routers.DefaultRouter()

router.register(r'Post', PostsViewSet)

urlpatterns = [
    url(r'^ghostapi/', include(router.urls))
]
