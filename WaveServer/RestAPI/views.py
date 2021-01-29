from .serializers import WaveUserSerializer
from .models import WaveUser
from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


# Create your views here.
class WaveUserRetrieveViewSet(viewsets.ModelViewSet):

    queryset = WaveUser.objects.all().order_by('id')
    serializer_class = WaveUserSerializer

    def retrieve(self, request, pk=None):
        instance = get_object_or_404(self.get_queryset(), pk=pk)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


