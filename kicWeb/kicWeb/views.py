# -*- coding: utf-8 -*-
"""
Created on Wed May 26 12:22:31 2021

@author: andya
"""
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from kicWeb import models
from django import forms
from django.shortcuts import render

# templates
def index(request):
    template = loader.get_template('ch01/index.html')
    context={ 'str':'hello'}
    return HttpResponse(template.render(context, request))

def list(request):
    template = loader.get_template('ch01/list.html')
    board = models.List()
    print(type(board))
    print(board)
    context={ 'board':board}
    return HttpResponse(template.render(context, request))

def content(request, num):
    template = loader.get_template('ch01/content.html')
    content = models.Content(num)
    context={ 'content':content[0]}
    return HttpResponse(template.render(context, request))

def writeform(request):
    template = loader.get_template('ch01/writeform.html')
    return HttpResponse(template.render(None, request)) 
    # None은 데이터 넘길게 없으면 저렇게 쓰면 된다
    
def write(request):
    board = { 
        'name': request.POST['name'],
        'content': request.POST['content'],
        'subject': request.POST['subject']
        
        }
    models.Write(board) # 위에서 딕셔너리로 만들어서 보내는 거다.
   
    return HttpResponseRedirect("/list/")    
    
def uploadfile(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            hadle_upload(request.FILES['file'])
            return HttpResponseRedirect("/")
    
    else:
        form = UploadFileForm()
        
    
    return render(request, 'ch01/upload.html', {'form':form})

def hadle_upload(f):
    with open("uploadDir/" + f.name, 'wb+') as destination:
        for ch in f.chunks():
            destination.write(ch)
            
class UploadFileForm(forms.Form):
    file = forms.FileField





















