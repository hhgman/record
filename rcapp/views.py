#-*- coding:utf-8 -*-



from rest_framework import generics,mixins
from rest_framework import status
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView
from rcapp.models import Recordings
from . import serializers
from .serializers import UserSerializer, RecordingSerializer
from rcapp.permissions import IsOwner
from rcapp.algorithm import algo
from django.contrib.auth.models import User
from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import os
import codecs


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    name = 'user-list'
    permission_classes = (
            permissions.IsAdminUser,)

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    name = 'user-detail'
    permission_classes = (
            permissions.IsAdminUser,)

class RecordingList(generics.GenericAPIView, mixins.ListModelMixin):
    queryset = Recordings.objects.all()
    parser_classes = (MultiPartParser, FormParser,)
    name = 'recording-list'
    serializer_class = RecordingSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        file_serializer = RecordingSerializer(data=request.data, context={'request': request})

        if file_serializer.is_valid():
            obj = file_serializer.save()
            obj.result = algo.evaluate(obj.datafile)
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RecordingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Recordings.objects.all()
    serializer_class = serializers.RecordingSerializer
    name = 'recordings-detail'

class ApiRoot(generics.GenericAPIView):
    name = 'api-root'
    def get(self, request, *args, **kwargs):
        return Response({
            'users': reverse(UserList.name, request=request),
            'recording': reverse(RecordingList.name, request=request),
            })

class Text(generics.GenericAPIView):
    name = 'text'
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    

    txtfile = codecs.open(os.path.join(BASE_DIR, 'static', 'text.txt'), "r", encoding="utf-16")
    mytxt = txtfile.read()
    txtfile.close()

    def get(self, request, *args, **kwargs):
        return Response({
            'text': self.mytxt,
        }, status=status.HTTP_200_OK)



class UserCreate(generics.CreateAPIView):
    """
    Creates the user.
    """
    serializer_class = UserSerializer
    def post(self, request, format='json'):
        serializer = UserSerializer(data=request.data,context={'request': request})
        if serializer.is_valid():
            user = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serialized._errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_user(request):
    serialized = UserSerializer(data=request.data,context={'request': request})
    if serialized.is_valid():
        serialized.save()
        return Response(serialized.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serialized._errors, status=status.HTTP_400_BAD_REQUEST)
