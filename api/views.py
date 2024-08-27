from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Course, Assessment
from .serializers import CourseSerializers, AssessmentSerializers

class CourseAPiView(APIView):
    def get(self, request):
        courses = Course.objects.all()
        serializer = CourseSerializers(courses, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = CourseSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class AssessmentAPiView(APIView):
    def get(self, request):
        assessments = Assessment.objects.all()
        serializer = AssessmentSerializers(assessments, many=True)
        return Response(serializer.data)

