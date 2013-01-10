from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf
from forms import *
from models import *
#from netControl import models as nCModels

dic = {}

def createUser(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
                
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/create/user/radius_informations/user='+request.POST["username"])
    
    else:
        form = UserForm()
    
    dic.update({
                'form' : form,
            })
    
    dic.update(csrf(request))
    
    return render_to_response('Financial/createUserForm.html', dic)

def listUser(request):
    users_list = User.objects.all()
    dic.update({
                'users_list' : users_list
                })
    
    return render_to_response('Financial/listUser.html', dic)

def editUser(request, user_n):
    try:
        user = User.objects.get(username=user_n)
    except:
        return HttpResponseRedirect('/list/user/')
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        
        if form.is_valid():
            form.save()
            
            return HttpResponseRedirect('/edit/user/radius_informations/user='+user_n)
    else:
        form = UserForm(instance=user)
        
    dic.update({
                'form' : form,
                'user_n' : user_n
            })
    
    dic.update(csrf(request))
    
    return render_to_response('Financial/editUserForm.html', dic)

def createCoverageArea(request):
    if request.method == 'POST':
        form = CoverageAreaForm(request.POST)
                
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/list/ca')
    
    else:
        form = CoverageAreaForm()
    
    dic.update({
                'form' : form,
            })
    
    dic.update(csrf(request))
    
    return render_to_response('Financial/createCAForm.html', dic)

def listCA(request):
    CA_list = Coverage_area.objects.all()
    dic.update({
                'CA_list' : CA_list
                })
    
    return render_to_response('Financial/listCA.html', dic)

def editCA(request, cityName):
    try:
        CA = Coverage_area.objects.get(city=cityName)
    except:
        return HttpResponseRedirect('/list/ca/')
    
    if request.method == 'POST':
        form = CoverageAreaForm(request.POST, instance=CA)
        
        if form.is_valid():
            form.save()
            
            return HttpResponseRedirect('/list/ca')
    else:
        form = CoverageAreaForm(instance=CA)
        
    dic.update({
                'form' : form,
                'city' : cityName,
            })
    
    dic.update(csrf(request))
    
    return render_to_response('Financial/editCAForm.html', dic)  