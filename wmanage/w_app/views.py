from django.shortcuts import render
import threading
import json
import requests
from django.core import serializers
from .models import *
from django.db.models import Count
from django.http import HttpResponse, JsonResponse
from django.db.models import Q
from django.db.models import Count
from django.views.decorators.cache import never_cache
from django.core.files.storage import FileSystemStorage
import os
import datetime
import re
from datetime import datetime
import os

# Create your views here.

@never_cache
def display_login(request):
	return render(request, "sign_in.html", {})

@never_cache
def display_reg(request):
	return render(request, "sign_up.html", {})

@never_cache
def reg_u(request):
	name = request.POST.get("name")
	email=request.POST.get("email")
	pswd= request.POST.get("pswd")
	obj10 = user_d.objects.filter(
	Email=email)
	co = obj10.count()
	if co == 1:
		return HttpResponse("<script>alert('User Already Exist');window.location.href='/display_login/'</script>")
	else:
		kk=user_d(Name=name,Email=email,Password=pswd)
		kk.save()
		return HttpResponse("<script>alert('Registered Successfully');window.location.href='/display_login/'</script>")	


@never_cache
def check_login(request):
	u_id = request.POST.get("email")
	password = request.POST.get("password")
	print(u_id)
	print(password)
	obj3=user_d.objects.filter(Email=u_id,Password=password)
	c3=obj3.count()
	
	if c3==1:
		obj5=user_d.objects.get(Email=u_id)
		name=obj5.Name
		email=obj5.Email
		request.session['uid'] = email
		request.session['uname'] = name
		request.session['em'] = email
		return HttpResponse("<script>alert('Login Successful');window.location.href='/show_home_user/';</script>")
	elif u_id=="admin@gmail.com" and password=="admin":
		request.session['uname'] = "Admin"
		request.session['uid'] = "Admin"
		return HttpResponse("<script>alert('Login Successful');window.location.href='/show_home_admin/';</script>")
	else:
		return HttpResponse("<script>alert('Invalid');window.location.href='/display_login/'</script>")
@never_cache
def logout(request):
	if 'uid' in request.session:
		del request.session['uid']
	return render(request, 'sign_in.html')

#################################################################################################################################

#Admin
@never_cache
def show_home_admin(request):
	if 'uid' in request.session:
		name=request.session['uname'] 
		return render(request, 'admin_index.html',{'name':name})
	else:
		return render(request, 'sign_in.html')


@never_cache
def add_drivers(request):
	if 'uid' in request.session:
		return render(request, 'add_drivers.html')
	else:
		return render(request, 'sign_in.html')

@never_cache
def add_drw_db(request):
	drv_name=request.POST.get('drv_name')
	drv_phn=request.POST.get('drv_phn')
	drv_email=request.POST.get('drv_email')
	drv_place=request.POST.get('drv_place')
	drv_psw=request.POST.get('drv_psw')
	obj10 = Driver.objects.filter(
			drv_email=drv_email)
	co = obj10.count()
	if co==1:
		return HttpResponse("<script>alert('Driver already added');window.location.href='/add_drivers/'</script>")
	else:	
		obj2=Driver(
			drv_name=drv_name, drv_phn=drv_phn,drv_email=drv_email,drv_psw=drv_psw,
			drv_place=drv_place)
		obj2.save()
		return HttpResponse("<script>alert('Driver Added Successfull');window.location.href='/add_drivers/'</script>")


@never_cache
def man_driver(request):
	if 'uid' in request.session:
		a=Driver.objects.all()		
		return render(request, 'man_driver.html',{'drv':a})
	else:
		return render(request, 'sign_in.html')

@never_cache
def edit_drv(request):
	S_id=request.POST.get("S_iddd")
	drv_name=request.POST.get('drv_name')
	drv_phn=request.POST.get('drv_phn')
	drv_email=request.POST.get('drv_email')
	drv_place=request.POST.get('drv_place')
	drv_psw=request.POST.get('drv_psw')
	obj5=Driver.objects.get(S_id=int(S_id))
	obj5.drv_name=drv_name
	obj5.drv_phn=drv_phn
	obj5.drv_email=drv_email
	obj5.drv_place=drv_place
	obj5.drv_psw=drv_psw
	obj5.save()
	return HttpResponse("<script>alert('Edited Successfully');window.location.href='/man_driver/'</script>")

@never_cache
def del_drv(request):
	S_id=request.POST.get("S_iddd")
	obj5=Driver.objects.get(S_id=int(S_id))
	obj5.delete()
	return HttpResponse("<script>alert('Deleted Successfully');window.location.href='/man_driver/'</script>")
##################################################################################################################################

#Customer
@never_cache
def show_home_user(request):
	if 'uid' in request.session:
		name=request.session['uname'] 
		return render(request, 'show_home_user.html',{'name':name})
	else:
		return render(request, 'sign_in.html')