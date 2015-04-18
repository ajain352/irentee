from django.db import models

# Create your models here.
class User(models.Model):
	uid = models.AutoField(primary_key=True)
	umail = models.EmailField(max_length=30, unique=True)
	upass = models.CharField(max_length=30)
	class Meta:
		db_table = "users"

class User_registration(models.Model):
	uid=models.IntegerField()
	uname=models.CharField(max_length=50)
	umobile=models.CharField(max_length=12, null=True)
	ucity=models.CharField(max_length=50, null=True)
	class Meta:
		db_table="users_registration"

class Product_category(models.Model):
	pc_id=models.AutoField(primary_key=True)
	pc_name=models.CharField(max_length=70)
	class Meta:
		db_table="product_category"

class Product_registration(models.Model):
	uid=models.IntegerField()
	product_id=models.AutoField(primary_key=True)
	product_name=models.CharField(max_length=30)
	pc_id=models.IntegerField()
	product_title=models.CharField(max_length=100)
	product_description=models.CharField(max_length=500)
	rental_condition=models.CharField(max_length=500)
	product_photo=models.ImageField('img', upload_to='path/', blank=True)
	class Meta:
		db_table="product_registration"