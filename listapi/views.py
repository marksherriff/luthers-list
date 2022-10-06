from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.core import serializers
from .api_loader import *
from .models import Section,Instructor,Meeting

def load_api(request):
    get_all_json_files()
    return HttpResponse("Hello, world. I just read a whole lot of JSON files.")

def find_all_by_dept(request, dept):
    sections = Section.objects.filter(subject=dept)
    sections_list = serializers.serialize('json', sections)
    return HttpResponse(sections_list, content_type='application/json')