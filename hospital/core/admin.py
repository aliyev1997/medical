from django.contrib import admin

from .models import *


# Register your models here.

class ApointmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'doctor', 'services', 'confirmed',)
    list_display_links = ('doctor', 'id')
    list_editable = ('confirmed',)
    list_filter = ('confirmed', 'doctor', 'meet_date')


class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname',)
    list_display_links = ('name', 'surname')
    list_filter = ('level',)


class ContactsAdmin(admin.ModelAdmin):
    list_display = ('title', 'phone', 'email')
    list_display_links = ('title', 'phone')


class ServicesAdmin(admin.ModelAdmin):
    list_display = ('title', 'subcategory', 'price', 'code',)
    list_display_links = ('title', 'subcategory', 'price')
    list_filter = ('subcategory',)


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'phone', 'is_published')
    list_display_links = ('name', 'surname', 'phone')
    list_editable = ('is_published',)
    list_filter = ('is_published',)


class FeedbackManagerAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'phone', 'email')
    list_display_links = ('name', 'surname', 'phone')


admin.site.register(Apointment, ApointmentAdmin)
admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Contacts, ContactsAdmin)
admin.site.register(Services, ServicesAdmin)
admin.site.register(Feedback, FeedbackAdmin)
admin.site.register(FeedbackManager, FeedbackManagerAdmin)
