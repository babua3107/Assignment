from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Task
from .serializers import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    def update(self, request, *args, **kwargs):
        kwargs['partial'] = True  # Allow partial updates
        return super().update(request, *args, **kwargs)