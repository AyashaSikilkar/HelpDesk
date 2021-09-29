from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Numbers,Covid,districtdata,Emergency,Manchar,Contact,DepartmentData,ElectricalData,ScienceData,CivilData,MechanicalData,ITData,sales
import requests
from django.core.mail import send_mail
from django.conf import settings
from django.db.models import Q
from django.contrib import messages

url = "https://www.fast2sms.com/dev/bulk"
headers = {
            'authorization': "G4RHY7v3bBuOWxdCgXIAe2fJQqFTarEnzotwVc61KypSjMLkmNsmjyzYCVBI9U7pSGbaETN3vRcetnr2",
            'Content-Type': "application/x-www-form-urlencoded",
            'Cache-Control': "no-cache",
          }

# Created views here.
def home(request):
    return render(request,"index.html", context=None)

def Emergency1(request):
    number1=Emergency.objects.all()
    num = {
        'no':number1
    }
    return render(request,"Emergency.html",context=num)

def ClgCampus(request):#computer
    numbers=Numbers.objects.all()
    num = {
               'no':numbers
    }
    return render(request,"Dept.html",context=num)
 
def MancharNos(request):
    number=Manchar.objects.all()
    num = {
        'no':number
    }
    return render(request,"Manchar.html",context=num)

def ITDept(request):#IT
    numbers=ITData.objects.all()
    num = {
        'no':numbers
    }
    return render(request,"Dept.html",context=num)

def CivilDept(request):#Civil
    numbers=CivilData.objects.all()
    num = {
        'no':numbers
    }
    return render(request,"Dept.html",context=num)

def MechanicalDept(request):#Mechanical
    numbers=MechanicalData.objects.all()
    num = {
        'no':numbers
    }
    return render(request,"Dept.html",context=num)

def ElectricalDept(request):#ElectricalDept
    numbers=ElectricalData.objects.all()
    num = {
        'no':numbers
    }
    return render(request,"Dept.html",context=num)

def ScienceDept(request):#ScienceDept
    numbers=ScienceData.objects.all()
    num = {
        'no':numbers
    }
    return render(request,"Dept.html",context=num)

def AboutUs(request):
    return render(request,"Aboutus.html", context=None)


def contact(request):
    if request.method=="POST":
        print(request)
        name=request.POST.get('name', '')
        email=request.POST.get('email', '')
        phone=request.POST.get('phone', '')
        city=request.POST.get('city', '')
        desc=request.POST.get('desc', '')
        contact = Contact(name=name, email=email, phone=phone,  desc=desc)
        contact.save()

        email = request.POST['email']
        desc = request.POST['desc']
        send_mail(
            'Thanks for connect with with us!!! We will let u soon',
            desc,
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False,
        )
        messages.success(request,"Thanks for contacting us!!")
    return render(request, "ContactUs.html")

def SearchFunction(request):
    if request.method=="POST":
        
        name = request.POST.get('search', '')
        
        numbers=ElectricalData.objects.all().filter(Q(mobileno = name) |Q(title=name)| Q(fname = name))
        getresult = Numbers.objects.all().filter(Q(mobileno = name) |Q(title=name)| Q(fname = name))
        emergency=Emergency.objects.all().filter(Q(title=name)|Q(mobileno = name))
        manchar=Manchar.objects.all().filter(Q(title=name)|Q(mobileno = name))
        it=ITData.objects.all().filter(Q(mobileno = name) | Q(title=name)|Q(fname = name))
        civil=CivilData.objects.all().filter(Q(mobileno = name) | Q(title=name)|Q(fname = name))
        mechanical=MechanicalData.objects.all().filter(Q(mobileno = name) | Q(title=name)|Q(fname = name))
        science=ScienceData.objects.all().filter(Q(mobileno = name) | Q(title=name)|Q(fname = name))
        
        print(name)
        num = {
            'civil':civil,
            'numbers':numbers,
            'no':getresult,
            'it':it,
            'mechanical':mechanical,
            'science':science,
            'emergency':emergency,
            'manchar':manchar
        }
        return render(request,"Numbers.html",context=num)

def covid(request):
        name = request.POST.get('search', '')
        data=True
        result=None
        globalsummary = None
        districts=None
        name=name.capitalize()
        while(data):
            try:
                districts=name
                result=requests.get("https://api.covid19india.org/state_district_wise.json");
                globalsummary=result.json()["Maharashtra"]
                dis = districtdata.objects.all()
                covid = Covid.objects.all()
                data = False
            except:
                data = True
        return render(request,"Covid19.html",{'globalsummary':globalsummary,'districts':districts,"num":dis,"covid":covid})

def sms(request):
    try:
        if request.method == "POST":
            
            name = request.POST.get('search', '')
            name = name.title()
            getresult = Numbers.objects.all().filter(fname=name)
            emergency=Emergency.objects.all().filter(Q(title=name)|Q(mobileno = name))
            manchar=Manchar.objects.all().filter(Q(title=name)|Q(mobileno = name)|Q(fname=name))
            it=ITData.objects.all().filter(Q(mobileno = name) | Q(fname = name))
            civil=CivilData.objects.all().filter(Q(mobileno = name) | Q(fname = name))
            mechanical=MechanicalData.objects.all().filter(Q(mobileno = name) | Q(fname = name))
            science=ScienceData.objects.all().filter(Q(mobileno = name) | Q(fname = name))
            electrical=ElectricalData.objects.all().filter(Q(mobileno = name) | Q(fname = name))
            print(getresult)
            a=""
            number = request.POST['number']
            if Manchar.objects.all().filter(fname=name).exists():
                for num in manchar:
                    a=num.mobileno
                    print("Mobile Number",a)
            if Emergency.objects.all().filter(title=name).exists():
                for num in emergency:
                    a=num.mobileno
                    print("Mobile Number",a)
            if Numbers.objects.all().filter(fname=name).exists():
                for num in getresult:
                    a=num.mobileno
                    name=num.fname
            if ITData.objects.all().filter(fname=name).exists():
                for num in it:
                    a=num.mobileno
                    name=num.fname
            if CivilData.objects.all().filter(fname=name).exists():
                for num in civil:
                    a=num.mobileno
                    name=num.fname
            if MechanicalData.objects.all().filter(fname=name).exists():
                for num in mechanical:
                    a=num.mobileno
                    name=num.fname
            if ScienceData.objects.all().filter(fname=name).exists():
                for num in science:
                    a=num.mobileno
                    name=num.fname
            if ElectricalData.objects.all().filter(fname=name).exists():
                for num in electrical:
                    a=num.mobileno
                    name=num.fname

            data=str(name)  
            if len(a)!=0 and len(number)==10:
                print(getresult)
                search="HELPDESKGPA\n\nMobile Number of "+name+" is "+str(a)+"\n\n Thanks For Using our Services\n\n "      
                phone = str(number)
            
                #msg="Hello"        
                payload = {     
                        'sender_id': 'FSTSMS',     
                            'message': search,               
                            'language': 'english',
                            'route': 'p',                
                            'numbers': phone    
                        }
                response = requests.request("POST", url, data=payload, headers=headers)
                print(search)
                print(response.text)
                messages.success(request,"Requested Data Sent One Your provided phone number Successfully!!!")
            else:
                messages.warning(request,"Message Could Not be Sent on Provided Number!!")
       
    except Exception:
        print("") 
        messages.warning(request,"Exception Message Could Not be Sent on Provided Number!!")
    return render(request, 'index.html')
