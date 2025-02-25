# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views
# from .views import smartphone_list

urlpatterns = [

    # The home page
    path('', views.index, name='home'),

    # Route pour la liste des laptops
    path('laptop.html', views.laptop_list, name='laptop_list'),

]
