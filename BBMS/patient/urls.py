from django.urls import path
from patient.views import *
urlpatterns = [
    path('signup/', patient_signup),
    path('login/', patient_login),
    path('make_request/', blood_request),
    path('request_history/<str:eml>', request_history),
    path('patient_dashboard/<str:eml>', patient_dashBoard)
]
