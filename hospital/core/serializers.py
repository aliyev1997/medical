from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = ('id',)


class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        exclude = ('id',)


class ContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        exclude = ('id',)


class ServicesSerializer(serializers.ModelSerializer):
    subcategory = serializers.SlugRelatedField(slug_field="title", queryset=SubCategory.objects.all())

    class Meta:
        model = Services
        exclude = ('id',)


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        exclude = ('is_published', 'phone', 'id',)


class FeedbackManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedbackManager
        fields = '__all__'


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        exclude = ('birth_date', 'id',)


class ApointmentSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field="title", queryset=Category.objects.all())
    services = serializers.SlugRelatedField(slug_field='title', queryset=Services.objects.all())

    class Meta:
        model = Apointment
        exclude = ('confirmed', 'created_at', 'updated_at', 'doctor',)
