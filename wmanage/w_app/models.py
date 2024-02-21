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