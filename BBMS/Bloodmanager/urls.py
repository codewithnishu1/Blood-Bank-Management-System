from django.urls import path
from Bloodmanager.views import admin_login, update_donor_details, reject_donation, \
    accept_donation, accept_request, reject_request

urlpatterns = [
    # path('',admin_login),
    path('update_donor_details/', update_donor_details),
    path('Accept-donation/<int:sn>/', accept_donation),
    path('Reject-donation/<int:sn>/',reject_donation),
    path('Accept-request/<int:sn>/',accept_request),
    path('Reject-request/<int:sn>/',reject_request),
]
