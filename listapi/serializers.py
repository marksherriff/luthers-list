# Serializers to support JSON parsing

from rest_framework import serializers
from .models import Section, Instructor, Meeting

class InstructorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instructor
        fields = ['name', 'email']

class SectionSerializer(serializers.ModelSerializer):
    instructor = InstructorSerializer()

    class Meta:
        model = Section
        fields = '__all__'