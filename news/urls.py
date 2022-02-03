from rest_framework.routers import DefaultRouter
from .views import NewsLetterViewSet

router = DefaultRouter()
router.register('', NewsLetterViewSet)
urlpatterns = router.urls