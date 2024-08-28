from rest_framework import serializers
from .models import Student, StudentNote

# CONVERTE O OBJETO PYTHON PARA JSON E VIRSE E VERSA
class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        extra_kwargs = {
            'email': {'write_only': True}
        }
        model = Student
        exclude = ['id']


class StudentNotesSerializers(serializers.ModelSerializer):
    class Meta:
        model = StudentNote
        exclude = ['id']


class StudentNotesSerializers(serializers.ModelSerializer):
    class Meta:
        model = StudentNote
        exclude = ['id', 'owner']

