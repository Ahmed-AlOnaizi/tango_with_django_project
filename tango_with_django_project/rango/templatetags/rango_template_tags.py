# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 17:21:29 2023

@author: bullz
"""

from django import template
from rango.models import Category

register = template.Library()

@register.inclusion_tag('rango/categories.html')
def get_category_list(current_category=None):
    return {'categories': Category.objects.all(),
            'current_category': current_category}