from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .models import Student
from .serializers import StudentSerializer

# Create your views here.

#List and create api,pk not required
class LCStudentAPI(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


#Retrieve,Update,delete, pk required    
class PUDStudentAPI(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer   