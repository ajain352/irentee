from django.shortcuts import render_to_response
from django.http import Http404, HttpResponse
from django.shortcuts import render
from django.core.context_processors import csrf
from django.db import models
from irent.models import Product_registration
from django.template import RequestContext

def home(request):
	pro_last3_entry= Product_registration.objects.all().order_by('-product_id')[:3]
	return render_to_response('index_boxed_parallax.html', {'list1':pro_last3_entry},context_instance=RequestContext(request))