from django.db import models

# Create your models here.
class Employee(models.Model):
    name=models.CharField(max_length=30)

class Department(models.Model):
    dept_id=models.CharField(max_length=20)
    name=models.CharField(max_length=30)
    manager=models.ForeignKey(Employee,on_delete=models.CASCADE)

        
