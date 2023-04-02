from django.contrib import admin
from django.urls import path, include

from Bloodmanager.views import admin_login, admin_signup, Donor_Details, Patient_Details, \
    update_patient_details, update_donor_details, Delete_Donor, Delete_Patient, Donation_Details, admin_dashboard, \
    request_history, stock_update, blood_request, homepage

urlpatterns = [
    path('patient/', include('patient.urls')),
    # path('', include('Bloodmanager.urls')),
    path('',homepage),
    path('donor/',include('donor.urls')),
    path('admin-blood-request/', include('Bloodmanager.urls')),
    path('admin-donation/', include('Bloodmanager.urls')),
    path('admin-request/',blood_request),
    path('admin-updated-stock/<int:unit>/<str:bg>/',stock_update),
    path('admin-request-history/', request_history),
    path('admin-login/', admin_login),
    path('admin-signup/', admin_signup),
    path('admin-dashboard/', admin_dashboard),
    path('admin-donor/', Donor_Details),
    path('admin-patient/', Patient_Details),
    path('admin-patient-update/<int:sn>/<str:district>/', update_patient_details),
    path('admin-donor-update/<int:sn>/<str:district>/', update_donor_details),
    path('admin-donor-delete/<int:sn>/', Delete_Donor),
    path('admin-patient-delete/<int:sn>/', Delete_Patient),
    path('admin-donation-detail/', Donation_Details),
]
