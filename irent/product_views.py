from django.shortcuts import render_to_response
from django.http import Http404, HttpResponse
from django.shortcuts import render
from django.core.context_processors import csrf
from django.db import models
from django import forms
from forms import product_entry
from irent.models import User_registration
from irent.models import Product_registration
from irent.models import Product_category
from django.core import validators
from django.template import RequestContext

def product_add(request):
	form =product_entry()
	return render(request, 'product_add.html',{'form': form})

def product_data_add(request):
	register = Product_registration(uid=request.session['global_uid'],pc_id=request.POST.get("product_category"),product_name=request.POST.get("product_name"),product_title=request.POST.get("product_title"),product_description=request.POST.get("product_description"),rental_condition=request.POST.get("product_conditions"))						
	register.save()
	return render(request, 'page_ecom_dashboard.html')

def search_result(request):

	search_proc_name=request.POST.get("ecom-search")
	search_proc_id=Product_category.objects.filter(pc_name__icontains=search_proc_name)

	search_pro_list=Product_registration.objects.filter(pc_id=search_proc_id)
		#print(spi1.product_name)
		#search_pro_list.append(spi1)
		#pass
	#for pci in search_proc_list1:
	#	search_pro_list= Product_registration.objects.filter(pc_id=)
	#	pass
	#search_pro_list= Product_registration.objects.filter(pc_id=search_proc_id)
	#for p in search_pro_list:
	#	print (p.product_name)
	#	pass
	return render_to_response('ecom_search_results.html',{'search_pro_list':search_pro_list},context_instance=RequestContext(request))