from modeltranslation.translator import register, TranslationOptions
from .models import CompanyInfo, Service, StoneType


@register(CompanyInfo)
class CompanyInfoTranslationOptions(TranslationOptions):
    fields = ('name', 'tagline', 'description', 'address')


@register(Service)
class ServiceTranslationOptions(TranslationOptions):
    fields = ('name', 'description')


@register(StoneType)
class StoneTypeTranslationOptions(TranslationOptions):
    fields = ('name', 'description')
