from django.db import models

# Create your models here.
class user_d(models.Model):
    S_id=models.IntegerField(primary_key=True)
    Name=models.CharField(max_length=255)
    Email=models.CharField(max_length=255)
    Password=models.CharField(max_length=255)

class Driver(models.Model):
    S_id=models.IntegerField(primary_key=True)
    drv_name=models.CharField(max_length=255)
    drv_phn=models.CharField(max_length=255)
    drv_email=models.CharField(max_length=255)
    drv_place=models.CharField(max_length=255)
    drv_psw=models.CharField(max_length=255)
class Complaints(models.Model):
    S_id = models.IntegerField(primary_key=True)
    c_name= models.CharField(max_length=255)
    c_email=models.CharField(max_length=400)
    status = models.CharField(max_length=255,default="-")
class GarbageB(models.Model):
    S_id= models.IntegerField(primary_key = True)
    g_id= models.CharField(max_length=255)
    g_lat=models.CharField(max_length=255)
    g_lng=models.CharField(max_length=255)
    g_fill=models.CharField(max_length=255,default="-")
    g_status=models.CharField(max_length=255,default="-")
    g_place=models.CharField(max_length=255)
    g_drv=models.CharField(max_length=255,default="-")