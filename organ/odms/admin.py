from django.contrib import admin
from odms.models import Feedback, Contact, Donor


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phonenumber', 'feedback')


admin.site.register(Feedback, FeedbackAdmin)


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phonenumber', 'msg')


admin.site.register(Contact, ContactAdmin)


class DonorAdmin(admin.ModelAdmin):
    list_display = (
        'firstname', 'lastname', 'fathername', 'mothername', 'gender', 'organ', 'date_of_birth', 'bloodgroup',
        'aadharnumber', 'email', 'phonenumber', 'emergencynumber', 'add')


admin.site.register(Donor, DonorAdmin)
# Register your models here.
