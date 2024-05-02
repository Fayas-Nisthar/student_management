from rest_framework import viewsets,permissions
from rest_framework_simplejwt import authentication
from .models import Student, Department
from .serializers import StudentSerializer, DepartmentSerializer

class DepartmentViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAdminUser]
    authentication_classes=[authentication.JWTAuthentication]
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    

class StudentViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAdminUser]
    authentication_classes=[authentication.JWTAuthentication]
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

