# -*- coding: utf-8 -*-
"""
Created on Fri Jan 20 09:35:26 2023

@author: bullz
"""

from django.urls import path
from rango import views
app_name = 'rango'


urlpatterns = [
path('', views.index, name='index'),
path('',views.about, name = 'about')
]