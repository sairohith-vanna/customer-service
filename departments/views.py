from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from departments.models import Department

from departments.serializers import DepartmentSerializer

class Departments(APIView):

    def post(self, request):
        print('Request data', request.data)
        serializer = DepartmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request):
        dep_qset = Department.objects.all()
        serializer = DepartmentSerializer(dep_qset, many=True)
        return serializer.data
        