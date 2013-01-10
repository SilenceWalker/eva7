import models
import md5
from django import forms

class radcheckForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput(render_value=False))
    mac_address = forms.CharField(max_length=17, required=False)
    ip_address = forms.IPAddressField(required=False)
    
    def userSave(self, qr):
        pass_ = md5.new(qr['password']).hexdigest()
        user_pass = models.radcheck(username=qr['username'], attribute='MD5-Password', value=pass_)
        user_pass.save(using='radius')
        
        if qr["mac_address"] != "":
            user_mac = models.radcheck(username=qr['username'], attribute='Calling-Station-ID', value=qr['mac_address'])
            user_mac.save(using='radius')
        if qr["ip_address"] != "":
            user_ip = models.radcheck(username=qr['username'], attribute='Framed-IP-Address', value=qr['ip_address'])
            user_ip.save(using='radius')
        
        