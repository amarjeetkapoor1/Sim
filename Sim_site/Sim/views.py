from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from django.apps import apps
import os

def index(request):
	tables = apps.get_app_config('Sim').get_models()
	table_names = []
	for t in tables:
		table_names.append(t.__name__)
	context = {'table_names' : table_names}
	return render(request, 'Sim/index.html', context)
	
def tables(request, name):
	tables = apps.get_app_config('Sim').get_models()
	for t in tables:
		if t.__name__ == name:
			data = serializers.serialize("python", t.objects.all())
			context = {'data':data}
			return render(request, 'Sim/table.html', context)
					
def home(request):
	return render(request, 'Sim/home.html', {})
def parseFile(request):
	
	#get the fileitem
	fileitem=request.FILES['userfile']
	if fileitem.file:
		#yay...we got a file
		message=fileitem.file.read()
	f=open('new.std','w')
	f.write(message)
	f.close()
	os.system('.././Main new.std>file 2>file2')
	
	f=open('file2','r')
	m=f.read()
	if(m):
		pass
	else:
		m="succesfull"
		
	f.close()
	os.system('rm new.std')
	return render(request, 'Sim/index.html', {'MESSAGE':message})
	
	
	
	
	
	
	
	

