# from django.urls import path
# from . import views

# urlpatterns = [path("", views.home)]
# myapp/urls.py
from django.urls import path
from .views import citizen_register, staff_register,home,citizen_login,staff_login,citizen_applicationform,citizen_details_display,citizen_application_status,staff_home,displaytostaff,surveyform_fill,display_surveyform,citizen_home,logoutUser,staff_citizens,staff_transactions,about
urlpatterns = [
    path('',home,name='home-view'),
    path('about/',about,name='about'),
    path('register/citizen/', citizen_register, name='citizen_register'),
    path('register/staff/', staff_register, name='staff_register'),
    path('login/citizen/',citizen_login,name='citizen_login'),
    path('login/staff/',staff_login,name='staff_login'),
    path('citizen/home/',citizen_home,name='citizen-home'),
    path('citizen/applicationform/',citizen_applicationform,name='citizen_applicationform'),
    path('citizen/applicationform_display',citizen_details_display,name='citizen-details-display'),
    path('citizen/application_status',citizen_application_status,name='app-status'),
    path('staff/home/',staff_home,name='staff-home'),
    path('staff/transactions/',staff_transactions,name='staff-transactions'),
    path('staff/home/citizens/',staff_citizens,name='staff_citizens'),
    path('staff/home/username=<str:username>',displaytostaff,name='each-citizen'),
    path('staff/home/survey/username=<str:username>',surveyform_fill,name='fill-survey'),
    path('staff/home/survey_display/username<str:username>',display_surveyform,name='display-survey'),
    path('logoutUser/',logoutUser,name='logout-user')
    # Add other URLs as needed
]
