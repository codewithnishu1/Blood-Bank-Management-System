from itertools import count
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from Bloodmanager.models import Blood_request
from patient.models import Patient

def patient_signup(request):
    if request.method == "POST":
        """retrieve patient inputs"""
        name = request.POST.get('patient-name')
        eml = request.POST.get('patient-email')
        psw = request.POST.get('patient-password')
        age = request.POST.get('patient-age')
        state = request.POST.get('patient-state')
        district = request.POST.get('patient-district')
        mob = request.POST.get('patient-mob')
        bgroup = request.POST.get('patient-bgroup')
        try:
            obj = Patient.objects.get(email=eml)
        except Patient.DoesNotExist:
            # return HttpResponse('No admin profile found')
            obj = Patient()  # it is object of patient class
            obj.name = name
            obj.email = eml
            obj.password = psw
            obj.Bgroup = bgroup
            obj.age = age
            obj.mobile_no = mob
            obj.state = state
            obj.district = district

        obj.save()
        # return JsonResponse(obj, safe=False)  # actually here is patient-login.html
        return render(request, 'patient/login.html')
    return render(request, 'patient/signup.html')


def patient_login(request):
    if request.method == "POST":

        email = request.POST.get('patient-email')
        password = request.POST.get('patient-password')
        print(email, password)
        try:
            obj = Patient.objects.get(email=email)
        except Patient.DoesNotExist:
             return HttpResponse('No Profile Found')
        if obj.password != password:
            return HttpResponse('Incorrect Password')
        # return redirect('patient_dashBoard')
        return HttpResponse('Login Successful')

    return render(request,'patient/login.html')
# def patient_login(request):
#         # request.GET
#         # el = request.GET['patient-email']
#         # psw = request.GET['patient-password']
#     if request.method == 'POST':
#         el = request.POST.get('patient-email')
#         psw = request.POST.get('patient-password')
#         print(el, psw)
#         l = []
#         data1 = Patient.objects.all()
#         for ele in data1:
#             l.append({'patient-email': ele.email, 'patient-password': ele.password})
#         for ele in l:
#             if ele['patient-email'] == el:
#                 if ele['patient-password'] == psw:
#                     return HttpResponse('Login Successful !')
#                 else:
#                     return HttpResponse('Login Failed!')
#             else:
#                 return HttpResponse('Register yourself first')
#     return render(request, 'patient/login.html')
    # else:
    #     return HttpResponse("this is not POST request")

def blood_request(request):
    if request.method == "POST":
        """retrieve patient inputs"""
        name = request.POST.get('patient-name')
        eml = request.POST.get('patient-email')
        bgroup = request.POST.get('patient-bgroup')
        # status = request.POST.get('patient-status')
        unit = request.POST.get('patient-unit')
        obj = Blood_request() # it is object of Blood_request class
        obj.name = name
        obj.email = eml
        # obj.status = status
        obj.Bgroup = bgroup
        obj.units = unit
        obj.save()

        return HttpResponse("Request Has Been Made")
    return render(request, 'patient/request.html')
        # print(name,eml,bgroup,unit)
        # return HttpResponse('Successful Request')
    # return HttpResponse('Try-again')

def request_history(request,eml):
    # eml = request.POST.get('email')
    # obj = Blood_request.objects.filter(email=eml)
    l = []
    for i in Blood_request.objects.filter(email=eml):
        dict = {}
        dict['patient_id'] = i.id
        dict["patient_name"] = i.name
        dict["bgroup"] = i.Bgroup
        dict['units'] = i.units
        dict["status"] = i.status
        l.append(dict)
    d = {'patient': l}
    return JsonResponse(d)

def patient_dashBoard(request,eml):
    obj = Blood_request.objects.filter(email=eml)
    count = 0
    approved = 0
    rejected = 0
    pending = 0
    for i in obj:
        count += 1
    for j in obj:
        if j.status == 'approved':
            approved += 1
        elif j.status == 'rejected':
            rejected += 1
        else:
            pending += 1
    return JsonResponse({'dashboard': [{'Count': count}, {'pending': pending}, {'Approved': approved},
                                       {'Rejected': rejected}]})