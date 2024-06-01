
from django.contrib import admin
from django.urls import path
from EnergoMap import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.welcome, name='welcome'),
    path('CFO.html', views.CFO, name='CFO'),
    path('DFO.html', views.DFO, name='DFO'),
    path('PFO.html', views.PFO, name='PFO'),
    path('SFO.html', views.SFO, name='SFO'),
    path('SKFO.html', views.SKFO, name='SKFO'),
    path('UFO.html', views.UFO, name='UFO'),
    path('YFO.html', views.YFO, name='YFO'),
    path('SZFO.html', views.SZFO, name='SZFO'),
    path('upload_file.html', views.upload_file, name='upload_file'),
]
