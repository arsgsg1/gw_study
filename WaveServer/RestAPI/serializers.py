from rest_framework import serializers
from .models import WaveUser


class WaveUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = WaveUser
        fields = '__all__'
