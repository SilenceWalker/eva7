from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf
from django.contrib.auth.models import User
from forms import *
from models import *

dic = {}

def createSupportTechUser(request):
    if request.method == 'POST':
        form = TechSupportUserForm(request.POST)
                
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/create/techSupport/user='+request.POST['username'])
    
    else:
        form = TechSupportUserForm()
        
    dic.update({
                'form' : form,
                'info_name' : 'Basic',
            })
    
    dic.update(csrf(request))
        
    return render_to_response("TechSupport/createForm.html", dic)

def createTechnicalSupport(request, user_n):
    if request.method == 'POST':
        try:
            tech_user = User.objects.get(username=user_n)
        except:
            return HttpResponseRedirect('/create/techSupport/basic/')
        qr = request.POST.copy()

        qr.update({
                   'tech_user' : tech_user.id,
                   })

        form = TechForm(qr)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/list/techSupport/')
    
    else:
        form = TechForm()
        
    dic.update({
                'form' : form,
                'info_name' : 'Advanced',
                'user_n' : user_n,
            })
    
    dic.update(csrf(request))
        
    return render_to_response("TechSupport/createForm.html", dic)

def listTechnicalSupport(request):
    ts_list = Tech_Support.objects.all()
    dic.update({
                'ts_list' : ts_list
                })
    
    return render_to_response("TechSupport/list.html", dic)

def editTechnicalSupport(request, tsid):
    try:
        ts = User.objects.get(id=tsid) 
    except:
        return HttpResponseRedirect('/list/technicalsupport/')
    if request.method == 'POST':
        form = TechSupportUserForm(request.POST, instance=ts)
        
        if form.is_valid():
            form.save()
            
            return HttpResponseRedirect('/list/technicalsupport/')
    else:
        form = TechSupportUserForm(instance=ts)
        
    dic.update({
                'form' : form,
                'tsid' : tsid,
            })
    
    dic.update(csrf(request))
    
    return render_to_response('TechSupport/editForm.html', dic)  