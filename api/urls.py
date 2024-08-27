from django.urls import path
from .views import StudentAPiView, StudentNotesAPiView

urlpatterns = [
    path('estudante/', StudentAPiView.as_view(), name='courses'),
    path('nota-estudante/', StudentNotesAPiView.as_view(), name='assessment')
]