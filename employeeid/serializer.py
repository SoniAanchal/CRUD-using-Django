#mobile app/ web app etc with the ability to communicate with api 
#Two way communication api<=> mobile app/ web app etc . data will be in JSON /XML format
#here we will be using json data format
#conversion: python->JSON->python

from rest_framework import serializers
from .models import Employee

class EmployeeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'
