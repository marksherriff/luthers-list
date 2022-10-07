# Serializers to support JSON parsing

from rest_framework import serializers
from .models import Section, Instructor, Meeting

class InstructorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instructor
        fields = ['name', 'email']

class SectionSerializer(serializers.ModelSerializer):
    instructor = InstructorSerializer()
    meetings = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='days'
    )

    class Meta:
        model = Section
        fields = '__all__'

class MeetingSerializer(serializers.ModelSerializer):
    section = SectionSerializer()
    class Meta:
        model = Meeting
        fields = '__all__'

