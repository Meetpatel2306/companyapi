from django.shortcuts import render
from rest_framework import viewsets
from api.models import company,employee
from api.serializers import companyS,employeeS
from rest_framework.decorators import action
from rest_framework.response import Response
# Create your views here.

class companyV(viewsets.ModelViewSet):
    queryset=company.objects.all()
    serializer_class=companyS
# pk=primary key
    # companies/{companyID}/employees
    @action(detail=True,methods=['get'])
    def employees(self,request,pk=None):
        try:
            Company=company.objects.get(pk=pk)
            employees = employee.objects.filter(company=Company)
            employees_serializer=employeeS(employees,many=True,context={'request':request})
            return Response(employees_serializer.data)
        except Exception as e:
            print(e)
            return Response({
                'message':'company might not exists'
            })
class employeeV(viewsets.ModelViewSet):
    queryset=employee.objects.all()
    serializer_class=employeeS