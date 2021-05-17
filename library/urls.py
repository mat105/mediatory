from rest_framework.routers import SimpleRouter
from library import views


router = SimpleRouter()

router.register(r'tale', views.TaleViewSet)

urlpatterns = router.urls
