from modeltranslation.translator import register, TranslationOptions
from .models import CompanyInfo, Service, StoneType, AboutPageContent


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
        'quality_title', 'quality_description',
        'delivery_title', 'delivery_description',
        'team_title', 'team_description',
        'equipment_title', 'equipment_description',
        'guarantee_title', 'guarantee_description',
        'customer_title', 'customer_description'
    )
