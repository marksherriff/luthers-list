from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .api_loader import *

def load_api(request):
    get_all_json_files()
    return HttpResponse("Hello, world. I just read a whole lot of JSON files.")

def load_dept(request, dept):
    return HttpResponse("Loading:", dept)