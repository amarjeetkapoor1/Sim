from django.shortcuts import render
from django.http import HttpResponse
import os, threading, csv, tempfile
from collections import OrderedDict
#from django.core.servers.basehttp import FileWrapper
#from wsgiref.util import FileWrapper


# Create your views here.

def index(request):
    return render(request, 'drawing_freecad/index.html')

#lists = {'stories':'','dep_of_foun':'','plinth_lev':'','cclear_height':'',
#    'dep_slab':'','rep_span_len':'','rep_span_wid':'','col_type':'',
#        'len_col':'','wid_col':'',  'radius_col':'','dep_beam':'',
#            'wid_beam':''}
#
lists = OrderedDict([('stories', ''), ('dep_of_foun', ''), ('plinth_lev', ''),
            ('cclear_height', ''), ('dep_slab', ''), ('rep_span_len', ''),
                ('rep_span_wid', ''), ('col_type', ''), ('len_col', ''),
                    ('wid_col', ''), ('radius_col', ''), ('dep_beam', ''),
                        ('wid_beam', '')])

lis = ['stories','dep_of_foun','plinth_lev','cclear_height','dep_slab','rep_span_len','rep_span_wid','col_type','len_col','wid_col','radius_col','dep_beam','wid_beam']

#bb = []

def specs(request):
    try:
        global lists
        global lis
        bb = list()
        for var in lists.keys():
            lists[var] = request.POST.get(var)
            # print("session  %s"  %request.session[var])
        print lists
#    print lists['rep_span_len']

#    print("list is : %s" %bb)
        f = open('drawing_freecad/some.csv', 'w')
        ww = csv.writer(f, delimiter=' ')
        a = []
        for i in lists.keys():
            a.append(lists[i])
        ww.writerow(a)
        f.close()
        os.system('rm project.fcstd')
        os.system('cd drawing_freecad/FreeCAD_macros && freecadcmd drawing.py')
#    print l
#    print request.POST
#    print len(request.POST)
        return render(request, 'drawing_freecad/specs.html', {'lists': lists})
    except:
        return render(request, 'drawing_freecad/specs.html',
        {'message': 'please fill again'})

def download(request):
    os.system('cd drawing_freecad/drawings/svg_pdf && rm -f *')
    os.system('cd drawing_freecad/drawings && rm -f drawings.zip')
    os.system('cp drawing_freecad/project.fcstd ./drawing_freecad/drawings/svg_pdf/')
    os.system('cd drawing_freecad/FreeCAD_macros && freecadcmd savepdf.FCMacro')
    command = "./drawing_freecad/drawings/drawings.zip"
    f = open(command)
    response = HttpResponse(f, content_type='application/zip')
    response['Content-Disposition'] = 'attachment; filename="drawings.zip"'
    return response

draw_list = OrderedDict([('x_dir', ''), ('y_dir', ''), ('z_dir', ''),
                ('hid_lines', ''), ('scale_size', ''), ('rotation', '')])

def drawing(request):
    global draw_list
    for i in draw_list.keys():
        draw_list[i] = request.POST.get(i)
    print draw_list
    return render(request,'web_app/drawing.html', {'draw_list':draw_list})
