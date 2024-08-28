from django.urls import path
from .views import StudentAPiView, StudentNotesAPiView, UpdateStudentAPiView, UpdateStudentNotesAPiView

urlpatterns = [
    path('estudante/', StudentAPiView.as_view(), name='student'),
    path('update/estudante/', UpdateStudentAPiView.as_view(), name='update_student'),
    path('nota-estudante/', StudentNotesAPiView.as_view(), name='notes'),
    path('update/notas/', UpdateStudentNotesAPiView.as_view(), name='update_notes')
]