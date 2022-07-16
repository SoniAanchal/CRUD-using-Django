from employeeid.viewsets import EmployeeViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('employee', EmployeeViewset)

#localhost:p/api/employee/5
#Basic web methods for restful api: GET, POST, PUT, DELETE
#GET function will be mapped either to the list or retrive function

