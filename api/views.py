from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Student, StudentNote
from .serializers import StudentSerializers, StudentNotesSerializers

class StudentAPiView(APIView):
    def get(self, request):
        student = Student.objects.all()
        serializer = StudentSerializers(student, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = StudentSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class StudentNotesAPiView(APIView):
    def get(self, request):
        student_notes = StudentNote.objects.all()
        serializer = StudentNotesSerializers(student_notes, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = StudentNotesSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    

class UpdateStudentAPiView(APIView):    
    def post(self, request):
        serializer = StudentSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class UpdateStudentNotesAPiView(APIView):
    def get(self, request):
        student_notes = StudentNote.objects.all()
        serializer = StudentNotesSerializers(student_notes, many=True)
        return Response(serializer.data)