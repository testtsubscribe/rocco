from django.core.management.base import BaseCommand
from company.models import CompanyInfo, Service, StoneType

class Command(BaseCommand):
    help = 'Load sample data for Precision Gems Ltd.'

    def handle(self, *args, **options):
        self.stdout.write('Loading sample data for Precision Gems Ltd...')
        
        # Create or update company info
        company, created = CompanyInfo.objects.update_or_create(
            name="Precision Gems Ltd.",
            defaults={
                'name': "Precision Gems Ltd.",
                'tagline': 'Premium Daş Kəsimi və Cilalama Xidmətləri',
                'description': 'Sənayedə 15 ildən artıq təcrübəyə malik peşəkar daş kəsmə və cilalama xidmətləri. Biz bütün təbii daş növlərinin dəqiq kəsimi üzrə ixtisaslaşmışıq.',
                'address': '123 Gem Street, Stone City, SC 12345',
                'phone': '+1 (555) 123-4567',
                'email': 'info@precisiongems.com',
                'website': 'https://www.precisiongems.com',
                'is_active': True
            }
        )
        
        # Create services
        services_data = [
            {
                'name': 'Dəqiq Kəsim',
                'icon': 'fas fa-cut',
                'description': 'Mükəmməl kənarlar və ölçülər üçün qabaqcıl almaz uclu alətlərdən istifadə edərək yüksək dəqiqlikli daş kəsimi.',
                'display_order': 1,
                'is_active': True
            },
            {
                'name': 'Fərdi Formalaşdırma',
                'icon': 'fas fa-draw-polygon',
                'description': 'Unikal memarlıq və dizayn tələbləri üçün fərdi daş formalaşdırma xidmətləri.',
                'display_order': 2,
                'is_active': True
            },
            {
                'name': 'Cilalama',
                'icon': 'fas fa-sparkles',
                'description': 'Daşlarınızın təbii gözəlliyini və parıltısını üzə çıxarmaq üçün peşəkar cilalama xidmətləri.',
                'display_order': 3,
                'is_active': True
            },
            {
                'name': 'Kənar Profilləmə',
                'icon': 'fas fa-border-style',
                'description': 'Mətbəx səthləri, pilləkənlər və dekorativ elementlər üçün ixtisaslaşmış kənar profilləmə.',
                'display_order': 4,
                'is_active': True
            },
        ]
        
        for service_data in services_data:
            Service.objects.update_or_create(
                name=service_data['name'], # This is used for lookup
                defaults=service_data
            )
        
        # Create stone types
        stone_types_data = [
            {
                'name': 'Qranit',
                'description': 'Mətbəx səthləri və gediş-gəlişin çox olduğu yerlər üçün mükəmməl olan davamlı vulkanik daş. Sərtliyi və rəng müxtəlifliyi ilə tanınır.',
                'display_order': 1,
                'is_active': True
            },
            {
                'name': 'Mərmər',
                'description': 'Gözəl damarları olan zərif metamorfik daş. Dekorativ parçalar və lüks səthlər üçün idealdır.',
                'display_order': 2,
                'is_active': True
            },
            {
                'name': 'Kvarsit',
                'description': 'Qranitin davamlılığına və mərmərin gözəlliyinə malik təbii daş. İstiyə və cızıqlara qarşı davamlıdır.',
                'display_order': 3,
                'is_active': True
            },
            {
                'name': 'Oniks',
                'description': 'Möhtəşəm vizual dərinliyə malik yarı şəffaf daş. Arxa işıqlandırmalı xüsusiyyətlər və dekorativ elementlər üçün idealdır.',
                'display_order': 4,
                'is_active': True
            },
            {
                'name': 'Kvars',
                'description': 'Naxış və rəngdə sabitlik təklif edən mühəndis daşı. Məsaməsizdir və az qulluq tələb edir.',
                'display_order': 5,
                'is_active': True
            },
        ]
        
        for stone_data in stone_types_data:
            StoneType.objects.update_or_create(
                name=stone_data['name'],
                defaults=stone_data
            )
        
        self.stdout.write(
            self.style.SUCCESS('Successfully loaded sample data for Precision Gems Ltd!')
        )