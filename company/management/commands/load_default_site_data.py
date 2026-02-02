from django.core.management.base import BaseCommand
from company.models import NavigationItem, BusinessHours, SiteSettings


class Command(BaseCommand):
    help = 'Load default data for NavigationItem, BusinessHours, and SiteSettings with Azerbaijani as primary language'

    def handle(self, *args, **options):
        self.stdout.write('Loading default site data with Azerbaijani language...')
        
        # Create NavigationItem entries (Azerbaijani)
        nav_items = [
            {'title_az': 'Ana Səhifə', 'title_en': 'Home', 'title_ru': 'Главная', 'url_name': 'home', 'display_order': 1},
            {'title_az': 'Haqqımızda', 'title_en': 'About', 'title_ru': 'О нас', 'url_name': 'about', 'display_order': 2},
            {'title_az': 'Xidmətlər', 'title_en': 'Services', 'title_ru': 'Услуги', 'url_name': 'services', 'display_order': 3},
            {'title_az': 'Daş Növləri', 'title_en': 'Stone Types', 'title_ru': 'Виды камней', 'url_name': 'stone_types', 'display_order': 4},
            {'title_az': 'Əlaqə', 'title_en': 'Contact', 'title_ru': 'Контакт', 'url_name': 'contact', 'display_order': 5},
        ]
        
        NavigationItem.objects.all().delete()
        for item_data in nav_items:
            NavigationItem.objects.create(**item_data)
            self.stdout.write(self.style.SUCCESS(f'✓ Created navigation item: {item_data["title_az"]}'))
        
        # Create BusinessHours entries (Azerbaijani)
        business_hours = [
            {
                'day_label_az': 'Bazar ertəsi - Cümə',
                'day_label_en': 'Monday - Friday',
                'day_label_ru': 'Понедельник - Пятница',
                'time_range_az': '08:00 - 18:00',
                'time_range_en': '8:00 AM - 6:00 PM',
                'time_range_ru': '08:00 - 18:00',
                'is_closed': False,
                'display_order': 1
            },
            {
                'day_label_az': 'Şənbə',
                'day_label_en': 'Saturday',
                'day_label_ru': 'Суббота',
                'time_range_az': '09:00 - 14:00',
                'time_range_en': '9:00 AM - 2:00 PM',
                'time_range_ru': '09:00 - 14:00',
                'is_closed': False,
                'display_order': 2
            },
            {
                'day_label_az': 'Bazar',
                'day_label_en': 'Sunday',
                'day_label_ru': 'Воскресенье',
                'time_range_az': 'Bağlıdır',
                'time_range_en': 'Closed',
                'time_range_ru': 'Закрыто',
                'is_closed': True,
                'display_order': 3
            },
        ]
        
        BusinessHours.objects.all().delete()
        for hours_data in business_hours:
            BusinessHours.objects.create(**hours_data)
            self.stdout.write(self.style.SUCCESS(f'✓ Created business hours: {hours_data["day_label_az"]}'))
        
        # Create SiteSettings entry (Azerbaijani - singleton)
        SiteSettings.objects.all().delete()
        site_settings = SiteSettings.objects.create(
            site_title_az='Precision Gems Ltd.',
            site_title_en='Precision Gems Ltd.',
            site_title_ru='Precision Gems Ltd.',
            default_phone='+994501234567',
            enable_contact_form=True,
            footer_text_az='Bütün hüquqlar qorunur.',
            footer_text_en='All rights reserved.',
            footer_text_ru='Все права защищены.',
            is_active=True
        )
        self.stdout.write(self.style.SUCCESS(f'✓ Created site settings: {site_settings.site_title_az}'))
        
        self.stdout.write(self.style.SUCCESS('\n✅ Successfully loaded all default site data in Azerbaijani!'))
