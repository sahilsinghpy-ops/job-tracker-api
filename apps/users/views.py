from rest_framework.generics import CreateAPIView, RetrieveAPIView
from .models import User
from .serializers import registerUserSerializer,UserSerilzation
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
class RegisterView(CreateAPIView):
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    serializer_class = registerUserSerializer

class UserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request):
        serilation = UserSerilzation(request.user)
        return Response(serilation.data)