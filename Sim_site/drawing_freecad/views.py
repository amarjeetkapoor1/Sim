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

list_pass2template = OrderedDict([('stories', ['Number of stories', '']), ('dep_of_foun', ['Depth of  foundation', '']),
    ('plinth_lev', ['Plinth level', '']), ('cclear_height', ['Clear height','']), ('dep_slab', ['Depth of foundation', '']),
    ('rep_span_len', ['Representaion of span length', '']), ('rep_span_wid', ['Representation of span width', '']),
    ('col_type', ['Column type', '']), ('len_col', ['Length of column', '']), ('wid_col', ['Width of column', '']),
    ('radius_col', ['Radius of column', '']), ('dep_beam', ['Depth of beam', '']), ('wid_beam', ['Width of beam', ''])])


lis = ['stories','dep_of_foun','plinth_lev','cclear_height','dep_slab','rep_span_len','rep_span_wid','col_type','len_col','wid_col','radius_col','dep_beam','wid_beam']

#bb = []

def specs(request):
    try:
        global lists
        global lis
        bb = list()
        for var in lists.keys():
            #print var +"  "+request.POST.get(var)
            lists[var] = str(request.POST.get(var))
            list_pass2template[var][1] = lists[var]
        print lists
        if list_pass2template["col_type"][1] == '0':
            list_pass2template["col_type"][1] = "Circular"
        elif list_pass2template["col_type"][1] == '1':
            list_pass2template["col_type"][1] = "Rectangular"
        print list_pass2template

        f = open('drawing_freecad/some.csv', 'w')
        ww = csv.writer(f, delimiter=' ')
        a = []
        for i in lists.keys():
            a.append(lists[i])
        ww.writerow(a)
        f.close()
        os.system('rm project.fcstd')
        os.system('cd drawing_freecad/FreeCAD_macros && freecadcmd drawing.py')
        return render(request, 'drawing_freecad/specs.html', {'list_pass2template': list_pass2template})
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


def convert_fcstd2webgl(request):
    os.system('cd drawing_freecad/FreeCAD_macros && freecadcmd fcstd2webgl.FCMacro')
    return render(request, 'drawing_freecad/show.html')

def drawing(request):
    global draw_list
    for i in draw_list.keys():
        draw_list[i] = request.POST.get(i)
    print draw_list
    return render(request,'web_app/drawing.html', {'draw_list':draw_list})
