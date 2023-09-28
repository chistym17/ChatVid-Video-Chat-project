from django.urls import path

from . import views

urlpatterns = [
    # path('',views.home,name='home'),
    path('',views.lobby,name='lobby'),
    path('room/',views.room,name='room'),
    path('get_token/',views.createToken,name='get_token')
    
]