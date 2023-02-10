from django.urls import re_path as url
from digi1 import views



urlpatterns=[
    url(r'^department$',views.departmentApi),
    url(r'^department/([0-9]+)$',views.departmentApi),

    url(r'^employeeGet$',views.employeeApiGet),
    url(r'^employeePut$',views.employeeApiPut),
    url(r'^employeePost$',views.employeeApiPost),
    url(r'^employeeDel/id=([0-9]+)$',views.employeeApiDel),

]


