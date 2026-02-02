from django.core.management.base import BaseCommand
from company.models import CompanyInfo, Service, StoneType, AboutPageContent, ContactInquiry, NavigationItem, BusinessHours, SiteSettings, HomePageContent, ServicesPageContent, StoneTypesPageContent, ContactPageContent

class Command(BaseCommand):
    help = 'Clear all data from Company tables (CompanyInfo, Service, StoneType, AboutPageContent, ContactInquiry, NavigationItem, BusinessHours, SiteSettings, HomePageContent, ServicesPageContent, StoneTypesPageContent, ContactPageContent)'

    def add_arguments(self, parser):
        parser.add_argument(
            '--yes',
            action='store_true',
            help='Skip confirmation prompt',
        )

    def handle(self, *args, **options):
        if not options['yes']:
            confirm = input('Are you sure you want to delete all data from Company tables? This cannot be undone. Type "yes" to continue: ')
            if confirm.lower() != 'yes':
                self.stdout.write(self.style.WARNING('Operation cancelled.'))
                return

        self.stdout.write('Clearing all Company data...')
        
        # Delete all records from each model
        contact_inquiry_count = ContactInquiry.objects.count()
        ContactInquiry.objects.all().delete()
        self.stdout.write(self.style.SUCCESS(f'  ✓ Deleted {contact_inquiry_count} Contact Inquiries'))
        
        contact_page_content_count = ContactPageContent.objects.count()
        ContactPageContent.objects.all().delete()
        self.stdout.write(self.style.SUCCESS(f'  ✓ Deleted {contact_page_content_count} Contact Page Content records'))
        
        stone_types_page_content_count = StoneTypesPageContent.objects.count()
        StoneTypesPageContent.objects.all().delete()
        self.stdout.write(self.style.SUCCESS(f'  ✓ Deleted {stone_types_page_content_count} Stone Types Page Content records'))
        
        services_page_content_count = ServicesPageContent.objects.count()
        ServicesPageContent.objects.all().delete()
        self.stdout.write(self.style.SUCCESS(f'  ✓ Deleted {services_page_content_count} Services Page Content records'))
        
        home_page_content_count = HomePageContent.objects.count()
        HomePageContent.objects.all().delete()
        self.stdout.write(self.style.SUCCESS(f'  ✓ Deleted {home_page_content_count} Home Page Content records'))
        
        business_hours_count = BusinessHours.objects.count()
        BusinessHours.objects.all().delete()
        self.stdout.write(self.style.SUCCESS(f'  ✓ Deleted {business_hours_count} Business Hours'))
        
        navigation_item_count = NavigationItem.objects.count()
        NavigationItem.objects.all().delete()
        self.stdout.write(self.style.SUCCESS(f'  ✓ Deleted {navigation_item_count} Navigation Items'))
        
        site_settings_count = SiteSettings.objects.count()
        SiteSettings.objects.all().delete()
        self.stdout.write(self.style.SUCCESS(f'  ✓ Deleted {site_settings_count} Site Settings'))
        
        service_count = Service.objects.count()
        Service.objects.all().delete()
        self.stdout.write(self.style.SUCCESS(f'  ✓ Deleted {service_count} Services'))
        
        stone_type_count = StoneType.objects.count()
        StoneType.objects.all().delete()
        self.stdout.write(self.style.SUCCESS(f'  ✓ Deleted {stone_type_count} Stone Types'))
        
        company_info_count = CompanyInfo.objects.count()
        CompanyInfo.objects.all().delete()
        self.stdout.write(self.style.SUCCESS(f'  ✓ Deleted {company_info_count} Company Info records'))
        
        about_content_count = AboutPageContent.objects.count()
        AboutPageContent.objects.all().delete()
        self.stdout.write(self.style.SUCCESS(f'  ✓ Deleted {about_content_count} About Page Content records'))
        
        total_count = (contact_inquiry_count + contact_page_content_count + stone_types_page_content_count + 
                       services_page_content_count + home_page_content_count + business_hours_count + 
                       navigation_item_count + site_settings_count + service_count + stone_type_count + 
                       company_info_count + about_content_count)
        
        self.stdout.write(
            self.style.SUCCESS(f'\nSuccessfully cleared all Company data! Total records deleted: {total_count}')
        )
