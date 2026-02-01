from django.contrib import admin
from .models import CompanyInfo, Service, StoneType, ContactInquiry

@admin.register(CompanyInfo)
class CompanyInfoAdmin(admin.ModelAdmin):
    list_display = ['name', 'get_email', 'get_phone', 'is_active']
    list_editable = ['is_active']
    
    def get_email(self, obj):
        return obj.email
    get_email.short_description = 'Email'
    
    def get_phone(self, obj):
        return obj.phone
    get_phone.short_description = 'Phone'

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'icon', 'display_order', 'is_active']
    list_editable = ['display_order', 'is_active']
    list_filter = ['is_active']
    search_fields = ['name']

@admin.register(StoneType)
class StoneTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'display_order', 'is_active']
    list_editable = ['display_order', 'is_active']
    list_filter = ['is_active']
    search_fields = ['name']

@admin.register(ContactInquiry)
class ContactInquiryAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'service', 'submitted_at', 'is_resolved']
    list_filter = ['submitted_at', 'is_resolved', 'service']
    search_fields = ['name', 'email', 'message']
    readonly_fields = ['submitted_at']
    list_editable = ['is_resolved']