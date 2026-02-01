from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import CompanyInfo, Service, StoneType, ContactInquiry, AboutPageContent


@admin.register(CompanyInfo)
class CompanyInfoAdmin(TranslationAdmin):
    list_display = ['name', 'email', 'phone', 'is_active']
    list_editable = ['is_active']
    fieldsets = (
        ('General Information', {
            'fields': ('name', 'tagline', 'description', 'address')
        }),
        ('Contact Information', {
            'fields': ('phone', 'email', 'website')
        }),
        ('Status', {
            'fields': ('is_active',)
        }),
    )
    
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@admin.register(Service)
class ServiceAdmin(TranslationAdmin):
    list_display = ['name', 'icon', 'display_order', 'is_active']
    list_editable = ['display_order', 'is_active']
    list_filter = ['is_active']
    search_fields = ['name', 'name_en', 'name_az', 'name_ru']
    fieldsets = (
        ('Service Information', {
            'fields': ('name', 'description', 'icon')
        }),
        ('Display Settings', {
            'fields': ('display_order', 'is_active')
        }),
    )
    
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@admin.register(StoneType)
class StoneTypeAdmin(TranslationAdmin):
    list_display = ['name', 'display_order', 'is_active']
    list_editable = ['display_order', 'is_active']
    list_filter = ['is_active']
    search_fields = ['name', 'name_en', 'name_az', 'name_ru']
    fieldsets = (
        ('Stone Type Information', {
            'fields': ('name', 'description')
        }),
        ('Display Settings', {
            'fields': ('display_order', 'is_active')
        }),
    )
    
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

@admin.register(AboutPageContent)
class AboutPageContentAdmin(TranslationAdmin):
    list_display = ['__str__', 'is_active']
    list_editable = ['is_active']
    fieldsets = (
        ('Mission & Vision', {
            'fields': ('mission_title', 'mission_description', 'vision_title', 'vision_description')
        }),
        ('Why Choose Us', {
            'fields': (
                'quality_title', 'quality_description',
                'delivery_title', 'delivery_description',
                'team_title', 'team_description',
                'equipment_title', 'equipment_description',
                'guarantee_title', 'guarantee_description',
                'customer_title', 'customer_description'
            )
        }),
        ('Status', {
            'fields': ('is_active',)
        }),
    )
    
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

@admin.register(ContactInquiry)
class ContactInquiryAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'service', 'submitted_at', 'is_resolved']
    list_filter = ['submitted_at', 'is_resolved', 'service']
    search_fields = ['name', 'email', 'message']
    readonly_fields = ['submitted_at']
    list_editable = ['is_resolved']
