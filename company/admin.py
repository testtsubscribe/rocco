from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import CompanyInfo, Service, StoneType, ContactInquiry, AboutPageContent, NavigationItem, BusinessHours, SiteSettings, HomePageContent, ServicesPageContent, StoneTypesPageContent, ContactPageContent


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
            'fields': (
                'mission_title', 'mission_description', 'mission_icon',
                'vision_title', 'vision_description', 'vision_icon'
            )
        }),
        ('Why Choose Us', {
            'fields': (
                'why_choose_us_title',
                'quality_title', 'quality_description', 'quality_icon',
                'delivery_title', 'delivery_description', 'delivery_icon',
                'team_title', 'team_description', 'team_icon',
                'equipment_title', 'equipment_description', 'equipment_icon',
                'guarantee_title', 'guarantee_description', 'guarantee_icon',
                'customer_title', 'customer_description', 'customer_icon'
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

@admin.register(NavigationItem)
class NavigationItemAdmin(TranslationAdmin):
    list_display = ['title', 'url_name', 'display_order', 'is_active']
    list_editable = ['display_order', 'is_active']
    list_filter = ['is_active']
    search_fields = ['title', 'title_az', 'title_en', 'title_ru', 'url_name']
    fieldsets = (
        ('Navigation Item', {
            'fields': ('title', 'url_name', 'icon')
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


@admin.register(BusinessHours)
class BusinessHoursAdmin(TranslationAdmin):
    list_display = ['day_label', 'time_range', 'is_closed', 'display_order', 'is_active']
    list_editable = ['display_order', 'is_active']
    list_filter = ['is_closed', 'is_active']
    search_fields = ['day_label', 'day_label_az', 'day_label_en', 'day_label_ru']
    fieldsets = (
        ('Business Hours', {
            'fields': ('day_label', 'time_range', 'is_closed')
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


@admin.register(SiteSettings)
class SiteSettingsAdmin(TranslationAdmin):
    list_display = ['site_title', 'default_phone', 'enable_contact_form', 'is_active']
    list_editable = ['is_active']
    fieldsets = (
        ('Site Information', {
            'fields': ('site_title', 'default_phone', 'footer_text', 'copyright_text')
        }),
        ('Settings', {
            'fields': ('enable_contact_form', 'is_active')
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
    
    def has_add_permission(self, request):
        # Only allow one instance
        return not SiteSettings.objects.exists()


@admin.register(HomePageContent)
class HomePageContentAdmin(TranslationAdmin):
    list_display = ['__str__', 'is_active']
    list_editable = ['is_active']
    fieldsets = (
        ('Services Section', {
            'fields': ('services_title', 'services_subtitle')
        }),
        ('Stone Types Section', {
            'fields': ('stone_types_title', 'stone_types_subtitle')
        }),
        ('CTA Section', {
            'fields': ('cta_title', 'cta_subtitle')
        }),
        ('Button Texts', {
            'fields': (
                'get_quote_button', 'our_services_button', 'view_all_services_button',
                'view_all_stones_button', 'start_project_button', 'call_now_button'
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


@admin.register(ServicesPageContent)
class ServicesPageContentAdmin(TranslationAdmin):
    list_display = ['__str__', 'is_active']
    list_editable = ['is_active']
    fieldsets = (
        ('Page Content', {
            'fields': ('page_title', 'page_subtitle')
        }),
        ('CTA Section', {
            'fields': ('cta_title', 'cta_subtitle', 'consultation_button')
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


@admin.register(StoneTypesPageContent)
class StoneTypesPageContentAdmin(TranslationAdmin):
    list_display = ['__str__', 'is_active']
    list_editable = ['is_active']
    fieldsets = (
        ('Page Content', {
            'fields': ('page_title', 'page_subtitle')
        }),
        ('CTA Section', {
            'fields': ('cta_title', 'cta_subtitle', 'expert_advice_button')
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


@admin.register(ContactPageContent)
class ContactPageContentAdmin(TranslationAdmin):
    list_display = ['__str__', 'is_active']
    list_editable = ['is_active']
    fieldsets = (
        ('Page Content', {
            'fields': ('page_title', 'page_subtitle')
        }),
        ('Form Content', {
            'fields': ('form_title', 'contact_info_title', 'send_message_button')
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
