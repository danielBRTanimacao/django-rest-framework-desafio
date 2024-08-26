from django.urls import path
from .views import CourseAPiView, AssessmentAPiView

urlpatterns = [
    path('courses/', CourseAPiView.as_view(), name='courses'),
    path('assessment/', AssessmentAPiView.as_view(), name='assessment')
]