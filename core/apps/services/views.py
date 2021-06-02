from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from core.apps.app.models import Todo
from core.apps.services.serializers import TodoSerializer

class TokenVerify(APIView):
    def get(self, request):
        return Response({
            'username': request.user.username,
            'email': request.user.email,
            'name': request.user.get_full_name()
        })
    permission_classes =[IsAuthenticated]

class TodoList(generics.ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticated]

class TodoCreate(generics.CreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticated]

class TodoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticated]
