from django.urls import path,include
from . import views
urlpatterns = [
    
    path('', views.index,name='home'),
    path('Base/',views.Base),

    path('About/',views.about),
    path('Booking/',views.booking,name='Booking'),
    path('Doctors/',views.doctorss,name='Doctors'),
    path('contact/',views.contact,name='Contact'),
    path('department/',views.department,name='department'),
    
]