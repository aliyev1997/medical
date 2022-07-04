from django.utils.timezone import now

from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Category(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.title


class SubCategory(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    category = models.ForeignKey(Category, related_name='SubCategory', null=True, on_delete=models.SET_NULL)
    feedback = models.TextField(max_length=2500, null=True, blank=True)

    def __str__(self):
        return self.title


class Services(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    subcategory = models.ForeignKey(SubCategory, related_name='Services', null=True, on_delete=models.SET_NULL)
    price = models.IntegerField(null=True, blank=True)
    code = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'
        ordering = ['title']


class Feedback(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    surname = models.CharField(max_length=255, null=True, blank=True)
    phone = models.IntegerField(null=True, blank=True)
    description = models.TextField(null=True)
    is_published = models.BooleanField(default=False, verbose_name="Показывать в странице")


class FeedbackManager(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    surname = models.CharField(max_length=255, null=True, blank=True)
    phone = models.IntegerField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    description = models.TextField(null=True)


class Doctor(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    surname = models.CharField(max_length=255, null=True, blank=True)
    biography = models.TextField(max_length=2500, null=True, blank=True)
    birth_date = models.DateTimeField(blank=True, null=True)
    level = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name + ' ' + self.surname

    class Meta:
        verbose_name = 'Doctor'
        verbose_name_plural = 'Doctors'


class Apointment(models.Model):
    name = models.CharField(max_length=255, null=True)
    surname = models.CharField(max_length=255, null=True)
    phone = models.IntegerField(default=0)
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    services = models.ForeignKey(Services, null=True, on_delete=models.SET_NULL)
    doctor = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    meet_date = models.DateTimeField(default=now)
    confirmed = models.BooleanField(blank=True, default=False)
    description = models.TextField(null=True)

    def __str__(self):
        return self.name + ' ' + self.surname + ' need ' + str(self.services) + ' at ' + str(self.meet_date)

    class Meta:
        verbose_name = 'Apointment'
        verbose_name_plural = 'Apointments'
        ordering = ['-created_at']


class Contacts(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    phone = models.IntegerField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    telegram = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'
