from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import (
    RecordingViewSet,
    EventViewSet,
    SubscriptionViewSet,
    CourseViewSet,
    GroupViewSet,
    ModuleViewSet,
    PaymentMethodViewSet,
    SubscriptionTypeViewSet,
    EnrollmentViewSet,
    LessonViewSet,
    CategoryViewSet,
)

router = DefaultRouter()
router.register("module", ModuleViewSet)
router.register("recording", RecordingViewSet)
router.register("lesson", LessonViewSet)
router.register("enrollment", EnrollmentViewSet)
router.register("course", CourseViewSet)
router.register("group", GroupViewSet)
router.register("category", CategoryViewSet)
router.register("paymentmethod", PaymentMethodViewSet)
router.register("subscription", SubscriptionViewSet)
router.register("event", EventViewSet)
router.register("subscriptiontype", SubscriptionTypeViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
