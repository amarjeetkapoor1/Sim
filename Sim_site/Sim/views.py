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

def table(request):
	tables = apps.get_app_config('Sim').get_models()
	name = request.POST.get('table')
	for t in tables:
		if t.__name__ == name:
			data = serializers.serialize("python", t.objects.all())
			context = {'data':data}
			return render(request, 'Sim/table.html', context)


def tables(request, name):
	tables = apps.get_app_config('Sim').get_models()
	for t in tables:
		if t.__name__ == name:
			data = serializers.serialize("python", t.objects.all())
			context = {'data':data}
			return render(request, 'Sim/tables.html', context)

def output(request):
	query1 = request.POST.get('query1')
	query2 = request.POST.get('query2')
	table_name = request.POST.get('option')
	tables = apps.get_app_config('Sim').get_models()
	for t in tables:
		if t.__name__ == table_name:
			query = "select "+query1+" from "+t._meta.db_table+" "+ query2 +";"
			try:
				data = serializers.serialize('python', t.objects.raw(query))
                                context = {'data': data}
			except:
				message = "Wrong Query! We told you. #Defensive Programming."
				data = ""
			        context = {'data': data, 'message': message}
	return render(request, 'Sim/output.html', context)

def home(request):
	return render(request, 'Sim/home.html', {})

def getfile(request):

	#get the fileitem
	try:
            fileitem=request.FILES['userfile']
            print fileitem
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
        except:
            m="Please browser the right file"
        return render(request, 'Sim/getfile.html', {'message':m})









