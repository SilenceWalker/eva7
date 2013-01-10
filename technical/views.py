from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf
from django.contrib.auth.models import User
from technical.forms import *

dic = {}

def createTechUser(request):
    if request.method == 'POST':
        form = TechUserForm(request.POST)
                
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/create/technical/user='+request.POST['username'])
    
    else:
        form = TechUserForm()
        
    dic.update({
                'form' : form,
                'info_name' : 'Basic',
            })
    
    dic.update(csrf(request))
        
    return render_to_response("Technical/createForm.html", dic)

def createTechnical(request, user_n):
    if request.method == 'POST':
        try:
            tech_user = User.objects.get(username=user_n)
        except:
            return HttpResponseRedirect('/create/technical/basic/')
        qr = request.POST.copy()

        qr.update({
                   'tech_user' : tech_user.id,
                   })

        form = TechForm(qr)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/list/technical/')
    
    else:
        form = TechForm()
        
    dic.update({
                'form' : form,
                'info_name' : 'Advanced',
                'user_n' : user_n,
            })
    
    dic.update(csrf(request))
        
    return render_to_response("Technical/createForm.html", dic)

def listTechnical(request):
    
    return render_to_response("Technical/list.html", dic)