from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from forms import *
from django.core.context_processors import csrf
from financial import forms as finForms
from financial import models as finModels
import models


dic = {
       
       }
    
def createUser(request, user_n):
    try:
        user = finModels.User.objects.get(username=user_n)
    except:
        return HttpResponseRedirect('/create/user/basic_informations/')
    
    if request.method == 'POST':
        form = radcheckForm(request.POST)
        
        qr = request.POST.copy()
        qr.update({
                   'username' : user_n,
                   })
        
        if form.is_valid():
            form.userSave(qr)
            
            return HttpResponseRedirect('/list/user/')
    else:
        form = radcheckForm()
    
    dic.update({
                'form' : form,
                'user_n' : user_n,
            })
    
    dic.update(csrf(request))
    
    return render_to_response('netControl/createradcheckForm.html', dic)

def editUser(request, user_n):
    try:
        user_details = models.radcheck.objects.using('radius').filter(username=user_n)
    except:
        return HttpResponseRedirect('/edit/user/basic_informations/user='+user_n)
    
    dic.update({
                'user_details' : user_details,
                'user_n' : user_n,
            })
    
    dic.update(csrf(request))
    
    return render_to_response('netControl/editradcheckForm.html', dic)