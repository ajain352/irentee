from django.shortcuts import render_to_response
from django.http import Http404, HttpResponse
from django.shortcuts import render
from django.core.context_processors import csrf
from django.db import models
from django import forms
#from forms import SignupForm
from forms import product_entry
from irent.models import User
from irent.models import User_registration
from irent.models import Product_registration
from irent.models import Product_category
from django.core import validators
from django.template import RequestContext

login_user_email=""
temp=""
uemail=""
global_uid=0
pr_details=[]


def register(request):

	try:
		UMAIL=request.POST.get("register-email")
		UPASS=request.POST.get("register-password")
		UNAME=request.POST.get("register-firstname")
		UMOBILE=request.POST.get("register-mobile")
		UCITY=request.POST.get("register-city")
		if (UMAIL!="" and UPASS!=""):
			user = User(umail=UMAIL, upass=UPASS)
			user.save()														

			e=User.objects.get(umail=UMAIL)

			user_reg = User_registration(uid=e.uid,uname=UNAME,umobile=UMOBILE,ucity=UCITY)
			user_reg.save()
			return render(request, 'page_ecom_dashboard.html')
		pass
	except Exception, e:
		raise e

	

def show(request):
	login_user_email=request.POST.get("login-email")

	request.session['uemail']=login_user_email
	login_user_pass=request.POST.get("login-password")

	list1=[]
	list2=[]
	for e in User.objects.all():
		list1.append(e.umail)
		list2.append(e.upass)
		pass

	if login_user_email in list1:
		index_email=list1.index(login_user_email)
		index_pass=list2[index_email]
		e=User.objects.get(umail=request.session['uemail'])
		uid=e.uid
		print(uid)
		request.session['global_uid']=uid
		ee=User_registration.objects.get(uid=uid)
		print(ee.uname)
		uname=ee.uname;
		if (index_pass==login_user_pass):
			print ('Inside login')
			pr_details=[]
			pr=Product_registration.objects.filter(uid=uid)


			for p in pr:
				proc_name=Product_category.objects.get(pc_id=p.pc_id)
				p.pc_id=proc_name.pc_name
				pass

			return render(request, 'page_ecom_dashboard.html',{'list1': uname, 'pr_details':pr})
		else:
			print ('Wrond Password')
			return render_to_response("show_data.html",{'list1': 'wrong password'})
	else:
		print('User not found')
		return render_to_response("show_data.html",{'list1': 'Unknown User'})

