from django.db import models

# Create your models here.

class Employee(models.Model):
    fullname = models.CharField(max_length=100)
    emp_code = models.CharField(max_length=3)
    mobile = models.CharField(max_length=15)

#CREATE/ INSERT/ ADD (A new record inside the table) -POST
#RETRIEVE/ FETCH - GET
#UPDATE/ EDIT (Update the record using the primary key) -PUT
#DELETE/ REMOVE (delete the record) - DELETE (Web method)

