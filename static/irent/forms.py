from django import forms
from django.core import validators
from django.db import models
from irent.models import Product_category

#class SignupForm(forms.Form):
    #register_firstname = forms.CharField(label='First name', max_length=100, 
    #									 widget=forms.TextInput(attrs={'placeholder': 'First name','class':'form-control input-lg'}))

    #register_email = forms.CharField(label='Email', max_length=100, 
    #									 widget=forms.TextInput(attrs={'placeholder': 'Email','id': 'register-email','class':'form-control input-lg'}))

    #register_pass = forms.CharField(label='Password', max_length=100, 
    #									 widget=forms.PasswordInput(attrs={'placeholder': 'Password','id': 'register-password','class':'form-control input-lg'}))

    #register_mobile = forms.CharField(label='VPassword', max_length=100, 
    #									 widget=forms.TextInput(attrs={'placeholder': 'Mobile No','id': 'register-password-verify','class':'form-control input-lg'}))

    #register_city = forms.CharField(label='VPassword', max_length=100, 
    #                                     widget=forms.TextInput(attrs={'placeholder': 'City','id': 'register-password-verify','class':'form-control input-lg'}))

    #login_email = forms.CharField(label='Email', max_length=100, 
    #									 widget=forms.TextInput(attrs={'placeholder': 'Email','id': 'login-email','class':'form-control input-lg'}))

    #login_pass = forms.CharField(label='Password', max_length=100, 
    #									 widget=forms.PasswordInput(attrs={'placeholder': 'Password','class':'form-control input-lg'}))

class product_entry(forms.Form):
    product_name=forms.CharField(label='Product Name', max_length=100, 
                                         widget=forms.TextInput(attrs={'placeholder': 'Enter Product  Name..','class':'form-control'}))
    
    product_title=forms.CharField(label='Product Title', max_length=100, 
                                         widget=forms.TextInput(attrs={'placeholder': 'Enter Ad Title..','class':'form-control'}))
    
    product_category=forms.CharField(label='First name', max_length=100, 
                                        widget=forms.TextInput(attrs={'placeholder': 'First name','class':'form-control input-lg'}))

    product_description=forms.CharField(label='First name', max_length=100, 
                                         widget=forms.Textarea(attrs={'placeholder': 'product-description','rows':'3','class':'form-control input-lg'}))

    product_conditions=forms.CharField(label='First name', max_length=100, 
                                         widget=forms.Textarea(attrs={'placeholder': 'Conditions to renting out this product.','rows':'3','class':'form-control input-lg'}))

    product_photo1=forms.ImageField()
    choice=[]
    choice = tuple(Product_category.objects.all().values_list())
    product_category=forms.ChoiceField(choices=choice, 
                                        widget=forms.Select(attrs={'placeholder': 'Conditions','class':'select-chosen'}))
