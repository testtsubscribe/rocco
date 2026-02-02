#!/usr/bin/env python
"""
Test script to verify language switching functionality
"""
import os
import sys

# Add the project directory to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rocco.settings')

# Setup Django
import django
django.setup()

from django.utils import translation
from company.models import AboutPageContent

def test_language_switching():
    print("Testing language switching for AboutPageContent...")
    
    # Get or create AboutPageContent
    content, created = AboutPageContent.objects.get_or_create(
        defaults={
            'mission_title': 'Missiyamız',
            'mission_description': 'Mükəmməl daş kəsimi və cilalama xidmətləri təmin etmək.',
            'vision_title': 'Viziyonumuz',
            'vision_description': 'Keyfiyyət və etibarlılıq üçün tanınan dünya səviyyəli daş emal xidməti provayderi olmaq.',
            'quality_title': 'Keyfiyyətli İşçilik',
            'quality_description': 'Hər kəsində dəqiqlik, hər cilalamada mükəmməllik',
            'delivery_title': 'Vaxtında Çatdırılma',
            'delivery_description': 'Vaxtında layihə tamamlanması təmin edilir',
            'team_title': 'Ekspert Komanda',
            'team_description': 'Onillik təcrübəsi olan peşəkar mütəxəssislər',
            'equipment_title': 'Müasir Avadanlıqlar',
            'equipment_description': 'Üstün nəticələr üçün ən müasir texnologiya',
            'guarantee_title': 'Keyfiyyət Zəmanəti',
            'guarantee_description': 'İşimizin arxasında etimadla dayanırıq',
            'customer_title': 'Müştəri Fokus',
            'customer_description': 'Məmnuniyyətiniz bizim əsas prioritetimizdir',
            'is_active': True,
        }
    )
    
    if created:
        print("Created new AboutPageContent with Azerbaijani defaults")
    
    # Set English translations
    content.mission_title_en = 'Our Mission'
    content.mission_description_en = 'Providing exceptional stone cutting and polishing services with superior craftsmanship and quality.'
    content.vision_title_en = 'Our Vision'
    content.vision_description_en = 'To be a world-leading stone processing service provider recognized for quality and reliability.'
    content.quality_title_en = 'Quality Craftsmanship'
    content.quality_description_en = 'Precision in every cut, perfection in every polish'
    content.delivery_title_en = 'Timely Delivery'
    content.delivery_description_en = 'On-time project completion guaranteed'
    content.team_title_en = 'Expert Team'
    content.team_description_en = 'Professional specialists with decades of experience'
    content.equipment_title_en = 'Modern Equipment'
    content.equipment_description_en = 'State-of-the-art technology for superior results'
    content.guarantee_title_en = 'Quality Guarantee'
    content.guarantee_description_en = 'We stand behind our work with confidence'
    content.customer_title_en = 'Customer Focus'
    content.customer_description_en = 'Your satisfaction is our top priority'
    
    content.save()
    
    print("\n=== Testing Language Switching ===")
    
    # Test Azerbaijani (default)
    with translation.override('az'):
        print("\n[AZ] Azerbaijani:")
        print(f"Mission Title: {content.mission_title}")
        print(f"Quality Title: {content.quality_title}")
        print(f"Delivery Title: {content.delivery_title}")
        print(f"Team Title: {content.team_title}")
        print(f"Equipment Title: {content.equipment_title}")
        print(f"Guarantee Title: {content.guarantee_title}")
        print(f"Customer Title: {content.customer_title}")
    
    # Test English
    with translation.override('en'):
        print("\n[EN] English:")
        print(f"Mission Title: {content.mission_title}")
        print(f"Quality Title: {content.quality_title}")
        print(f"Delivery Title: {content.delivery_title}")
        print(f"Team Title: {content.team_title}")
        print(f"Equipment Title: {content.equipment_title}")
        print(f"Guarantee Title: {content.guarantee_title}")
        print(f"Customer Title: {content.customer_title}")
    
    # Test Russian
    with translation.override('ru'):
        print("\n[RU] Russian:")
        print(f"Mission Title: {content.mission_title}")
        print(f"Quality Title: {content.quality_title}")
        print(f"Delivery Title: {content.delivery_title}")
        print(f"Team Title: {content.team_title}")
        print(f"Equipment Title: {content.equipment_title}")
        print(f"Guarantee Title: {content.guarantee_title}")
        print(f"Customer Title: {content.customer_title}")
    
    print("\n=== Test Complete ===")

if __name__ == '__main__':
    test_language_switching()
