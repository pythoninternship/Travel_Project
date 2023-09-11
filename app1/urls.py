from . import views
from django.urls import path

urlpatterns = [

    path('',views.project,name='project'),
    # path('add/',views.addition,name='addition'),
    # path('about/',views.about,name='about'),
    # path('contact/',views.contact,name='contact'),
    # path('thankyou/',views.thankyou,name='thankyou')
]