from django.urls import path

from . import views

app_name = 'mainapp'

urlpatterns = [
    path('', views.intro, name='intro'),
    path('instruction', views.instruction, name='instruction'),
    path('instruction2', views.instruction2, name='instruction2'),
    path('results', views.results, name='results'),
    path('errorpage', views.errorpage, name='errorpage'),
    path('download', views.download_file, name='download'),
    path('track-page', views.track_page, name='track-page'),

    path('faq', views.faq, name='faq'),
    path('info', views.info, name='info'),
    path('privacy', views.privacy, name='privacy'),

    path('tech_doc', views.tech_doc, name='tech_doc'),
    path('tech_attack', views.tech_attack, name='tech_attack'),
    path('tech_install', views.tech_install, name='tech_install'),
    path('tech_ver1', views.tech_ver1, name='tech_ver1'),
    path('tech_ver3', views.tech_ver3, name='tech_ver3'),
    path('tech_ver4', views.tech_ver4, name='tech_ver4'),
    path('tech_mixnet', views.tech_mixnet, name='tech_mixnet'),      
]
