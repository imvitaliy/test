from django.shortcuts import render
from .serializer import SentenceSerializer
from .models import Sentence

from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status

# Create your views here.

class SentenceViewSet(viewsets.GenericViewSet):

    queryset = Sentence.objects.all()
    lookup_field = 'id'
    serializer_class = SentenceSerializer

    def get_object(pk):
        sentence = Sentence.objects.get(id=pk)
        return sentence
    
    def list(self, request):
        data = SentenceSerializer(data=self.queryset)
        data.is_valid()
        return Response(data.data, status=status.HTTP_200_OK)

    