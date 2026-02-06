from django.shortcuts import render
from rest_framework import viewsets, permissions, response
from rest_framework.permissions import IsAuthenticated

from .models import Job
from .serializers import JobSerializer

class JobViewSet(viewsets.ModelViewSet):
    serializer_class=JobSerializer
    permission_classes = [IsAuthenticated]
    filterset_fields = ['status', 'company']
    def get_queryset(self):
        return Job.objects.filter(user=self.request.user)

    def perform_create(self,serializer):
        return serializer.save(user=self.request.user)
