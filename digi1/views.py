from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.http import HttpResponse

from digi1.models import Departments,Employees
from digi1.serializers import DepartmentSerializer,EmployeeSerializers
# Create your views here.

@csrf_exempt
def departmentApi(request,id=0):
    if request.method=='GET':
        departments = Departments.objects.all()
        departments_serializer = DepartmentSerializer(departments,many=True)
        return JsonResponse(departments_serializer.data,safe=False)
    elif request.method=='POST':
        department_data=JSONParser().parse(request)
        departments_serializer=DepartmentSerializer(data=department_data)
        if departments_serializer.is_valid():
            departments_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse('Failed to Add',safe=False)
    elif request.method == 'PUT':
        department_data = JSONParser().parse(request)
        department = Departments.objects.get(DepartmentId=department_data['DepartmentId']) 
        departments_serializer=DepartmentSerializer(department,data=department_data)
        if departments_serializer.is_valid():
            departments_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse('Failed to Update',safe=False)
    elif request.method=='DELETE':
        department=Departments.objects.get(DepartmentId=id)
        department.delete()
        return JsonResponse("Deleted Successfully",safe=False)

@csrf_exempt
def employeeApiGet(request,id=0):
    if request.method=='GET':
        employee = Employees.objects.all()
        employee_serialize = EmployeeSerializers(employee,many=True)
        return JsonResponse(employee_serialize.data,safe=False)

@csrf_exempt
def employeeApiPost(request,id=0):
    if request.method=='POST':
        employee_data = JSONParser().parse(request)
        employee_serialize = EmployeeSerializers(data=employee_data)
        if employee_serialize.is_valid():
            employee_serialize.save()
            return JsonResponse('Data Added',safe=False)
        return JsonResponse('Data Failed')
        
@csrf_exempt
def employeeApiPut(request,id=0):
    if request.method=='PUT':
        employee_data = JSONParser().parse(request)
        employee = Employees.objects.get(EmployeeId=employee_data['EmployeeId'])
        employee_serialize = EmployeeSerializers(employee,data=employee_data)
        if employee_serialize.is_valid():
            employee_serialize.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse('Failed to Update',safe=False)
        

@csrf_exempt
def employeeApiDel(request,id=0):
    if request.method=='DELETE':
        employee = Employees.objects.get(EmployeeId=id)
        employee.delete()
        return JsonResponse("Deleted Successfully",safe=False)
       
