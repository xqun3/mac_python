# -*- coding: utf-8 -*-
# from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect 
# Create your views here.
# from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.shortcuts import render_to_response

# from django.http import JsonResponse
import json
from backend import process_loadedpdb
import os
from django.views.decorators import csrf
import chardet
import copy
import numpy as np
import httplib
import urllib2
# import argparse
# parser = process_loadedpdb.parser

def index(request):
    return render(request, 'index.html')
def simple_upload(request):
    return render(request, 'simple_upload.html')
    # return render(request, 'integration.html')


# def loadpdb(request):
#     # https://files.rcsb.org/download/1crn.pdb

#     print "downloading with urllib2"
#     PdbID = request.GET['a']
#     url = 'https://files.rcsb.org/download/'+ PdbID +'.pdb'
#     f = urllib2.urlopen(url) 
#     data = f.read() 
#     downloadpdb = "media/%s.pdb"%PdbID
#     with open(downloadpdb, "wb") as code:   
#       code.write(data)
#     result_dict2 = process_loadedpdb.process_pdb1(downloadpdb)
#     print downloadpdb
#     if result_dict2 == False:
#         wrongmsg1 = True
#         print wrongmsg1
#         return render(request, 'simple_upload.html', {
#             # 'reslut_dict': reslut_dict
#             'wrongmsg1': json.dumps(wrongmsg1),
#         })
#     # print result_dict1
#     # json_data = json.dumps(reslut_dict, separators=(',', ':')) 
#     return render(request, 'base_result.html', {
#         'uploaded_file_url': json.dumps('/'+downloadpdb),
#         # 'reslut_dict': reslut_dict
#         'result_dict1': json.dumps(result_dict2),
#     })
def result(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        print uploaded_file_url
        bdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        father_path=os.path.abspath(os.path.dirname(bdir)+os.path.sep+".")
        result_dict1 = process_loadedpdb.process_pdb1(father_path + uploaded_file_url)
        if result_dict1 == False:
            wrongmsg = True
            print wrongmsg
            return render(request, 'simple_upload.html', {
                # 'reslut_dict': reslut_dict
                'wrongmsg': json.dumps(wrongmsg),
            })
        # print result_dict1
        # json_data = json.dumps(reslut_dict, separators=(',', ':')) 
        return render(request, 'base_result.html', {
            'uploaded_file_url': json.dumps(uploaded_file_url),
            # 'reslut_dict': reslut_dict
            'result_dict1': json.dumps(result_dict1),
        })
    elif request.method == 'GET':
        print "downloading with urllib2"
        PdbID = request.GET['a']
        url = 'https://files.rcsb.org/download/'+ PdbID +'.pdb'
        f = urllib2.urlopen(url) 
        data = f.read() 
        downloadpdb = "media/%s.pdb"%PdbID
        with open(downloadpdb, "wb") as code:   
          code.write(data)
        result_dict2 = process_loadedpdb.process_pdb1(downloadpdb)
        print downloadpdb
        if result_dict2 == False:
            wrongmsg1 = True
            print wrongmsg1
            return render(request, 'simple_upload.html', {
                # 'reslut_dict': reslut_dict
                'wrongmsg1': json.dumps(wrongmsg1),
            })
        # print result_dict1
        # json_data = json.dumps(reslut_dict, separators=(',', ':')) 
        return render(request, 'base_result.html', {
            'uploaded_file_url': json.dumps('/'+downloadpdb),
            # 'reslut_dict': reslut_dict
            'result_dict1': json.dumps(result_dict2),
        })


def comments_upload(request):  
    if request.method == 'POST':  
        print "it's a test"                            #用于测试  
        print request.POST['name']           #测试是否能够接收到前端发来的name字段  
        print request.POST['password']     #用途同上  
  
        return HttpResponse("表单测试成功")     #最后返会给前端的数据，如果能在前端弹出框中显示我们就成功了  
    else:  
        return render(request,'test.html')

def integration(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        # process_loadedpdb.process_pdb()
        # print uploaded_file_url
        # return HttpResponse("文件上传成功")  
        # return JsonResponse(uploaded_file_url, safe=False)
        resp = "文件上传成功"
        HttpResponse(json.dumps(resp), content_type="application/json")
    # return render(request, 'simple_upload.html')
    return render(request, 'integration.html')

def result_base(request):
    List = ['自强学堂', '渲染Json到模板']
    Dict = {'site': 12.232, 'author': 13.23450}
    
    result_dict= process_loadedpdb.process_pdb('/Users/dongxq/Sites/project/media/brilM.pdb')
    # dict1 = {'CYS64-ILE102': 0.9643271, 'ASN6-CYS36': 0.97175026, 'LYS27-CYS79': 0.98015743, 'LEU78-CYS87': 0.99493909, 'ILE17-GLN88': 0.60018289, 'GLN41-PHE65': 0.99764061, 'CYS1-CYS43': 0.99764794, 'SER52-SER55': 0.84778833, 'THR9-CYS36': 0.99549544, 'CYS37-VAL69': 0.95059538, 'CYS75-CYS91': 0.89467913, 'LYS83-GLU86': 0.78248858, 'CYS20-VAL26': 0.97678238, 'THR44-GLU49': 0.63160717, 'CYS23-CYS79': 0.79461765, 'LEU30-ILE72': 0.50958848, 'CYS79-CYS87': 0.98777896, 'LEU3-CYS43': 0.96189582, 'ASN13-MET33': 0.9752118, 'LEU3-CYS40': 0.5557251, 'CYS75-CYS87': 0.78973401, 'LEU30-LEU76': 0.96143025, 'LYS51-SER55': 0.98620892, 'GLN71-LEU94': 0.76616061, 'CYS20-GLN25': 0.99625009, 'VAL16-CYS29': 0.99531871, 'ASN6-CYS40': 0.99559397, 'ASN13-CYS29': 0.97335285, 'ILE17-VAL26': 0.52856702, 'CYS37-PHE65': 0.68681014, 'LEU78-GLU86': 0.86555809, 'ASP2-ASP5': 0.731363, 'ASN99-GLN103': 0.65525472, 'ILE17-CYS29': 0.97806919, 'VAL26-CYS79': 0.95976686, 'CYS75-CYS90': 0.99594289, 'LEU68-THR97': 0.91530484, 'LEU10-CYS36': 0.92845851, 'CYS64-TYR101': 0.9992618, 'CYS23-VAL84': 0.90147549, 'ARG34-ILE72': 0.96744645, 'LEU10-MET33': 0.50534409}
    with open('brilm1'+'.json','a') as outfile1:
		json.dump(dict1,outfile1,ensure_ascii=False)
		outfile1.write('\n')
    with open('brilm'+'.json','a') as outfile:
    	json.dump(result_dict,outfile,ensure_ascii=False)
    	outfile.write('\n')
	
    # dict2 = copy.deepcopy(reslut_dict)
    # print id(reslut_dict),id(dict1)
    # dict2 = reslut_dict.copy()
    # for i in reslut_dict:
    # 	dict1[reslut_dict[i].key]=
    print '***************************'
    # print Dict
    # print dict1
    # print result_dict
    # print chardet.detect(reslut_dict)
    return render(request, 'result_base.html', {
            'List': json.dumps(Dict),
            'result_dict': json.dumps(result_dict),
    })

