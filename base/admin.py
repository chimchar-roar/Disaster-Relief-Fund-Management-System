from django.contrib import admin

# Register your models here.
from .models import CustomUser,CitizenUser,StaffUser,CitizenDetails,Survey,Transfer
admin.site.register(CitizenUser)
admin.site.register(StaffUser)
admin.site.register(CitizenDetails)
admin.site.register(Survey)
admin.site.register(Transfer)