# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render 
from django.http import HttpResponse
from django.http import Http404
from .models import Dreamreal
#from django.views.generic import TemplateView
#def index(request):
#	return HttpResponse("Rango says hey there world")
def detail(request,website_id):
	return HttpResponse("website id is %s,"%website_id)
def index(request):
	latest_list = Dreamreal.objects.order_by('-date')[:3]
	context ={
	'latest_list':latest_list}
	return render(request,'index.html',context)
#def detail(request,dreamreal_id):
#	try:	
#		dreamreal = Dreamreal.objects.get(pk=dreamreal_id)
#	except Dreamreal.DoesNotExist:
#		raise Http404("Website does not exist")
#	return render(request, 'detail.html',{'dreamreal':dreamreal}) 


