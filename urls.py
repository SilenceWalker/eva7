from django.conf.urls.defaults import *
import settings
import financial.views as finViews
import views as central
import netControl.views as nCViews
import SOControl.views as sOViews
import technical.views as techViews
import tech_support.views as tsViews


# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    
    url(r'^$', central.home, name='dashboard'),
    
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
    url(r'^logout/$', central.logout, name='logout'),
    
    url(r'^create/user/basic_informations/$', finViews.createUser, name='create-user/basic'),
    url(r'^create/user/radius_informations/user=(?P<user_n>\w+)$', nCViews.createUser, name='create-user/radius'),
    url(r'^create/so/$', sOViews.createOS, name='create-so'),
    url(r'^create/ca/$', finViews.createCoverageArea, name='create-ca'),
    url(r'^create/technical/basic/$', techViews.createTechUser, name='create-tech/basic'),
    url(r'^create/technical/user=(?P<user_n>\w+)$', techViews.createTechnical, name='create-tech/advanced'),
    url(r'^create/techSupport/basic/$', tsViews.createSupportTechUser, name='create-techsupport/basic'),
    url(r'^create/techSupport/user=(?P<user_n>\w+)$', tsViews.createTechnicalSupport, name='create-techsupport/advanced'),
       
    url(r'^list/user/$', finViews.listUser, name='list-user'),
    url(r'^list/ca/$', finViews.listCA, name='list-ca'),
    url(r'^list/so/$', sOViews.listOS, name='list-so'),
    url(r'^list/technical/$', techViews.listTechnical, name='list-tech'),
    url(r'^list/technicalsupport/$', tsViews.listTechnicalSupport, name='list-techsupport'),
    
    url(r'^edit/user/basic_informations/user=(?P<user_n>\w+)$', finViews.editUser, name='edit-user/basic'),
    url(r'^edit/user/radius_informations/user=(?P<user_n>\w+)$', nCViews.editUser, name='edit-user/radius'),
    url(r'^edit/so/soid=(?P<soid>\w+)$', sOViews.editSO, name='edit-so'),
    url(r'^edit/technicalsupport/tsid=(?P<tsid>\w+)$', tsViews.editTechnicalSupport, name='edit-techsupport'),
    url(r'^edit/ca/city=(?P<cityName>\w+)$', finViews.editCA, name='edit-ca'),

    # Example:
    # (r'^Eva7/', include('Eva7.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
    
    url(r'^media/(.*)$', 'django.views.static.serve',{'document_root': settings.MEDIA_ROOT}),
)
