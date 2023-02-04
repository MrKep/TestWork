from rest_framework import serializers

from .models import Case

class CaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Case
        fields = ('id', 'uuid', 'created', 'body', 'active')
        read_only_fields = ('uuid',)