from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
from .models import Departments, Doctorsnew
from .forms import BookingForm
# Create your views here.
def index(request): 
    return render(request,'index.html')
def Base(request):
    return render(request, 'Base.html')

def about(request):
    return render(request,'About.html')

def booking(request):

    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'confirmbooking.html')
    form = BookingForm()
    dict_form = {
        'form': form
    }
    return render(request,'Booking.html' , dict_form)

def doctorss(request):
    dict_docs = {
        'doctors': Doctorsnew.objects.all()
    }
    return render(request, 'Doctors.html', dict_docs)

def contact(request):
    return render(request,'Contacts.html')

def department(request):
    dict_dept={
        'dept': Departments.objects.all()
    }
    return render(request, 'department.html',dict_dept)