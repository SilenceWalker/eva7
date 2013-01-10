from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf
from financial import forms as finForms
import netControl.forms as nCForms
import netControl.models as nCModels
import financial.models as finModels
from django.contrib.auth import logout

dic = {
       
       }

@login_required
def home(request):
    
    return render_to_response("dashboard.html", dic)
    

def logout(request):
    try:
        logout(request)
        return HttpResponseRedirect('/')
    except:
        return HttpResponseRedirect('/')

def editUser(request, sid):
    if request.method == 'POST':
        form = nCForms.radcheckForm(request.POST)
        
        qr = request.POST
        if form.is_valid():
            form.userEditSave(qr)
            
            return render_to_response("dashboard.html", dic)
    else:
        pass
        #criar instace 
        #form = nCForms.radcheckForm(instance=)
        
    dic.update({
                'form' : form,
                'sid' : sid,
            })
    
    dic.update(csrf(request))
    
    return render_to_response('editUserForm.html', dic)  