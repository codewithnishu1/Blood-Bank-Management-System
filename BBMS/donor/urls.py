from django.urls import path
from django.contrib.auth.views import LoginView

from donor.views import donor_dashboard, Donate_Blood, donation_history, request_blood, request_history

urlpatterns =[
    # path('login/', LoginView.as_view(template_name='')),
    # path('signup/', donor_signup),
    path('dashboard/<str:em>/',donor_dashboard),
    path('donate-blood/', Donate_Blood),
    path('donation-history/<str:email>', donation_history),
    path('request-blood/', request_blood),
    path('request-history/', request_history),
  ]