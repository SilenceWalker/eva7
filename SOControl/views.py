from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from forms import *
from models import *
import datetime
from SOControl.models import SO

dic = {
       
       }

def createOS(request):
    if request.method == 'POST':
        form = OSForm(request.POST)
        
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/list/so')
    
    else:
        form = OSForm()
    
    dic.update({
                'form' : form,
            })
    
    dic.update(csrf(request))
    
    return render_to_response('SOControl/createForm.html', dic)

def listOS(request):
    os_list = SO.objects.all()
    dic.update({
                'os_list' : os_list
                })
    
    return render_to_response('SOControl/list.html', dic)

def editSO(request, soid):
    try:
        so = SO.objects.get(id=soid) 
    except:
        return HttpResponseRedirect('/list/so/')
    if request.method == 'POST':
        form = OSForm(request.POST, instance=so)
        
        if form.is_valid():
            form.save()
            
            return HttpResponseRedirect('/list/so')
    else:
        form = OSForm(instance=so)
        
    dic.update({
                'form' : form,
                'soid' : soid,
            })
    
    dic.update(csrf(request))
    
    return render_to_response('SOControl/editForm.html', dic)  