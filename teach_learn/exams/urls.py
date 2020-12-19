from django.urls import include, path

from rest_framework.routers import DefaultRouter

from .views import exams as exams_views

router = DefaultRouter()
router.register(r'exams', exams_views.ExamViewSet, basename='exams')

urlpatterns = [
    path('', include(router.urls))
]
