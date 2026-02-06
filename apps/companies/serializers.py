from rest_framework import serializers

from .models import Company
from ..users.models import User


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = [
            'id',
            'name',
            'website',
            'location',
            'created_at',
        ]
        read_only_fields = ('id','created_at')



