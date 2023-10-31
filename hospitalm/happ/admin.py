from django.contrib import admin
from .models import Departments, Doctorsnew,Booking
# Register your models here.
admin.site.register(Departments)
admin.site.register(Doctorsnew)


class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'pat_name', 'pat_phone', 'doc_name',  'booking_date' ,'booked_on')
admin.site.register(Booking, BookingAdmin)