from rest_framework import serializers
from .models import Course, Assessment

# CONVERTE O OBJETO PYTHON PARA JSON E VIRSE E VERSA
class AssessmentSerializers(serializers.ModelSerializer):
    class Meta:
        extra_kwargs = {
            'email': {'write_only': True}
        }
        model = Assessment
        exclude = ['id']


class CourseSerializers(serializers.ModelSerializer):
    class Meta:
        model = Course
        exclude = ['id']

