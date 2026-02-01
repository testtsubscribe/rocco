from django.db import models
from django.utils.translation import gettext_lazy as _

class CompanyInfo(models.Model):
    name = models.CharField(_('Name'), max_length=200)
    tagline = models.CharField(_('Tagline'), max_length=300)
    description = models.TextField(_('Description'))
    address = models.TextField(_('Address'))
    phone = models.CharField(_('Phone'), max_length=20)
    email = models.EmailField(_('Email'))
    website = models.URLField(_('Website'), blank=True)
    is_active = models.BooleanField(_('Is Active'), default=True)
    
    class Meta:
        verbose_name = _('Company Information')
        verbose_name_plural = _('Company Information')
    
    def __str__(self):
        return self.name

class Service(models.Model):
    name = models.CharField(_('Name'), max_length=100)
    description = models.TextField(_('Description'))
    icon = models.CharField(_('Icon'), max_length=50, help_text=_('Font Awesome icon class'))
    display_order = models.IntegerField(_('Display Order'), default=0)
    is_active = models.BooleanField(_('Is Active'), default=True)
    
    class Meta:
        ordering = ['display_order', 'name']
        verbose_name = _('Service')
        verbose_name_plural = _('Services')
    
    def __str__(self):
        return self.name

class StoneType(models.Model):
    name = models.CharField(_('Name'), max_length=100)
    description = models.TextField(_('Description'))
    display_order = models.IntegerField(_('Display Order'), default=0)
    is_active = models.BooleanField(_('Is Active'), default=True)
    
    class Meta:
        ordering = ['display_order', 'name']
        verbose_name = _('Stone Type')
        verbose_name_plural = _('Stone Types')
    
    def __str__(self):
        return self.name

class AboutPageContent(models.Model):
    mission_title = models.CharField(_('Mission Title'), max_length=100, default='Our Mission')
    mission_description = models.TextField(_('Mission Description'))
    vision_title = models.CharField(_('Vision Title'), max_length=100, default='Our Vision')
    vision_description = models.TextField(_('Vision Description'))
    
    # Why Choose Us section
    quality_title = models.CharField(_('Quality Title'), max_length=100, default='Quality Craftsmanship')
    quality_description = models.CharField(_('Quality Description'), max_length=200)
    delivery_title = models.CharField(_('Delivery Title'), max_length=100, default='Timely Delivery')
    delivery_description = models.CharField(_('Delivery Description'), max_length=200)
    team_title = models.CharField(_('Team Title'), max_length=100, default='Expert Team')
    team_description = models.CharField(_('Team Description'), max_length=200)
    equipment_title = models.CharField(_('Equipment Title'), max_length=100, default='Modern Equipment')
    equipment_description = models.CharField(_('Equipment Description'), max_length=200)
    guarantee_title = models.CharField(_('Guarantee Title'), max_length=100, default='Quality Guarantee')
    guarantee_description = models.CharField(_('Guarantee Description'), max_length=200)
    customer_title = models.CharField(_('Customer Title'), max_length=100, default='Customer Focus')
    customer_description = models.CharField(_('Customer Description'), max_length=200)
    
    is_active = models.BooleanField(_('Is Active'), default=True)
    
    class Meta:
        verbose_name = _('About Page Content')
        verbose_name_plural = _('About Page Content')
    
    def __str__(self):
        return "About Page Content"

class ContactInquiry(models.Model):
    name = models.CharField(_('Name'), max_length=100)
    email = models.EmailField(_('Email'))
    phone = models.CharField(_('Phone'), max_length=40, blank=True, null=True)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, verbose_name=_('Service'))
    message = models.TextField(_('Message'))
    submitted_at = models.DateTimeField(_('Submitted At'), auto_now_add=True)
    is_resolved = models.BooleanField(_('Is Resolved'), default=False)
    
    class Meta:
        ordering = ['-submitted_at']
        verbose_name = _('Contact Inquiry')
        verbose_name_plural = _('Contact Inquiries')
    
    def __str__(self):
        return f"Inquiry from {self.name}"
