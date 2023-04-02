from django.http import HttpResponse
from django.shortcuts import render

from Bloodmanager.models import Blood_request


# Create your views here.
from genericpath import exists
from itertools import count
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render

from Bloodmanager.models import Blood_request, Donation, admini

from donor.models import Donor
from patient.models import Patient

blood = {'A+': 10, 'A-': 10, 'B+': 10, 'B-': 10, 'AB+': 10, 'AB-': 10, 'O+': 10, 'O-': 10}


def homepage(request):
    return HttpResponse('This is My Website Homepage')

# def Blood_stock(request):
#     return JsonResponse(blood)

def admin_dashboard(request):
    return JsonResponse(blood)


def admin_signup(request):
    if request.method == "POST":

        """retrive admin inputs"""
        name = request.POST.get('admin-name')
        eml = request.POST.get('admin-email')
        psw = request.POST.get('admin-password')
        try:
            obj = Patient.objects.get(email=eml)
        except Patient.DoesNotExist:
            obj = Patient()
            obj.name = name
            obj.email = eml
            obj.password = psw
            obj.save()
            # return redirect('/admin-login.html/')
    return HttpResponse('PLease try again')


def admin_login(request):
    if request.method == "POST":

        """retrive admin inputs"""
        el = request.POST.get('admin-email')
        psw = request.POST.get('admin-password')
        print(el, psw)
        try:
            obj = admini.objects.get(email=el)
        except admini.DoesNotExist:
            return HttpResponse('No admin profile found')
        if obj.password != psw:
            return HttpResponse('incorrect password')
        # return redirect('admin-dashboard/')
    return HttpResponse('there should be method="post"')


def Donor_Details(request):
    obj = Donor.objects.all()
    l = []
    for i in obj:
        dict = {}
        dict['donor_id'] = i.id
        dict["donor_name"] = i.name
        dict['donor_email'] = i.email
        dict['age'] = i.age
        dict["bgroup"] = i.Bgroup
        dict['donor_district'] = i.district
        l.append(dict)
    d = {'donor':l}
    return JsonResponse(d)


def Patient_Details(request):
    obj = Patient.objects.all()
    l = []
    for i in obj:
        dict = {}
        dict['patient_id'] = i.id
        dict["patient_name"] = i.name
        dict['patient_email'] = i.email
        dict['age'] = i.age
        dict["bgroup"] = i.Bgroup
        dict['patient_district'] = i.district
        l.append(dict)
    d = {'patient':l}
    return JsonResponse(d)


def Delete_Donor(request,sn):
    obj = Donor.objects.get(id=sn)
    obj.delete()
    l = []
    for i in Donor.objects.all():
        dict = {}
        dict['donor_id'] = i.id
        dict["donor_name"] = i.name
        dict['donor_email'] = i.email
        dict['age'] = i.age
        dict["bgroup"] = i.Bgroup
        dict['donor_district'] = i.district
        l.append(dict)
    d = {'donor': l}
    # return redirect("/admin/admin-donor/")
    return JsonResponse(d)

def update_donor_details(request,sn,district):
    # if request.method == 'POST':
    #     n = request.POST.get('id')
    obj = Donor.objects.get(id=sn)
    # for key, value in request.POST:
    #     if value and True:
    #         setattr(obj, key, value)
    obj.district = district

    obj.save()
    l = []
    for i in Donor.objects.all():
        dict = {}
        dict['donor_id'] = i.id
        dict["donor_name"] = i.name
        dict['donor_email'] = i.email
        dict['age'] = i.age
        dict["bgroup"] = i.Bgroup
        dict['donor_district'] = i.district
        l.append(dict)
    d = {'donor': l}
    return JsonResponse(d)
    # return redirect("/admin/admin-donor/")
    # return HttpResponse('updated-donor-details')

def Delete_Patient(request,sn):
    # n = request.get('id')
    obj = Patient.objects.get(id=sn)
    obj.delete()

    l = []
    for i in Patient.objects.all():
        dict = {}
        dict['patient_id'] = i.id
        dict["patient_name"] = i.name
        dict['patient_email'] = i.email
        dict['age'] = i.age
        dict["bgroup"] = i.Bgroup
        dict['patient_district'] = i.district
        l.append(dict)
    d = {'patient': l}
    # return redirect("/admin/admin-patient/")
    return JsonResponse(d)

def update_patient_details(request,sn,district):
    # if request.method == 'POST':
    # n = request.POST.get('id')
    obj = Patient.objects.get(id=sn)
        # for key, value in request.POST:
        #     if value and True:
        #         setattr(obj, key, value)
    obj.district = district

    obj.save()
    l = []
    for i in Patient.objects.all():
        dict = {}
        dict['patient_id'] = i.id
        dict["patient_name"] = i.name
        dict['patient_email'] = i.email
        dict['age'] = i.age
        dict["bgroup"] = i.Bgroup
        dict['patient_district'] = i.district
        l.append(dict)
    d = {'patient': l}
    # return redirect("/admin/admin-patient/")
    return JsonResponse(d)

def Donation_Details(request):
    # n = request.POST.get('id')
    donation = Donation.objects.all()
    l = []
    for i in donation:
        dict = {}
        dict["donor_name"] = i.name
        dict['units'] = i.units
        dict["blood"] = i.Bgroup
        dict['status'] = i.status
        l.append(dict)
    d = {'donation': l}
    # return JsonResponse(donation)
    return JsonResponse(d)

def accept_donation(request,sn):
    global blood
    # n = request.POST.get('id')
    donation = Donation.objects.all()
    obj = Donation.objects.get(id=sn)
    if obj.status == 'Pending':
        obj.status = 'Accepted'
        bg = obj.Bgroup
        blood[bg] = blood.get(bg) + obj.units
    obj.save()
    l = []
    for i in donation:
        dict = {}
        dict["donor_name"] = i.name
        dict['units'] = i.units
        dict["blood"] = i.Bgroup
        dict['status'] = i.status
        l.append(dict)
    d = {'donation': l,'blood':blood}
    return JsonResponse(d)
    # return HttpResponse(obj)

# def request_made(request):
#     eml = request.get('email')
#     obj = Blood_request.objects.fetch(email=eml)
#     count(obj)
#     return count

def reject_donation(reqeust,sn):
    donation = Donation.objects.all()
    obj = Donation.objects.get(id=sn)
    if obj.status == 'Pending':
        obj.status = 'Rejected'
    obj.save()
    l = []
    for i in donation:
        dict = {}
        dict["donor_name"] = i.name
        dict['units'] = i.units
        dict["blood"] = i.Bgroup
        dict['status'] = i.status
        l.append(dict)
    d = {'donation': l,'blood':blood}
    print(blood)
    return JsonResponse(d)

def accept_request(request,sn):
    obj = Blood_request.objects.get(id=sn)
    rqs = Blood_request.objects.all()
    if obj.units > blood[obj.Bgroup]:
        return HttpResponse('Limited Stock')
    if obj.status == 'Pending':
        obj.status = 'Accepted'
        bg = obj.Bgroup
        unit = obj.units
        blood[bg] = blood.get(bg)-unit
    obj.save()
    l = []
    for i in rqs:
        dict = {}
        dict["_name"] = i.name
        dict['units'] = i.units
        dict["blood"] = i.Bgroup
        dict['status'] = i.status
        l.append(dict)
    d = {'Reqeust': l,'blood':blood}
    return JsonResponse(d)

def reject_request(request,sn):
    obj = Blood_request.objects.get(id=sn)
    rqs = Blood_request.objects.all()
    if obj.status == 'Pending':
        obj.status = 'Rejected'
    obj.save()
    l = []
    for i in rqs:
        dict = {}
        dict["name"] = i.name
        dict['units'] = i.units
        dict["blood"] = i.Bgroup
        dict['status'] = i.status
        l.append(dict)
    d = {'Request': l,'blood':blood}
    print(blood)
    return JsonResponse(d)

def request_history(request):
    obj = Blood_request.objects.all()
    l = []
    for i in obj:
        dict = {}
        dict["name"] = i.name
        dict['units'] = i.units
        dict["blood"] = i.Bgroup
        dict['status'] = i.status
        l.append(dict)
    d = {'Request': l}
    print(blood)
    return JsonResponse(d)

def stock_update(request,unit,bg):
    # unit = request.GET('unit')
    # bg = request.GET('bgroup')

    blood[bg] = blood.get(bg)+unit
    return JsonResponse(blood)


def blood_request(request):
    obj = Blood_request.objects.filter(status='Pending')
    l = []
    for i in obj:
        dict = {}
        dict['units'] = i.units
        dict['patient_id'] = i.id
        dict["patient_name"] = i.name
        dict["bgroup"] = i.Bgroup
        l.append(dict)
    d = {'patient':l}
    return JsonResponse(d)



