from rest_framework import viewsets
from .models import Student
from .serializers import StudentSerializer
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser,AllowAny,IsAuthenticatedOrReadOnly,DjangoModelPermissions,DjangoModelPermissionsOrAnonReadOnly

class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [SessionAuthentication]
    # permission_classes = [IsAuthenticated]
    # permission_classes = [AllowAny]
    # permission_classes = [IsAdminUser] #api is accessed by those users who stuf status = true.
    #IsAuthenticatedOrReadOnly api - autheticate user can do everything(read,write) but unauthenticate user can do only read
    # permission_classes = [IsAuthenticatedOrReadOnly] 
    # permission_classes = [DjangoModelPermissions]
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]