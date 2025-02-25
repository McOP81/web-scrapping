# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.shortcuts import render
from .models import Smartphone, Laptop


def index(request):
    smartphones = Smartphone.objects.all()
    
    return render(request, 'home/index.html', {'smartphones': smartphones, 'segment': 'index'})

def laptop_list(request):
    laptops = Laptop.objects.all() 
    return render(request, 'home/laptop.html', {'laptops': laptops, 'segment': 'laptop_list'})


