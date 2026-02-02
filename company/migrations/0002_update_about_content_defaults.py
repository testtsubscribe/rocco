# Generated migration for updating AboutPageContent with proper defaults

from django.db import migrations

def update_about_content_defaults(apps, schema_editor):
    """
    Update existing AboutPageContent objects with proper English defaults
    """
    AboutPageContent = apps.get_model('company', 'AboutPageContent')
    
    # Get all existing AboutPageContent objects
    for content in AboutPageContent.objects.all():
        # Update description fields if they are empty
        if not content.quality_description:
            content.quality_description = 'Precision in every cut, perfection in every polish'
        if not content.delivery_description:
            content.delivery_description = 'On-time project completion guaranteed'
        if not content.team_description:
            content.team_description = 'Professional specialists with decades of experience'
        if not content.equipment_description:
            content.equipment_description = 'State-of-the-art technology for superior results'
        if not content.guarantee_description:
            content.guarantee_description = 'We stand behind our work with confidence'
        if not content.customer_description:
            content.customer_description = 'Your satisfaction is our top priority'
        
        content.save()

def reverse_update_about_content_defaults(apps, schema_editor):
    """
    Reverse function (optional)
    """
    pass

class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(update_about_content_defaults, reverse_update_about_content_defaults),
    ]
