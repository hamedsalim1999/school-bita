
from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render , redirect
from django.views.generic import TemplateView,ListView,DetailView
from django.http import HttpResponse

class HomeTemplateView(TemplateView):
    template_name = 'index.html'
    page_nam = 'index'