from rest_framework import routers
from .api import ProjectViewSet

router = routers.DefaultRouter()

# All CRUD
router.register('api/projects', ProjectViewSet, 'projects')

urlpatterns = router.urls