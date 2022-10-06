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

def find_all_by_dept_old(request, dept):
    sections = Section.objects.filter(subject=dept)
    instructors = Instructor.objects.all()
    meetings = Meeting.objects.all()
    all_sections_to_return = [*instructors, *meetings, *sections]
    sections_serialized = serializers.serialize('json', all_sections_to_return)
    return HttpResponse(sections_serialized, content_type='application/json')

def find_all_by_dept(request, dept):
    sections = Section.objects.filter(subject=dept)
    return render(request, 'findallbydept.html', {'sections': sections})

