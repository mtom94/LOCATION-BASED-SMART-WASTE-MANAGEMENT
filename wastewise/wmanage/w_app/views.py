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
import random
from django.core.serializers import serialize
import string
from django.views.decorators.csrf import csrf_exempt
from math import radians, cos, sin, asin, sqrt
from itertools import permutations


# Create your views here.

@never_cache
def display_login(request):
	return render(request, "sign_in.html", {})

@never_cache
def forgot_p(request):
	return render(request, "forgot_password.html", {})

@never_cache
def display_reg(request):
	return render(request, "sign_up.html", {})

@never_cache
def reg_u(request):
	name = request.POST.get("name")
	email=request.POST.get("email")
	pswd= request.POST.get("password")
	addr=request.POST.get("address")
	phn=request.POST.get("phone")
	print()
	obj10 = user_d.objects.filter(
	Email=email)
	co = obj10.count()
	obj11 = Driver.objects.filter(
	drv_email=email)
	cot = obj11.count()
	if (co == 1 or cot==1):
		return HttpResponse("<script>alert('Customer Already Exist');window.location.href='/display_login/'</script>")
	else:
		kk=user_d(Name=name,Email=email,Password=pswd,Address=addr,PhoneNo=phn)
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

	obj4=Driver.objects.filter(drv_email=u_id,drv_psw=password)
	c4=obj4.count()
	
	if c3==1:
		obj5=user_d.objects.get(Email=u_id)
		name=obj5.Name
		email=obj5.Email
		request.session['uid'] = email
		request.session['uname'] = name
		request.session['em'] = email
		return HttpResponse("<script>alert('Login Successful');window.location.href='/show_home_user/';</script>")
	elif u_id=="admin@gmail.com" and password=="admin12@A":
		request.session['uname'] = "Admin"
		request.session['uid'] = "Admin"
		return HttpResponse("<script>alert('Login Successful');window.location.href='/show_home_admin/';</script>")
	elif c4==1:
		obj5=Driver.objects.get(drv_email=u_id)
		name=obj5.drv_name
		email=obj5.drv_email
		request.session['uid'] = email
		request.session['uname'] = name
		request.session['em'] = email
		return HttpResponse("<script>alert('Login Successful');window.location.href='/show_home_driver/';</script>")
	else:
		return HttpResponse("<script>alert('Invalid');window.location.href='/display_login/'</script>")
@never_cache
def logout(request):
	if 'uid' in request.session:
		del request.session['uid']
	return render(request, 'sign_in.html')

@never_cache
def change_password(request):
	email=request.POST.get('email')
	new_password=request.POST.get('password')
	obj1=user_d.objects.filter(Email=email)
	vv=obj1.count()
	obj2=Driver.objects.filter(drv_email=email)
	yy=obj2.count()
	if(vv==1):
		obj5=user_d.objects.get(Email=email)
		obj5.Password=new_password
		obj5.save()
		return HttpResponse("<script>alert('Password Changed Successfully');window.location.href='/display_login/'</script>")
	elif(yy==1):
		obj5=Driver.objects.get(drv_email=email)
		obj5.drv_psw=new_password
		obj5.save()
		return HttpResponse("<script>alert('Password Changed Successfully');window.location.href='/display_login/'</script>")
	else:
		return HttpResponse("<script>alert('No user found');window.location.href='/display_login/'</script>")

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


def generate_password():
	# Define the pool of characters
	lowercase_letters = string.ascii_lowercase
	uppercase_letters = string.ascii_uppercase
	digits = string.digits
	special_characters = string.punctuation

	# Ensure at least one character of each type
	password = random.choice(lowercase_letters)
	password += random.choice(uppercase_letters)
	password += random.choice(digits)
	password += random.choice(special_characters)

	# Fill up the remaining length
	remaining_length = 8 - len(password)
	for _ in range(remaining_length):
		password += random.choice(lowercase_letters + uppercase_letters + digits + special_characters)

	# Shuffle the password characters to make it more random
	password_list = list(password)
	random.shuffle(password_list)
	password = ''.join(password_list)

	return password

@never_cache
def add_drw_db(request):
	drv_name=request.POST.get('drv_name')
	drv_phn=request.POST.get('drv_phn')
	drv_email=request.POST.get('drv_email')
	drv_place=request.POST.get('drv_place')
	random_password = generate_password()
	drv_psw=random_password
	obj10 = Driver.objects.filter(
			drv_email=drv_email)
	co = obj10.count()
	obj11 = user_d.objects.filter(
	Email=drv_email)
	cot = obj11.count()
	if (co==1 or cot==1):
		return HttpResponse("<script>alert('Email already exists');window.location.href='/add_drivers/'</script>")
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
	S_id=request.POST.get("S_id")
	drv_name=request.POST.get('drv_name')
	drv_phn=request.POST.get('drv_phn')
	drv_email=request.POST.get('drv_email')
	drv_place=request.POST.get('drv_place')
	obj5=Driver.objects.get(S_id=S_id)
	obj5.drv_name=drv_name
	obj5.drv_phn=drv_phn
	obj5.drv_email=drv_email
	obj5.drv_place=drv_place
	obj5.save()
	return HttpResponse("<script>alert('Edited Successfully');window.location.href='/man_driver/'</script>")

@never_cache
def del_drv(request):
	S_id=request.POST.get("S_id")
	obj5=Driver.objects.get(S_id=S_id)
	obj5.delete()
	return HttpResponse("<script>alert('Deleted Successfully');window.location.href='/man_driver/'</script>")


@never_cache
def add_garbage_bins(request):
	if 'uid' in request.session:
		return render(request, 'add_garbage_bins.html')
	else:
		return render(request, 'sign_in.html')

def generate_random_code():
	chars = string.digits
	code = ''.join(random.choice(chars) for _ in range(4))
	return code

@never_cache
def add_grb_db(request):
	g_lat=request.POST.get('glat')
	g_lng=request.POST.get('glng')
	g_place=request.POST.get('plc_name')
	random_code = generate_random_code()
	obj10 = GarbageB.objects.filter(
			g_lat=g_lat,g_lng=g_lng)
	co = obj10.count()
	if (co==1):
		return HttpResponse("<script>alert('Garbage bin already exists');window.location.href='/add_garbage_bins/'</script>")
	else:   
		obj2=GarbageB(
			g_id=random_code, g_lat=g_lat,g_lng=g_lng,g_place=g_place,)
		obj2.save()
		return HttpResponse("<script>alert('Garbage Bin Added Successfull');window.location.href='/add_garbage_bins/'</script>")

@never_cache
def man_garbage_bins(request):
	if 'uid' in request.session:
		a=GarbageB.objects.all()        
		return render(request, 'man_garbage_bins.html',{'drv':a})
	else:
		return render(request, 'sign_in.html')

@never_cache
def edit_gbin(request):
	S_id=request.POST.get("S_id")
	g_lat=request.POST.get('g_lat')
	g_lng=request.POST.get('g_lng')
	obj5=GarbageB.objects.get(S_id=S_id)
	obj5.g_lat=g_lat
	obj5.g_lng=g_lng
	obj5.save()
	return HttpResponse("<script>alert('Edited Successfully');window.location.href='/man_garbage_bins/'</script>")

@never_cache
def del_gbin(request):
	S_id=request.POST.get("S_id")
	obj5=GarbageB.objects.get(S_id=S_id)
	obj5.delete()
	return HttpResponse("<script>alert('Deleted Successfully');window.location.href='/man_garbage_bins/'</script>")

@never_cache
def view_users_complaint(request):
	if 'uid' in request.session:
		a=Complaints.objects.all()      
		return render(request, 'view_users_complaint.html',{'drv':a})
	else:
		return render(request, 'sign_in.html')

@never_cache
def edit_cmp_status(request):
	S_id=request.POST.get("S_id")
	cmpsta=request.POST.get('cmpsta')
	obj5=Complaints.objects.get(S_id=S_id)
	obj5.status=cmpsta
	obj5.save()
	return HttpResponse("<script>alert('Status Updated Successfully');window.location.href='/view_users_complaint/'</script>")

@never_cache
def search_driver(request):
	if 'uid' in request.session:     
		return render(request, 'search_driver.html')
	else:
		return render(request, 'sign_in.html')

def search_places(request):
	query = request.GET.get('query', '')
	if len(query) >= 2:  # Adjust the minimum characters required for search
		matching_places = GarbageB.objects.filter(g_place__icontains=query).values('g_place')
		return JsonResponse(list(matching_places), safe=False)
	return JsonResponse([], safe=False)

@csrf_exempt
def view_place_drivers(request):
	if request.method == 'POST':
		data = json.loads(request.body.decode('utf-8'))
		# This is an AJAX request
		place = data.get('place', '')
		# Perform actions with the selected place
		print('Selected place:', place)
		# Get data related to the selected place
		a = GarbageB.objects.filter(g_place=place)
		
		# Store the data in session variable
		request.session['plc_data'] = list(a.values())  # Convert QuerySet to list of dictionaries
		
		return JsonResponse({'success': True})
	else:
		# Return an error response if the request method is not POST or not AJAX
		return JsonResponse({'error': 'Invalid request'}, status=400)

def view_place_drivers_html(request):
	# Retrieve data from session variable
	plc_data = request.session.get('plc_data', [])
	print(plc_data)
	return render(request, 'view_place_drivers.html', {'plc_data': plc_data})

@never_cache
def view_garbage_report(request):
	if 'uid' in request.session:
		a=GarbageB.objects.all()      
		return render(request, 'view_garbage_report.html',{'drv':a})
	else:
		return render(request, 'sign_in.html')

def view_garbage_refresh(request):
	if 'uid' in request.session:
		a = GarbageB.objects.all()
		print("Refreshing")
		data = [{'S_id': item.S_id, 'g_id': item.g_id, 'g_place': item.g_place, 'g_lat': item.g_lat, 'g_lng': item.g_lng, 'g_fill': item.g_fill} for item in a]
		return JsonResponse({'data': data})
	else:
		return render(request, 'sign_in.html')

def assign_work(request):
	places = GarbageB.objects.values_list('g_place', flat=True).distinct()
	drivers = Driver.objects.all()
	
	# Retrieve assigned drivers for each place and convert to strings
	driver_names_by_place = {}
	for place in places:
		assigned_drivers = GarbageB.objects.filter(g_place=place).values_list('g_drv', flat=True).distinct()
		driver_names_by_place[place] = ', '.join(assigned_drivers) if assigned_drivers else '-'

	context = {
		'places': places,
		'driver_names_by_place': driver_names_by_place,
		'drivers': drivers,
	}
	print(context)
	return render(request, 'assign_work.html', context)

def assign_db(request):
	if request.method == 'POST':
		place = request.POST.get('place')
		driver_name = request.POST.get('driver')
		ob=GarbageB.objects.filter(g_place=place)
		for i in ob:
			i.g_status="-"
			i.g_drv=driver_name
			i.save()
		return HttpResponse("<script>alert('Assigned Successfully');window.location.href='/assign_work/'</script>")
	else:
		return HttpResponse("<script>alert('Issue Occured');window.location.href='/assign_work/'</script>")


##################################################################################################################################

#Customer
@never_cache
def show_home_user(request):
	if 'uid' in request.session:
		name=request.session['uname'] 
		return render(request, 'show_home_user.html',{'name':name})
	else:
		return render(request, 'sign_in.html')

@never_cache
def user_profile(request):
	if 'uid' in request.session:
		emailll=request.session['em'] 
		asd=user_d.objects.get(Email=emailll)
		name=asd.Name
		email=asd.Email
		addr=asd.Address
		phn=asd.PhoneNo
		return render(request, 'profile_updation.html',{'name':name,'email':email,'addr':addr,'phn':phn})
	else:
		return render(request, 'sign_in.html')

@never_cache
def edit_prof(request):
	emailll=request.session['em']
	user_name=request.POST.get('us_name')
	user_email=request.POST.get('us_email')
	user_address=request.POST.get('us_addr')
	user_phone=request.POST.get('us_phn')
	obj5=user_d.objects.get(Email=emailll)
	obj5.Name=user_name
	obj5.Email=user_email
	obj5.Address=user_address
	obj5.PhoneNo=user_phone
	obj5.save()
	request.session['em']=user_email
	return HttpResponse("<script>alert('Updated Successfully');window.location.href='/user_profile/'</script>")


@never_cache
def reg_complaint(request):
	if 'uid' in request.session:
		return render(request, 'reg_complaint.html')
	else:
		return render(request, 'sign_in.html')

@never_cache
def add_cmp_db(request):
	complaint=request.POST.get('ucmp')
	c_name=request.session['uname']
	c_email=request.session['em']
	obj2=Complaints(
		c_name=c_name, c_email=c_email,complaint=complaint)
	obj2.save()
	return HttpResponse("<script>alert('Garbage Bin Added Successfull');window.location.href='/reg_complaint/'</script>")

@never_cache
def view_cm_status(request):
	if 'uid' in request.session:
		c_email=request.session['em']
		a=Complaints.objects.filter(c_email=c_email)        
		return render(request, 'view_cm_status.html',{'drv':a})
	else:
		return render(request, 'sign_in.html')

###########################################################################################################################
#Admin
@never_cache
def show_home_driver(request):
	if 'uid' in request.session:
		name=request.session['uname'] 
		return render(request, 'show_home_driver.html',{'name':name})
	else:
		return render(request, 'sign_in.html')

@never_cache
def view_works(request):
	if 'uid' in request.session:
		name=request.session['uname'] 
		pl=[]
		obj=GarbageB.objects.filter(g_drv=name)
		for i in obj:
			pl.append(i.g_place)
		unique_list = list(set(pl))
		return render(request, 'view_works.html',{'place':unique_list})
	else:
		return render(request, 'sign_in.html')

@never_cache
def work_finished(request):
	plc=request.POST.get('place')
	name=request.session['uname']
	objj=GarbageB.objects.filter(g_place=plc,g_drv=name)
	for i in objj:
		i.g_status="Completed"
		i.save()
	return HttpResponse("<script>alert('Done');window.location.href='/view_works/'</script>")
distances = {}
def haversine(lon1, lat1, lon2, lat2):
	"""
	Calculate the great circle distance between two points
	on the earth specified in radians.
	"""
	# Convert decimal degrees to radians
	lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

	# Haversine formula
	dlon = lon2 - lon1
	dlat = lat2 - lat1
	a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
	c = 2 * asin(sqrt(a))
	r = 6371  # Radius of earth in kilometers
	return c * r

def total_distance(path):
	total = 0
	for i in range(len(path)-1):
		total += distances[(path[i], path[i+1])]
	return total

def find_shortest_paths(num_paths):
	global coordinates
	all_paths = []
	for perm in permutations(range(len(coordinates))):
		path = list(perm) + [perm[0]]
		all_paths.append(path)

	all_paths.sort(key=total_distance)
	
	return all_paths[:num_paths]

def fpath():
	global coordinates
	for i in range(len(coordinates)):
		for j in range(len(coordinates)):
			if i != j:
				distances[(i, j)] = haversine(coordinates[i][1], coordinates[i][0], coordinates[j][1], coordinates[j][0])
	shortest_paths = find_shortest_paths(4)
	for i, path in enumerate(shortest_paths):
		print(f"Shortest Path {i+1}: {' -> '.join(str(p+1) for p in path)}")
		print(f"Total Distance: {total_distance(path)} km")
	return shortest_paths



@never_cache
def work_path(request):
	global coordinates
	coordinates=[]
	p1=[]
	p2=[]
	p3=[]
	p4=[]
	plc = request.POST.get('place')
	bn = GarbageB.objects.filter(g_place=plc)
	cou=bn.count()
	if cou>2:	
		for i in bn:
			a1 = float(i.g_lat)
			a2 = float(i.g_lng)
			tco = [a1, a2]  # Using a list instead of a tuple
			coordinates.append(tco)
		
		#print(coordinates)
		a=fpath()
		for k in range(0,len(a)):
			if k==0:
				s=a[k]
				for h in s:
					p1.append(coordinates[h])
			if k==1:
				s=a[k]
				for h in s:
					p2.append(coordinates[h])
			if k==2:
				s=a[k]
				for h in s:
					p3.append(coordinates[h])
			if k==3:
				s=a[k]
				for h in s:
					p4.append(coordinates[h])
		fg=[1,2,3,4]
		request.session['1']=p1
		request.session['2']=p2
		request.session['3']=p3
		request.session['4']=p4
		return render(request, 'view_fpaths.html',{'coor':fg})
	else:
		for i in bn:
			a1 = float(i.g_lat)
			a2 = float(i.g_lng)
			tco = [a1, a2]  # Using a list instead of a tuple
			coordinates.append(tco)
		fg=[1]
		request.session['1']=coordinates
		return render(request, 'view_fpaths.html',{'coor':fg})

@never_cache
def view_map_p(request):
	if 'uid' in request.session:
		path_key=request.POST.get('pathl')
		print(path_key)
		pth=request.session[path_key] 
		print(pth)
		return render(request, 'view_map_p.html',{'Coordinates':pth})
	else:
		return render(request, 'sign_in.html')




