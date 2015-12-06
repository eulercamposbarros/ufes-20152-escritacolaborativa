"""
Definition of urls for EscritaColaborativa.
"""

from datetime import datetime
from django.conf.urls import patterns, url
from app.forms import BootstrapAuthenticationForm

# Uncomment the next lines to enable the admin:
from django.conf.urls import include
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'app.views.home', name='home'),
    url(r'^contact$', 'app.views.contact', name='contact'),
    url(r'^about', 'app.views.about', name='about'),

    url(r'^editar_historia', 'app.views.editar_historia', name='editar_historia'),      
    url(r'^listar_historia', 'app.views.listar_historia', name='listar_historia'),     
    url(r'^listar_interacao_historia', 'app.views.listar_interacao_historia', name='listar_interacao_historia'),     
    
    url(r'^validar_escritor', 'app.views.validar_escritor', name='validar_escritor'),      
    url(r'^salvar_edicao', 'app.views.salvar_edicao', name='salvar_edicao'),      
    

    url(r'^login/$',
        'django.contrib.auth.views.login',
        {
            'template_name': 'app/login.html',
            'authentication_form': BootstrapAuthenticationForm,
            'extra_context':
            {
                'title':'Log in',
                'year':datetime.now().year,
            }
        },
        name='login'),
    url(r'^logout$',
        'django.contrib.auth.views.logout',
        {
            'next_page': '/',
        },
        name='logout'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls), name='admin'),
)
