from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .api_loader import *

def load_api(request):
    get_all_json_files()
    return HttpResponse("Hello, world. You're at the load_api index.")