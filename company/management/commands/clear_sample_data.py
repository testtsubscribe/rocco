from django.core.management.base import BaseCommand
from company.models import CompanyInfo, Service, StoneType, ContactInquiry

class Command(BaseCommand):
    help = 'Clear all data from Company tables (CompanyInfo, Service, StoneType, ContactInquiry)'

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
        
        service_count = Service.objects.count()
        Service.objects.all().delete()
        self.stdout.write(self.style.SUCCESS(f'  ✓ Deleted {service_count} Services'))
        
        stone_type_count = StoneType.objects.count()
        StoneType.objects.all().delete()
        self.stdout.write(self.style.SUCCESS(f'  ✓ Deleted {stone_type_count} Stone Types'))
        
        company_info_count = CompanyInfo.objects.count()
        CompanyInfo.objects.all().delete()
        self.stdout.write(self.style.SUCCESS(f'  ✓ Deleted {company_info_count} Company Info records'))
        
        total_count = contact_inquiry_count + service_count + stone_type_count + company_info_count
        
        self.stdout.write(
            self.style.SUCCESS(f'\nSuccessfully cleared all Company data! Total records deleted: {total_count}')
        )
