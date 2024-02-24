from rest_framework import routers
from .api import ProjectViewSet
from rest_framework.documentation import include_docs_urls
from django.urls import path, include

router = routers.DefaultRouter()

# All CRUD
router.register('api/projects', ProjectViewSet, 'projects')

urlpatterns = [
    path('', include(router.urls)),
    path('docs/', include_docs_urls(title='Carapp Projects API')),
]