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

def load_api_by_dept(request, dept):
    filename = 'JSON/' + dept + '.json'
    load_json_file(filename)
    return HttpResponse("Hello, world. I just read a whole lot of JSON files.")

def find_all_by_dept(request, dept):
    sections = Section.objects.filter(subject=dept)
    sections_serialized = serializers.serialize('json', sections)
    return HttpResponse(sections_serialized, content_type='application/json')

def find_all_by_dept_v2(request, dept):
    sections = Section.objects.filter(subject=dept)
    return render(request, 'findallbydept.html', {'sections': sections})

