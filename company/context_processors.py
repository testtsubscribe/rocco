from .models import CompanyInfo, NavigationItem, SiteSettings, HomePageContent, ServicesPageContent, StoneTypesPageContent, ContactPageContent

def company_info(request):
    try:
        company = CompanyInfo.objects.filter(is_active=True).first()
    except CompanyInfo.DoesNotExist:
        company = None
    
    try:
        navigation_items = NavigationItem.objects.filter(is_active=True)
    except:
        navigation_items = []
    
    try:
        site_settings = SiteSettings.objects.filter(is_active=True).first()
    except:
        site_settings = None
    
    try:
        home_content = HomePageContent.objects.filter(is_active=True).first()
    except:
        home_content = None
    
    try:
        services_content = ServicesPageContent.objects.filter(is_active=True).first()
    except:
        services_content = None
    
    try:
        stone_types_content = StoneTypesPageContent.objects.filter(is_active=True).first()
    except:
        stone_types_content = None
    
    try:
        contact_content = ContactPageContent.objects.filter(is_active=True).first()
    except:
        contact_content = None
    
    return {
        'company': company,
        'navigation_items': navigation_items,
        'site_settings': site_settings,
        'home_content': home_content,
        'services_content': services_content,
        'stone_types_content': stone_types_content,
        'contact_content': contact_content,
    }
