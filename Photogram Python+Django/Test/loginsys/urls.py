from django.conf.urls import url


urlpatterns = [

    url(r'^login/', 'loginsys.views.login'),
    url(r'^logout/', 'loginsys.views.logout'),
    url(r'^registration/$', 'loginsys.views.registration'),

]