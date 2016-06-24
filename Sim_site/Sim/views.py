from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
# Create your views here.
from .models import *
def hello(request):
	data = serializers.serialize("python",Indianlegacysectionsangle.objects.all())
	context = {'data': data}
	return render(request, 'Sim/hello.html', context)

def index(request):
	return render(request, 'Sim/index.html', {})
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
