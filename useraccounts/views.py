# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import httplib
from lobify.settings import lobify
from django.shortcuts import render
from django.contrib.auth.models import User
from .models import messcanteen,diet,contact,urlshort,credittable
from login.models import category
from django.http import JsonResponse
from django.http import HttpResponseRedirect
import hashlib
import requests
from django.http import JsonResponse
from django.http import HttpResponse
#from selleraccounts.models import messlist,canteenlist

# Create your views here.

def userprofile(request):
    if request.method == "POST" and 'amount' in request.POST and 'remarks' in request.POST:
        cname = request.POST['cname']
        amount = request.POST['amount']
        remarks = request.POST['remarks']
        messname = messcanteen.objects.get(incharge = request.user)
        customer = User.objects.get(username = cname)
        newDiet = diet(messname = messname, customer = customer ,remarks = remarks, amount = amount)
        newDiet.save()
            
        try:
            cexist = credittable.objects.filter(messname = messname, customer = customer)
            if len(cexist) > 0:
                chkval = 1
            else:
                chkval = 0
        except credittable.DoesNotExist:
            chkval = 0
            
        except Exception,e:
            print e

        if chkval == 0:
            ccreate  = credittable(messname = messname, customer = customer, credit = 0)
            ccreate.save()
        
        cval = credittable.objects.get(messname = messname, customer = customer)
        cval.credit = int(cval.credit)-int(amount)
        cval.save()

        messname = messcanteen.objects.get(incharge = request.user)
        diets = diet.objects.filter(messname=messname).order_by("-ts")
        try:
                q = str(newDiet.id)
                link = hashlib.md5(q)
                linkval = link.hexdigest()
                u = urlshort(dietplan = newDiet, link = linkval)
                u.save()

                url = "http://2factor.in/API/V1/3def7813-0830-11e8-a996-0200cd936042/ADDON_SERVICES/SEND/TSMS"
                mob_num = cname
                amount_fin = str(amount) +"Rs"
                mess_name = messname
                link = "http://"+str(lobify) + "/mverify/?id=" + linkval
                payload={"From":"LOBIFY","To":str(mob_num),"TemplateName":"LOBIFY","VAR1":str(amount_fin),"VAR2":str(mess_name),"VAR3":str(link)}
                response = requests.request("POST", url, data=payload)
                result_js=response.json()
                print(result_js)
        except Exception,e:
                print e

        return render(request,"profile.html",{"customer": False , "messname" : messname.messcanteen , "diets": diets})

    profiletype = category.objects.get(user = request.user)
    
    if profiletype.customer == False:
        try:
            messname = messcanteen.objects.get(incharge = request.user)
            diets = diet.objects.filter(messname=messname).order_by("-ts")
            return render(request,"profile.html",{"customer": profiletype.customer , "messname" : messname.messcanteen , "diets": diets})

        except:
            return render(request,"profile.html",{"customer": profiletype.customer})

    
    else:
        diets = diet.objects.filter(customer = request.user).order_by("-ts")
        return render(request,"profile.html",{"customer": profiletype.customer,"diets": diets})

def sellerrecords(request):
    messname = messcanteen.objects.get(incharge = request.user)
    d = diet.objects.filter(messname = messname).order_by("-ts")
    hashtable =[]
    diets = []
    for data in d:
        if data.customer not in hashtable:
            hashtable.append(data.customer)
            diets.append(data)

    #cval = credittable.objects.filter(messname = messname)
    return render(request,"sellerrecords.html",{"customer": False , "messname" : messname.messcanteen , "diets": diets})


def userrecords(request):
    d = diet.objects.filter(customer=request.user)
    hashtable = []
    diets = []
    for data in d:
        if data.messname not in hashtable:
            hashtable.append(data.messname)
            diets.append(data)
    return render(request,"userrecords.html",{"customer": True, "diets": diets})



def profilesettings(request):
    profiletype = category.objects.get(user = request.user)
    if request.method == "POST" and 'mess' in request.POST:
        mess = request.POST['mess']
        user = User.objects.get(username=request.user.username)
        details = messcanteen(incharge = user, messcanteen = mess)
        details.save()
    
    if request.method == "POST" and 'mobile' in request.POST:
        mobile = request.POST['mobile']     
        user = User.objects.get(username=request.user.username)
        details = contact(username = user, mobileno = mobile)
        details.save()

    
    if profiletype.customer==False:
        try:
            usermess = messcanteen.objects.get(incharge=request.user)
            return render(request,"profilesettingsprofile.html",{"customer": profiletype.customer,"mess":usermess.messcanteen})
        except:
            return render(request,"profilesettingsprofile.html",{"customer": profiletype.customer})

    return render(request,"profilesettingsprofile.html",{"customer": profiletype.customer})



def emailsettings(request):
    user=User.objects.get(username=request.user.username)
    if request.method=="POST":
        email = request.POST['email']
        user.email= email
        user.save()
        return render(request,"profilesettingsemail.html",{"message": "Email Changed"})

    return render(request,"profilesettingsemail.html",{user: user})


#@login_required(login_url="/login/")
def passwordsettings(request):
	user=User.objects.get(username=request.user.username)
	if request.method=="POST":
		user=User.objects.get(username=request.user.username)
		pwd1=request.POST.get("newpassword").strip()
		pwd2=request.POST.get("confirmnewpassword").strip()
		opwd=request.POST.get("oldpassword").strip()
		if pwd1 and pwd2 and opwd:
			if pwd1==pwd2:
				if user.check_password(opwd):
					user.set_password(pwd1)
					user.save()
					return render(request,"profilesettingspassword.html",{"message": "Password Changed"})

	return render(request,"profilesettingspassword.html")


def searchuser(request):
    query = request.GET.get('query')
    users = User.objects.filter(username__contains = query)
    return render(request,"searchresults.html",{"users" : users})

def userbills(request):
    query = request.GET.get('username')
    user = User.objects.get(username = query)
    diets = diet.objects.filter(customer = user).order_by("-ts")
    return render(request,"searchresults.html",{"diets" : diets,"mobile":query})


def messwise(request):
    data = diet.objects.filter(customer=request.user).order_by('messname')
    return render(request, "messwiselist.html",{"diets":data})


def profilepicturesettings(request):
    return render(request,"profilesettingspicture.html")



def loginajax(request):
	username = request.GET.get('cname')

	data={
            'user' : User.objects.filter(username__iexact=username).exists()
         }
	return JsonResponse(data)

def paymentdone(request):
    userid = request.GET['id']

    paiddiet = diet.objects.get(id=userid)
    paiddiet.payment = True
    paiddiet.save()

    messname = messcanteen.objects.get(incharge = request.user)
    diets = diet.objects.filter(messname=messname).order_by("-ts")
    return render(request,"sellerrecords.html",{"customer": False , "messname" : messname.messcanteen , "diets": diets})


def verifydiet(request):
    userid = request.GET['id']

    verifydiet = diet.objects.get(id=userid)
    verifydiet.verified = True
    verifydiet.save()

    diets = diet.objects.filter(customer=request.user)
    return render(request,"userrecords.html",{"customer": True, "diets": diets})


def messagedietverification(request):
    dietid = request.GET['id']
    urlobj = urlshort.objects.get(link = dietid)
    d = diet.objects.get(id= urlobj.dietplan.id)
    d.verified = True
    d.save()
    return HttpResponse("Success!! Your item has been verified!!")



def viewdetailsmesswise(request):
    mess = request.GET['messwise']
    messdet = messcanteen.objects.get(messcanteen = mess)
    diets = diet.objects.filter(messname = messdet, customer = request.user)
    return render(request, "messdetails.html",{"diets":diets, "messname" : mess})

def addmoney(request):
    if request.method == "POST":
        mess = request.POST['messname']
        amount = request.POST['amount']
        mname = messcanteen.objects.get(messcanteen = mess)
        mob_num = User.objects.get(username = mname.incharge)
        print mob_num

        c = credittable.objects.get(customer = request.user, messname = mname)
        c.credit = int(amount) + int(c.credit)
        c.save()

        try:
            q = str(c.id)
            link = hashlib.md5(q)
            linkval = link.hexdigest()
            #u = urlshort(dietplan = newDiet, link = linkval)
            #u.save()

            url = "http://2factor.in/API/V1/3def7813-0830-11e8-a996-0200cd936042/ADDON_SERVICES/SEND/TSMS"
            link = "http://"+str(lobify) + "/adverify/?id=" + linkval
            payload={"From":"LOBIFY","To":str(mob_num),"TemplateName":"usercredit","VAR1":str(request.user.username),"VAR2":str(amount),"VAR3":str(link)}
            response = requests.request("POST", url, data=payload)
            result_js=response.json()
            print(result_js)
        except Exception,e:
                print e


        return HttpResponseRedirect('/userhome/')


def messageadvverification(request):
    return HttpResponse("Success!! Your item has been verified!!")

