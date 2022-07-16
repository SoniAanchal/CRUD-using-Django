from rest_framework import viewsets
from . import models
from . import serializer

class EmployeeViewset(viewsets.ModelViewSet):
    queryset = models.Employee.objects.all()
    serializer_class = serializer.EmployeeSerializers            #for JSON conversion

#list(), retrieve(), create(), update(), destroy()

