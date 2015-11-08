from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hcoop.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^inicio/$','ahcoop.views.inicio', name='inicio'),
    url(r'^regras/$','ahcoop.views.regras', name='regras'),
 #  url(r'^prim_paragraf/$','ahcoop.views.primParagraf', name='prim_paragraf'),
    url(r'^prim_paragraf/', 'ahcoop.views.primParagraf',name='prim_paragraf'),
    url(r'^proxparte/$','ahcoop.views.proxParte', name='proxparte'),
    url(r'^adminesp/$','ahcoop.views.adminesp', name='adminesp'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'ahcoop.views.redireciona'), 
)


