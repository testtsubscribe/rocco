#!/usr/bin/env python
import os
import sys
import django

# Add the project directory to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rocco.settings')

# Setup Django
django.setup()

from company.models import AboutPageContent

def setup_about_content():
    # Get or create AboutPageContent
    about_content, created = AboutPageContent.objects.get_or_create(
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
        print('Created new AboutPageContent with Azerbaijani defaults')
    else:
        print('AboutPageContent already exists')
    
    # Set English translations
    about_content.mission_title_en = 'Our Mission'
    about_content.mission_description_en = 'Providing exceptional stone cutting and polishing services with superior craftsmanship and quality.'
    about_content.vision_title_en = 'Our Vision'
    about_content.vision_description_en = 'To be a world-leading stone processing service provider recognized for quality and reliability.'
    about_content.quality_title_en = 'Quality Craftsmanship'
    about_content.quality_description_en = 'Precision in every cut, perfection in every polish'
    about_content.delivery_title_en = 'Timely Delivery'
    about_content.delivery_description_en = 'On-time project completion guaranteed'
    about_content.team_title_en = 'Expert Team'
    about_content.team_description_en = 'Professional specialists with decades of experience'
    about_content.equipment_title_en = 'Modern Equipment'
    about_content.equipment_description_en = 'State-of-the-art technology for superior results'
    about_content.guarantee_title_en = 'Quality Guarantee'
    about_content.guarantee_description_en = 'We stand behind our work with confidence'
    about_content.customer_title_en = 'Customer Focus'
    about_content.customer_description_en = 'Your satisfaction is our top priority'
    
    # Set Russian translations
    about_content.mission_title_ru = 'Наша Миссия'
    about_content.mission_description_ru = 'Предоставление исключительных услуг по резке и полировке камня с превосходным мастерством и качеством.'
    about_content.vision_title_ru = 'Наше Видение'
    about_content.vision_description_ru = 'Стать ведущим в мире поставщиком услуг по обработке камня, признанным за качество и надежность.'
    about_content.quality_title_ru = 'Качественная Работа'
    about_content.quality_description_ru = 'Точность в каждом разрезе, совершенство в каждой полировке'
    about_content.delivery_title_ru = 'Своевременная Доставка'
    about_content.delivery_description_ru = 'Гарантированное своевременное завершение проекта'
    about_content.team_title_ru = 'Команда Экспертов'
    about_content.team_description_ru = 'Профессиональные специалисты с десятилетиями опыта'
    about_content.equipment_title_ru = 'Современное Оборудование'
    about_content.equipment_description_ru = 'Передовая технология для превосходных результатов'
    about_content.guarantee_title_ru = 'Гарантия Качества'
    about_content.guarantee_description_ru = 'Мы стоим за свою работу с уверенностью'
    about_content.customer_title_ru = 'Фокус на Клиенте'
    about_content.customer_description_ru = 'Ваше удовлетворение - наш главный приоритет'
    
    about_content.save()
    
    print('Successfully set up translations for AboutPageContent')
    
    # Display current values
    print('\nCurrent values:')
    print(f'AZ Mission: {about_content.mission_title}')
    print(f'EN Mission: {about_content.mission_title_en}')
    print(f'RU Mission: {about_content.mission_title_ru}')

if __name__ == '__main__':
    setup_about_content()
