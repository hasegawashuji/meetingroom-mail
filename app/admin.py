from django.contrib import admin
from .models import Room, Staff, Booking, Schedule

admin.site.register(Room)
admin.site.register(Staff)
admin.site.register(Booking)
admin.site.register(Schedule)