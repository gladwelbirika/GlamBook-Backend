from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, ServiceViewSet, StylistViewSet, BookingViewSet, PaymentViewSet   

router = DefaultRouter()

router.register("categories", CategoryViewSet)
router.register("services", ServiceViewSet)
router.register("stylists", StylistViewSet) 
router.register("bookings", BookingViewSet)
router.register("payments", PaymentViewSet)

urlpatterns = router.urls
