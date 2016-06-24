from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
# Create your views here.
from .models import *

def index(request):
	return render(request, 'Sim/index.html', {})
					
def tables(request, name):
	if name=="0":
		data=serializers.serialize("python", Indianlegacysectionsangle.objects.all())
		context = {'data':data}
	elif name=="1":
		data=serializers.serialize("python", Indianlegacysectionschannel.objects.all())
		context = {'data':data}
	elif name=="2":
		data=serializers.serialize("python", IndianlegacysectionsconversionErrors.objects.all())
		context = {'data':data}
	elif name=="3":
		data=serializers.serialize("python", Indianlegacysectionsdbinfo.objects.all())
		context = {'data':data}
	elif name=="4":
		data=serializers.serialize("python", IndianlegacysectionsfieldUnits.objects.all())
		context = {'data':data}
	elif name=="5":
		data=serializers.serialize("python", IndianlegacysectionsiShape.objects.all())
		context = {'data':data}
	elif name=="6":
		data=serializers.serialize("python", IndianlegacysectionsmShape.objects.all())
		context = {'data':data}
	elif name=="7":
		data=serializers.serialize("python", Indianlegacysectionspipe.objects.all())
		context = {'data':data}
	elif name=="8":
		data=serializers.serialize("python", IndianlegacysectionssShape.objects.all())
		context = {'data':data}
	elif name=="9":
		data=serializers.serialize("python", IndianlegacysectionstShape.objects.all())
		context = {'data':data}
	elif name=="10":
		data=serializers.serialize("python", Indianlegacysectionstube.objects.all())
		context = {'data':data}
	elif name=="11":
		data=serializers.serialize("python", IndianlegacysectionswShape.objects.all())
		context = {'data':data}
	elif name=="12":
		data=serializers.serialize("python", Indiansectionsangle.objects.all())
		context = {'data':data}
	elif name=="13":
		data=serializers.serialize("python", Indiansectionschannel.objects.all())
		context = {'data':data}
	elif name=="14":
		data=serializers.serialize("python", Indiansectionsdbinfo.objects.all())
		context = {'data':data}
	elif name=="15":
		data=serializers.serialize("python", IndiansectionsfieldUnits.objects.all())
		context = {'data':data}
	elif name=="16":
		data=serializers.serialize("python", IndiansectionsiShape.objects.all())
		context = {'data':data}
	elif name=="17":
		data=serializers.serialize("python", IndiansectionsmShape.objects.all())
		context = {'data':data}
	elif name=="18":
		data=serializers.serialize("python", Indiansectionspipe.objects.all())
		context = {'data':data}
	elif name=="19":
		data=serializers.serialize("python", IndiansectionssShape.objects.all())
		context = {'data':data}
	elif name=="20":
		data=serializers.serialize("python", IndiansectionstShape.objects.all())
		context = {'data':data}
	elif name=="21":
		data=serializers.serialize("python", Indiansectionstube.objects.all())
		context = {'data':data}
	elif name=="22":
		data=serializers.serialize("python", IndiansectionswShape.objects.all())
		context = {'data':data}
	elif name=="23":
		data=serializers.serialize("python", Jindalsectionsdbinfo.objects.all())
		context = {'data':data}
	elif name=="24":
		data=serializers.serialize("python", JindalsectionsfieldUnits.objects.all())
		context = {'data':data}
	elif name=="25":
		data=serializers.serialize("python", JindalsectionsheShape.objects.all())
		context = {'data':data}
	elif name=="26":
		data=serializers.serialize("python", JindalsectionsipeShape.objects.all())
		context = {'data':data}
	elif name=="27":
		data=serializers.serialize("python", JindalsectionsismcShape.objects.all())
		context = {'data':data}
	elif name=="28":
		data=serializers.serialize("python", JindalsectionsnpbShape.objects.all())
		context = {'data':data}
	elif name=="29":
		data=serializers.serialize("python", JindalsectionsubShape.objects.all())
		context = {'data':data}
	elif name=="30":
		data=serializers.serialize("python", JindalsectionsucShape.objects.all())
		context = {'data':data}
	elif name=="31":
		data=serializers.serialize("python", JindalsectionswpbShape.objects.all())
		context = {'data':data}
	elif name=="32":
		data=serializers.serialize("python", Job.objects.all())
		context = {'data':data}
	elif name=="33":
		data=serializers.serialize("python", JobMaterial.objects.all())
		context = {'data':data}
	elif name=="34":
		data=serializers.serialize("python", Joint.objects.all())
		context = {'data':data}
	elif name=="35":
		data=serializers.serialize("python", Member.objects.all())
		context = {'data':data}
	elif name=="36":
		data=serializers.serialize("python", MemberIncidence.objects.all())
		context = {'data':data}
	elif name=="37":
		data=serializers.serialize("python", MemberProperty.objects.all())
		context = {'data':data}
	elif name=="38":
		data=serializers.serialize("python", Tatastructuressectionschs.objects.all())
		context = {'data':data}
	elif name=="39":
		data=serializers.serialize("python", Tatastructuressectionsdbinfo.objects.all())
		context = {'data':data}
	elif name=="40":
		data=serializers.serialize("python", TatastructuressectionsfieldUnits.objects.all())
		context = {'data':data}
	elif name=="41":
		data=serializers.serialize("python", Tatastructuressectionsrhs.objects.all())
		context = {'data':data}
	elif name=="42":
		data=serializers.serialize("python", Tatastructuressectionsshs.objects.all())
		context = {'data':data}
	return render(request, 'Sim/table.html', context)
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	

