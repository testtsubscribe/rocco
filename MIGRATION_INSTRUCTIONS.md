# Multilanguage Support Migration Instructions

This guide will help you migrate your database to support multilanguage functionality for models.

## Overview of Changes

The following files have been modified to add multilanguage support:

1. **company/models.py** - Added translation labels to all model fields
2. **company/translation.py** - NEW FILE - Registers translatable fields (name, description, tagline, address)
3. **company/admin.py** - Updated to use TranslationAdmin for better multilanguage interface
4. **company/views.py** - Added translation support for user messages
5. **rocco/settings.py** - Added modeltranslation configuration

## Fields That Will Be Translated

### CompanyInfo Model
- name (Azerbaijani, English, Russian)
- tagline (Azerbaijani, English, Russian)
- description (Azerbaijani, English, Russian)
- address (Azerbaijani, English, Russian)

### Service Model
- name (Azerbaijani, English, Russian)
- description (Azerbaijani, English, Russian)

### StoneType Model
- name (Azerbaijani, English, Russian)
- description (Azerbaijani, English, Russian)

## Migration Steps

### Step 1: Install/Verify Dependencies

Make sure django-modeltranslation is installed:

```bash
pip install django-modeltranslation
```

Or reinstall all requirements:

```bash
pip install -r requirements.txt
```

### Step 2: Generate Migrations

Run the following command to create migrations for the new translatable fields:

```bash
python manage.py makemigrations
```

This will create migration files that add the language-specific fields (e.g., `name_az`, `name_en`, `name_ru`, etc.)

### Step 3: Apply Migrations

Apply the migrations to your database:

```bash
python manage.py migrate
```

### Step 4: Update Translation Fields (IMPORTANT)

After migrating, you need to copy existing data to the default language fields. Run:

```bash
python manage.py update_translation_fields
```

This command copies data from the base fields (e.g., `name`) to the language-specific fields (e.g., `name_az`).

### Step 5: Sync Translation Fields

To ensure consistency, run:

```bash
python manage.py sync_translation_fields --noinput
```

### Step 6: Compile Translation Messages (Optional)

If you want to translate the admin interface and form labels, compile the translation messages:

```bash
python manage.py compilemessages
```

## Post-Migration

### Admin Interface

After migration, when you access the admin panel:

1. Each translatable field will appear with tabs for each language (Azərbaycan, English, Русский)
2. You can fill in translations for each language separately
3. The default language (Azerbaijani) will be used as fallback if a translation is missing

### Frontend Display

The website will automatically display content in the user's selected language:
- The language switcher should be available in templates
- Content will fall back to Azerbaijani if translation is missing

## Troubleshooting

### Issue: "No such table" error
**Solution:** Run migrations again:
```bash
python manage.py migrate
```

### Issue: Fields not showing in admin
**Solution:** 
1. Restart the Django development server
2. Clear browser cache
3. Verify that `modeltranslation` is before `django.contrib.admin` in INSTALLED_APPS

### Issue: Existing data not appearing
**Solution:** Run the update command:
```bash
python manage.py update_translation_fields
```

### Issue: Translation fields empty
**Solution:** Make sure to run all post-migration commands:
```bash
python manage.py update_translation_fields
python manage.py sync_translation_fields --noinput
```

## Rollback (if needed)

If you need to rollback these changes:

1. Identify the last migration before modeltranslation:
```bash
python manage.py showmigrations company
```

2. Migrate back to that migration:
```bash
python manage.py migrate company 0005
```

3. Remove the modeltranslation from INSTALLED_APPS in settings.py
4. Restore the original models.py file

## Data Management

### Adding New Content
When adding new services, stone types, or company info through the admin:
1. Fill in ALL language tabs
2. At minimum, fill in the Azerbaijani (default) version
3. Other languages will fall back to Azerbaijani if left empty

### Existing Data
Your existing data will be preserved in the Azerbaijani (az) fields after running the update_translation_fields command.

## Testing

After migration, test the following:

1. ✅ Admin panel loads without errors
2. ✅ Company info displays correctly in all languages
3. ✅ Services display correctly in all languages
4. ✅ Stone types display correctly in all languages
5. ✅ Contact form works
6. ✅ Language switcher changes content language

## Support

If you encounter any issues:
1. Check Django logs for detailed error messages
2. Verify all migration steps were completed
3. Ensure virtual environment is activated
4. Check that all required packages are installed
