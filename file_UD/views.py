# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
import os
import json

def home(request):
    print request
    print os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return render(request,'test.html')
    #return HttpResponse("Hello World Django")


def upload(request):
    if request.method=='GET':
        return HttpResponse('please url')
    elif request.method=='POST':
        user=request.POST.get('user')
        file_url=request.POST.get('file_url')
        file_data=request.FILES.get('file_url')
        file_path=os.path.join('/home/mql/Documents',file_data.name)
        f=open(file_path,'wb')
        for chunk in file_data.chunks():
            f.write(chunk)
        f.close()
        
        return HttpResponse(json.dumps({'status':True,'path':file_path}))


        