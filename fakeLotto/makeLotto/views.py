# -*- coding: utf-8 -*-
from django.shortcuts import render

# Create your views here.
def index(request):
    name = 'minho'
    return render(request, 'makeLotto/index.html', {'name':name})