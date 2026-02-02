from modeltranslation.translator import register, TranslationOptions
from .models import CompanyInfo, Service, StoneType, AboutPageContent, NavigationItem, BusinessHours, SiteSettings, HomePageContent, ServicesPageContent, StoneTypesPageContent, ContactPageContent


@register(CompanyInfo)
class CompanyInfoTranslationOptions(TranslationOptions):
    fields = ('name', 'tagline', 'description', 'address')


@register(Service)
class ServiceTranslationOptions(TranslationOptions):
    fields = ('name', 'description')


@register(StoneType)
class StoneTypeTranslationOptions(TranslationOptions):
    fields = ('name', 'description')


@register(AboutPageContent)
class AboutPageContentTranslationOptions(TranslationOptions):
    fields = (
        'mission_title', 'mission_description',
        'vision_title', 'vision_description',
        'why_choose_us_title',
        'quality_title', 'quality_description',
        'delivery_title', 'delivery_description',
        'team_title', 'team_description',
        'equipment_title', 'equipment_description',
        'guarantee_title', 'guarantee_description',
        'customer_title', 'customer_description'
    )


@register(NavigationItem)
class NavigationItemTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(BusinessHours)
class BusinessHoursTranslationOptions(TranslationOptions):
    fields = ('day_label', 'time_range')


@register(SiteSettings)
class SiteSettingsTranslationOptions(TranslationOptions):
    fields = ('site_title', 'footer_text', 'copyright_text')


@register(HomePageContent)
class HomePageContentTranslationOptions(TranslationOptions):
    fields = (
        'services_title', 'services_subtitle',
        'stone_types_title', 'stone_types_subtitle',
        'cta_title', 'cta_subtitle',
        'get_quote_button', 'our_services_button', 'view_all_services_button',
        'view_all_stones_button', 'start_project_button', 'call_now_button'
    )


@register(ServicesPageContent)
class ServicesPageContentTranslationOptions(TranslationOptions):
    fields = ('page_title', 'page_subtitle', 'cta_title', 'cta_subtitle', 'consultation_button')


@register(StoneTypesPageContent)
class StoneTypesPageContentTranslationOptions(TranslationOptions):
    fields = ('page_title', 'page_subtitle', 'cta_title', 'cta_subtitle', 'expert_advice_button')


@register(ContactPageContent)
class ContactPageContentTranslationOptions(TranslationOptions):
    fields = ('page_title', 'page_subtitle', 'form_title', 'contact_info_title', 'send_message_button')
