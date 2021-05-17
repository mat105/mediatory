from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from library.models import Tale


class TaleSerializer(ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Tale
        fields = '__all__'
