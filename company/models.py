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
    mission_icon = models.CharField(_('Mission Icon'), max_length=50, default='fas fa-bullseye', help_text=_('Font Awesome icon class'))
    
    vision_title = models.CharField(_('Vision Title'), max_length=100, default='Our Vision')
    vision_description = models.TextField(_('Vision Description'))
    vision_icon = models.CharField(_('Vision Icon'), max_length=50, default='fas fa-eye', help_text=_('Font Awesome icon class'))
    
    # Why Choose Us section
    why_choose_us_title = models.CharField(_('Why Choose Us Title'), max_length=200, default='')
    
    quality_title = models.CharField(_('Quality Title'), max_length=100, default='Quality Craftsmanship')
    quality_description = models.CharField(_('Quality Description'), max_length=200, default='Precision in every cut, perfection in every polish')
    quality_icon = models.CharField(_('Quality Icon'), max_length=50, default='fas fa-award', help_text=_('Font Awesome icon class'))
    
    delivery_title = models.CharField(_('Delivery Title'), max_length=100, default='Timely Delivery')
    delivery_description = models.CharField(_('Delivery Description'), max_length=200, default='On-time project completion guaranteed')
    delivery_icon = models.CharField(_('Delivery Icon'), max_length=50, default='fas fa-clock', help_text=_('Font Awesome icon class'))
    
    team_title = models.CharField(_('Team Title'), max_length=100, default='Expert Team')
    team_description = models.CharField(_('Team Description'), max_length=200, default='Professional specialists with decades of experience')
    team_icon = models.CharField(_('Team Icon'), max_length=50, default='fas fa-users', help_text=_('Font Awesome icon class'))
    
    equipment_title = models.CharField(_('Equipment Title'), max_length=100, default='Modern Equipment')
    equipment_description = models.CharField(_('Equipment Description'), max_length=200, default='State-of-the-art technology for superior results')
    equipment_icon = models.CharField(_('Equipment Icon'), max_length=50, default='fas fa-cogs', help_text=_('Font Awesome icon class'))
    
    guarantee_title = models.CharField(_('Guarantee Title'), max_length=100, default='Quality Guarantee')
    guarantee_description = models.CharField(_('Guarantee Description'), max_length=200, default='We stand behind our work with confidence')
    guarantee_icon = models.CharField(_('Guarantee Icon'), max_length=50, default='fas fa-shield-alt', help_text=_('Font Awesome icon class'))
    
    customer_title = models.CharField(_('Customer Title'), max_length=100, default='Customer Focus')
    customer_description = models.CharField(_('Customer Description'), max_length=200, default='Your satisfaction is our top priority')
    customer_icon = models.CharField(_('Customer Icon'), max_length=50, default='fas fa-handshake', help_text=_('Font Awesome icon class'))
    
    is_active = models.BooleanField(_('Is Active'), default=True)
    
    class Meta:
        verbose_name = _('About Page Content')
        verbose_name_plural = _('About Page Content')
    
    def __str__(self):
        return "About Page Content"

class NavigationItem(models.Model):
    title = models.CharField(_('Title'), max_length=100)
    url_name = models.CharField(_('URL Name'), max_length=100, help_text=_('Django URL name (e.g., "home", "about")'))
    icon = models.CharField(_('Icon'), max_length=50, blank=True, help_text=_('Font Awesome icon class (optional)'))
    display_order = models.IntegerField(_('Display Order'), default=0)
    is_active = models.BooleanField(_('Is Active'), default=True)
    
    class Meta:
        ordering = ['display_order', 'title']
        verbose_name = _('Navigation Item')
        verbose_name_plural = _('Navigation Items')
    
    def __str__(self):
        return self.title

class BusinessHours(models.Model):
    DAY_CHOICES = [
        (1, _('Monday')),
        (2, _('Tuesday')),
        (3, _('Wednesday')),
        (4, _('Thursday')),
        (5, _('Friday')),
        (6, _('Saturday')),
        (7, _('Sunday')),
    ]
    
    day_label = models.CharField(_('Day Label'), max_length=100, help_text=_('e.g., "Monday - Friday" or "Saturday"'))
    time_range = models.CharField(_('Time Range'), max_length=100, help_text=_('e.g., "8:00 AM - 6:00 PM" or "Closed"'))
    is_closed = models.BooleanField(_('Is Closed'), default=False)
    display_order = models.IntegerField(_('Display Order'), default=0)
    is_active = models.BooleanField(_('Is Active'), default=True)
    
    class Meta:
        ordering = ['display_order']
        verbose_name = _('Business Hours')
        verbose_name_plural = _('Business Hours')
    
    def __str__(self):
        return f"{self.day_label}: {self.time_range}"

class SiteSettings(models.Model):
    site_title = models.CharField(_('Site Title'), max_length=200, default='Precision Gems Ltd.')
    default_phone = models.CharField(_('Default Phone'), max_length=20, default='+994501234567')
    enable_contact_form = models.BooleanField(_('Enable Contact Form'), default=True)
    footer_text = models.CharField(_('Footer Text'), max_length=300, blank=True)
    copyright_text = models.CharField(_('Copyright Text'), max_length=300, default='© 2024 Precision Gems Ltd. All rights reserved.')
    is_active = models.BooleanField(_('Is Active'), default=True)
    
    class Meta:
        verbose_name = _('Site Settings')
        verbose_name_plural = _('Site Settings')
    
    def __str__(self):
        return "Site Settings"
    
    def save(self, *args, **kwargs):
        # Ensure only one instance exists (singleton pattern)
        if not self.pk and SiteSettings.objects.exists():
            raise ValueError(_('Only one SiteSettings instance is allowed'))
        return super().save(*args, **kwargs)

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

class HomePageContent(models.Model):
    # Services Section
    services_title = models.CharField(_('Services Title'), max_length=200, default='Our Services')
    services_subtitle = models.CharField(_('Services Subtitle'), max_length=300, default='Comprehensive stone processing solutions tailored to your needs')
    
    # Stone Types Section
    stone_types_title = models.CharField(_('Stone Types Title'), max_length=200, default='Stone Types We Work With')
    stone_types_subtitle = models.CharField(_('Stone Types Subtitle'), max_length=300, default='Expert processing for various stone materials')
    
    # CTA Section
    cta_title = models.CharField(_('CTA Title'), max_length=200, default='Ready to Transform Your Stone Materials?')
    cta_subtitle = models.CharField(_('CTA Subtitle'), max_length=300, default='Contact us today for a free consultation and quote!')
    
    # Button Texts
    get_quote_button = models.CharField(_('Get Quote Button'), max_length=50, default='Get Free Quote')
    our_services_button = models.CharField(_('Our Services Button'), max_length=50, default='Our Services')
    view_all_services_button = models.CharField(_('View All Services Button'), max_length=50, default='View All Services')
    view_all_stones_button = models.CharField(_('View All Stones Button'), max_length=50, default='View All Stone Types')
    start_project_button = models.CharField(_('Start Project Button'), max_length=50, default='Start Your Project')
    call_now_button = models.CharField(_('Call Now Button'), max_length=50, default='Call Now')
    
    is_active = models.BooleanField(_('Is Active'), default=True)
    
    class Meta:
        verbose_name = _('Home Page Content')
        verbose_name_plural = _('Home Page Content')
    
    def __str__(self):
        return "Home Page Content"

class ServicesPageContent(models.Model):
    page_title = models.CharField(_('Page Title'), max_length=200, default='Our Services')
    page_subtitle = models.CharField(_('Page Subtitle'), max_length=300, default='Comprehensive stone processing solutions for all your needs')
    cta_title = models.CharField(_('CTA Title'), max_length=200, default='Ready to Get Started?')
    cta_subtitle = models.CharField(_('CTA Subtitle'), max_length=300, default='Contact us today to discuss your project requirements')
    consultation_button = models.CharField(_('Consultation Button'), max_length=50, default='Get Free Consultation')
    
    is_active = models.BooleanField(_('Is Active'), default=True)
    
    class Meta:
        verbose_name = _('Services Page Content')
        verbose_name_plural = _('Services Page Content')
    
    def __str__(self):
        return "Services Page Content"

class StoneTypesPageContent(models.Model):
    page_title = models.CharField(_('Page Title'), max_length=200, default='Stone Types We Work With')
    page_subtitle = models.CharField(_('Page Subtitle'), max_length=300, default='Expert processing for various natural stone materials')
    cta_title = models.CharField(_('CTA Title'), max_length=200, default='Not Sure Which Stone is Right for You?')
    cta_subtitle = models.CharField(_('CTA Subtitle'), max_length=300, default='Our experts can help you choose the perfect stone for your project')
    expert_advice_button = models.CharField(_('Expert Advice Button'), max_length=50, default='Get Expert Advice')
    
    is_active = models.BooleanField(_('Is Active'), default=True)
    
    class Meta:
        verbose_name = _('Stone Types Page Content')
        verbose_name_plural = _('Stone Types Page Content')
    
    def __str__(self):
        return "Stone Types Page Content"

class ContactPageContent(models.Model):
    page_title = models.CharField(_('Page Title'), max_length=200, default='Contact Us')
    page_subtitle = models.CharField(_('Page Subtitle'), max_length=300, default='Get in touch with our expert team')
    form_title = models.CharField(_('Form Title'), max_length=200, default='Send us a Message')
    contact_info_title = models.CharField(_('Contact Info Title'), max_length=200, default='Contact Information')
    send_message_button = models.CharField(_('Send Message Button'), max_length=50, default='Send Message')
    
    is_active = models.BooleanField(_('Is Active'), default=True)
    
    class Meta:
        verbose_name = _('Contact Page Content')
        verbose_name_plural = _('Contact Page Content')
    
    def __str__(self):
        return "Contact Page Content"
