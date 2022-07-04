from django.http import request, HttpResponse
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.mixins import ListModelMixin
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import *
from .permissions import *
from .serializers import *


class HomeViewSet(ModelViewSet):
    serializer_class = CategorySerializer
    permission_classes = (UsageManager,)

    def list(self, request):
        queryset1 = Contacts.objects.all()
        contacts = ContactsSerializer(queryset1, many=True)
        queryset2 = Doctor.objects.all()
        doctors = DoctorSerializer(queryset2, many=True)
        queryset3 = Category.objects.all()
        categories = CategorySerializer(queryset3, many=True)
        result = {'Contacts': contacts.data, 'Doctors': doctors.data, 'Categories': categories.data}
        return Response(result)


class ApointmentViewSet(ModelViewSet):
    queryset = Apointment.objects.all()
    serializer_class = ApointmentSerializer
    permission_classes = (FeedbackM,)


class ApViewSet(viewsets.ModelViewSet):
    serializer_class = ApointmentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.method == 'GET':
            return Apointment.objects.filter(doctor=self.request.user)


class DoctorViewSet(ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = (UsageManager,)


class ServicesViewSet(ModelViewSet):
    queryset = Services.objects.all()
    serializer_class = ServicesSerializer
    permission_classes = (UsageManager,)


class FeedbackViewSet(ModelViewSet):
    queryset = Feedback.objects.filter(is_published=True)
    serializer_class = FeedbackSerializer


class FeedbackManagerViewSet(ModelViewSet):
    queryset = FeedbackManager.objects.all()
    serializer_class = FeedbackManagerSerializer
    permission_classes = (FeedbackM,)


class ContactsViewSet(ModelViewSet):
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer
    permission_classes = (UsageManager,)
