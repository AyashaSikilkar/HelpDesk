from django.db import models

# Create your models here.
class Numbers(models.Model):
    title = models.CharField(max_length=200)
    fname = models.CharField(max_length=200, default='Pratik',editable=True)
    lname =  models.CharField(max_length=200, default='Pratik',editable=True)
    mobileno = models.CharField(max_length=200)
    mail = models.CharField(max_length=200)
    desc = models.CharField(max_length=200, default='...',editable=True)
    def _str_(self):
        return self.title

class DepartmentData(models.Model):
    dept  = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    fname = models.CharField(max_length=200, default='',editable=True)
    lname =  models.CharField(max_length=200, default='',editable=True)
    mobileno = models.CharField(max_length=200)
    mail = models.CharField(max_length=200)
    desc = models.CharField(max_length=200, default='...',editable=True)

class ITData(models.Model):
    dept  = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    fname = models.CharField(max_length=200, default='',editable=True)
    lname =  models.CharField(max_length=200, default='',editable=True)
    mobileno = models.CharField(max_length=200)
    mail = models.CharField(max_length=200)
    desc = models.CharField(max_length=200, default='...',editable=True)

class MechanicalData(models.Model):
    dept  = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    fname = models.CharField(max_length=200, default='',editable=True)
    lname =  models.CharField(max_length=200, default='',editable=True)
    mobileno = models.CharField(max_length=200)
    mail = models.CharField(max_length=200)
    desc = models.CharField(max_length=200, default='...',editable=True)

class ElectricalData(models.Model):
    dept  = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    fname = models.CharField(max_length=200, default='',editable=True)
    lname =  models.CharField(max_length=200, default='',editable=True)
    mobileno = models.CharField(max_length=200)
    mail = models.CharField(max_length=200)
    desc = models.CharField(max_length=200, default='...',editable=True)

class CivilData(models.Model):
    dept  = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    fname = models.CharField(max_length=200, default='',editable=True)
    lname =  models.CharField(max_length=200, default='',editable=True)
    mobileno = models.CharField(max_length=200)
    mail = models.CharField(max_length=200)
    desc = models.CharField(max_length=200, default='...',editable=True)

class ScienceData(models.Model):
    dept  = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    fname = models.CharField(max_length=200, default='',editable=True)
    lname =  models.CharField(max_length=200, default='',editable=True)
    mobileno = models.CharField(max_length=200)
    mail = models.CharField(max_length=200)
    desc = models.CharField(max_length=200, default='...',editable=True)
    
class Emergency(models.Model):
    title = models.CharField(max_length=200)
    mobileno = models.CharField(max_length=200)
    mail = models.CharField(max_length=200)
    desc = models.CharField(max_length=200, default='...',editable=True)
   
class Manchar(models.Model):
    title = models.CharField(max_length=200)
    fname = models.CharField(max_length=200)
    lname =  models.CharField(max_length=200)
    mobileno = models.CharField(max_length=200)
    mail = models.CharField(max_length=200)
    desc = models.CharField(max_length=200, default='...',editable=True)

class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=70, default="")
    desc = models.CharField(max_length=500, default="")
    def _str_(self):
        return self.name

class sales(models.Model):
    item = models.CharField(max_length=50)
    price = models.CharField(max_length=70, default="")
    

class districtdata(models.Model):
    district_id=models.AutoField
    district_name=models.CharField(max_length=100)
    image=models.ImageField(upload_to='Services/images',default="")

class Covid(models.Model):
    name = models.CharField(max_length=50)
    mobileno = models.CharField(max_length=70, default="")