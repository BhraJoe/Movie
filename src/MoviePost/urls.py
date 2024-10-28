


from django.urls import path
from .views import * 

urlpatterns = [
    
    
    
    path('', ShowHome, name='Home'),
    path('about/',ShowAbout, name='about'),
    path('contact/',ShowContact, name='contact'),
    path('services/',ShowServices, name='services'),
    path('team/',ShowTeam, name='team'),
    path('equalizer/',Equalizer, name='equalizer'),
    path('director/',Director, name='director'),
    path('mo/',Mo, name='mo'),
    path('latest/',Latest, name='latest'),
    path('movie/',Movie, name='movie'),
    path('popular/',Popular, name='popular'),
    path('up/',Up, name='up')

]