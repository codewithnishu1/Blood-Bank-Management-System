from django.http import HttpResponse, JsonResponse
from Bloodmanager.models import Blood_request
from donor.models import Donor, Blood_Donate

def donor_dashboard(request,em):
    c = Blood_request.objects.filter(email=em)
    count = 0
    pending = 0
    approved = 0
    rejected = 0
    for i in c:
        count = count+1
    for j in c:
       if j.status == "pending":
           pending = pending+1
       elif j.status == "approved":
           approved = approved+1
       else:
           rejected = rejected+1
    return JsonResponse({'dashboard': [{'Count': count}, {'pending': pending}, {'Approved': approved},
                                       {'Rejected': rejected}]})
    # return HttpResponse(em)

def Donate_Blood(request):
    name=request.GET.get("donor")
    email=request.GET.get("email")
    age = request.GET.get("age")
    bloodgroup = request.GET.get("bloodgroup")
    unit = request.GET.get("unit")
    date = request.GET.get("date")
    s=Blood_Donate()
    s.donor=name
    s.email=email
    s.age=age
    s.bloodgroup=bloodgroup
    s.unit=unit
    s.date=date
    s.save()
    l = []
    for i in Blood_Donate.objects.filter(email=email):
        dict = {}
        dict['donor_id'] = i.id
        dict["donor_name"] = i.name
        dict["Bgroup"] = i.Bgroup
        l.append(dict)
    d = {'donor': l}
    return JsonResponse(d)
    # return HttpResponse('donation request made is successful')

def donation_history(request,email):
    # email = request.POST.get('email')
    # obj = Blood_request.objects.filter(email=email)
    l = []
    for i in Blood_Donate.objects.filter(email=email):
        dict = {}
        dict['donor_id'] = i.id
        dict["donor_name"] = i.donor
        dict["bgroup"] = i.bloodgroup
        dict['unit'] = i.unit
        l.append(dict)
    d = {'donor': l}
    return JsonResponse(d)

def request_blood(request):
    if request.method == "POST":
        name = request.POST.get('name')
        eml = request.POST.get('email')
        bg = request.POST.get('bgroup')
        unit = request.POST.get('unit')
        obj = Blood_request()  # admin class object
        obj.name = name
        obj.email = eml
        obj.Bgroup = bg
        obj.unit = unit
        obj.save()
        l=[]
        for i in Blood_request.objects.filter(email=eml):
            dict={}
            dict['donor_id'] = i.id
            dict["donor_name"] = i.name
            dict["Bgroup"] = i.Bgroup
            l.append(dict)
        d = {'donor': l}
        return JsonResponse(d)
        # return HttpResponse('request made is successful')
        # return redirect('/request-history.html/')


def request_history(request,eml):
    eml = request.POST.get('email')
    obj = Blood_request.objects.filter(email=eml)
    l = []
    for i in request_blood.objects.filter(email=eml):
        dict = {}
        dict['donor_id'] = i.id
        dict["donor_name"] = i.name
        dict["bgroup"] = i.Bgroup
        dict['units'] = i.units
        l.append(dict)
    d = {'donor': l}
    return JsonResponse(d)


def donor_signup(request):
    if request.method == "POST":
        name = request.POST.get('donor-name')
        email = request.POST.get('donor-email')
        password = request.POST.get('donor-password')
        age = request.POST.get('donor-age')
        state = request.POST.get('donor-state')
        district = request.POST.get('donor-district')
        mobile_no = request.POST.get('donor-mob')
        Bgroup = request.POST.get('donor-bgroup')
        try:
            obj = Donor.objects.get(email=email)
        except Donor.DoesNotExist:
            # return HttpResponse('No admin profile found')
            obj = Donor()  # it is object of patient class
            obj.name = name
            obj.email = email
            obj.password = password
            obj.Bgroup = Bgroup
            obj.age = age
            obj.mobile_no = mobile_no
            obj.state = state
            obj.district = district
        obj.save()
        return HttpResponse('donor-login page')
    return HttpResponse('Please try again')


def donor_login(request):
    if request.method == "POST":
        email = request.POST.get('donor-email')
        password = request.POST.get('donor-password')
        print(email, password)
        try:
            obj = Donor.objects.get(email=email)
        except Donor.DoesNotExist:
            return HttpResponse('No donor profile found')
        if obj.password != password:
            return HttpResponse('incorrect password')
        # return redirect('donor-dashboard/')
        return HttpResponse('Login Successful')