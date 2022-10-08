from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.core import serializers
from .api_loader import *
from .models import Section, Instructor, Meeting
from .serializers import SectionSerializer, InstructorSerializer
from rest_framework import viewsets


# --- LOAD ALL SECTIONS FOR A GIVEN DEPARTMENT --- #
class DeptViewSet(viewsets.ModelViewSet):
    # queryset = Section.objects.all()
    serializer_class = SectionSerializer

    def get_queryset(self):
        dept = self.kwargs['dept']
        queryset = Section.objects.prefetch_related('instructor','meetings').filter(subject=dept)
        return queryset


# --- LOAD ALL SECTIONS --- #
class SectionViewSet(viewsets.ModelViewSet):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer


# --- TODO: LOAD ALL DEPARTMENT CODES --- #

# --- LOAD JSON FILES FOR ALL DEPARTMENTS --- #
def load_api(request):
    get_all_json_files()
    return HttpResponse("Hello, world. I just read a whole lot of JSON files.")


def load_api_by_dept(request, dept):
    filename = 'JSON/' + dept + '.json'
    load_json_file(filename)
    return HttpResponse("Hello, world. I just read a JSON file for " + dept + ".")

# --- END LOAD JSON FILES FOR ALL DEPARTMENTS --- #
