#!/usr/bin/python
# -*- coding: utf-8
from django.http import HttpResponse
from django.shortcuts import render_to_response
from settings import MEDIA_URL
from django.core import serializers

# Create your views here.
def index(request):
    """front page"""
    return render_to_response('index.html',{})