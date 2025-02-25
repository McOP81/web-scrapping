# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Smartphone, Laptop


def index(request):
    smartphones = Smartphone.objects.all()
    return render(request, 'home/index.html', {'smartphones': smartphones})

def laptop_list(request):
    laptops_list = Laptop.objects.all()  # Récupère tous les laptops
    paginator = Paginator(laptops_list, 8)  # Pagination
    page = request.GET.get('page')

    try:
        laptops = paginator.page(page)
    except PageNotAnInteger:
        laptops = paginator.page(1)
    except EmptyPage:
        laptops = paginator.page(paginator.num_pages)

    return render(request, 'home/laptops.html', {'laptops': laptops})

def smartphone_list(request):
    smartphones = Smartphone.objects.all()
    return render(request, 'home/index.html', {'smartphones': smartphones})

def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))
