from django.core.management.base import BaseCommand
from company.models import CompanyInfo, Service, StoneType, AboutPageContent, NavigationItem, BusinessHours, SiteSettings, HomePageContent, ServicesPageContent, StoneTypesPageContent, ContactPageContent

class Command(BaseCommand):
    help = 'Load sample data for Precision Gems Ltd. in 3 languages (Azerbaijani, English, Russian)'

    def handle(self, *args, **options):
        self.stdout.write('Loading sample data for Precision Gems Ltd. (az, en, ru)...')
        
        # Create or update company info with all 3 languages
        company, created = CompanyInfo.objects.update_or_create(
            name_az="Precision Gems Ltd.",
            defaults={
                # Azerbaijani
                'name_az': "Precision Gems Ltd.",
                'tagline_az': 'Premium Daş Kəsimi və Cilalama Xidmətləri',
                'description_az': 'Sənayedə 15 ildən artıq təcrübəyə malik peşəkar daş kəsmə və cilalama xidmətləri. Biz bütün təbii daş növlərinin dəqiq kəsimi üzrə ixtisaslaşmışıq.',
                'address_az': '123 Gem Street, Stone City, SC 12345',
                
                # English
                'name_en': "Precision Gems Ltd.",
                'tagline_en': 'Premium Stone Cutting and Polishing Services',
                'description_en': 'Professional stone cutting and polishing services with over 15 years of experience in the industry. We specialize in precision cutting of all natural stone types.',
                'address_en': '123 Gem Street, Stone City, SC 12345',
                
                # Russian
                'name_ru': "Precision Gems Ltd.",
                'tagline_ru': 'Премиум Услуги по Резке и Полировке Камня',
                'description_ru': 'Профессиональные услуги по резке и полировке камня с более чем 15-летним опытом работы в отрасли. Мы специализируемся на точной резке всех типов натурального камня.',
                'address_ru': '123 Gem Street, Stone City, SC 12345',
                
                # Non-translatable fields
                'phone': '+1 (555) 123-4567',
                'email': 'info@precisiongems.com',
                'website': 'https://www.precisiongems.com',
                'is_active': True
            }
        )
        
        # Create services with all 3 languages
        services_data = [
            {
                'name_az': 'Dəqiq Kəsim',
                'name_en': 'Precision Cutting',
                'name_ru': 'Точная Резка',
                'description_az': 'Mükəmməl kənarlar və ölçülər üçün qabaqcıl almaz uclu alətlərdən istifadə edərək yüksək dəqiqlikli daş kəsimi.',
                'description_en': 'High-precision stone cutting using advanced diamond-tipped tools for perfect edges and dimensions.',
                'description_ru': 'Высокоточная резка камня с использованием современных алмазных инструментов для идеальных краев и размеров.',
                'icon': 'fas fa-cut',
                'display_order': 1,
                'is_active': True
            },
            {
                'name_az': 'Fərdi Formalaşdırma',
                'name_en': 'Custom Shaping',
                'name_ru': 'Индивидуальная Формовка',
                'description_az': 'Unikal memarlıq və dizayn tələbləri üçün fərdi daş formalaşdırma xidmətləri.',
                'description_en': 'Custom stone shaping services for unique architectural and design requirements.',
                'description_ru': 'Услуги индивидуальной формовки камня для уникальных архитектурных и дизайнерских требований.',
                'icon': 'fas fa-draw-polygon',
                'display_order': 2,
                'is_active': True
            },
            {
                'name_az': 'Cilalama',
                'name_en': 'Polishing',
                'name_ru': 'Полировка',
                'description_az': 'Daşlarınızın təbii gözəlliyini və parıltısını üzə çıxarmaq üçün peşəkar cilalama xidmətləri.',
                'description_en': 'Professional polishing services to bring out the natural beauty and shine of your stones.',
                'description_ru': 'Профессиональные услуги полировки для раскрытия естественной красоты и блеска ваших камней.',
                'icon': 'fas fa-sparkles',
                'display_order': 3,
                'is_active': True
            },
            {
                'name_az': 'Kənar Profilləmə',
                'name_en': 'Edge Profiling',
                'name_ru': 'Профилирование Краев',
                'description_az': 'Mətbəx səthləri, pilləkənlər və dekorativ elementlər üçün ixtisaslaşmış kənar profilləmə.',
                'description_en': 'Specialized edge profiling for kitchen countertops, stairs, and decorative elements.',
                'description_ru': 'Специализированное профилирование краев для кухонных столешниц, лестниц и декоративных элементов.',
                'icon': 'fas fa-border-style',
                'display_order': 4,
                'is_active': True
            },
        ]
        
        for service_data in services_data:
            Service.objects.update_or_create(
                name_az=service_data['name_az'],  # Lookup by Azerbaijani name
                defaults=service_data
            )
        
        # Create stone types with all 3 languages
        stone_types_data = [
            {
                'name_az': 'Qranit',
                'name_en': 'Granite',
                'name_ru': 'Гранит',
                'description_az': 'Mətbəx səthləri və gediş-gəlişin çox olduğu yerlər üçün mükəmməl olan davamlı vulkanik daş. Sərtliyi və rəng müxtəlifliyi ilə tanınır.',
                'description_en': 'Durable igneous rock perfect for kitchen countertops and high-traffic areas. Known for its hardness and variety of colors.',
                'description_ru': 'Прочная вулканическая порода, идеально подходящая для кухонных столешниц и мест с высокой проходимостью. Известна своей твердостью и разнообразием цветов.',
                'display_order': 1,
                'is_active': True
            },
            {
                'name_az': 'Mərmər',
                'name_en': 'Marble',
                'name_ru': 'Мрамор',
                'description_az': 'Gözəl damarları olan zərif metamorfik daş. Dekorativ parçalar və lüks səthlər üçün idealdır.',
                'description_en': 'Elegant metamorphic stone with beautiful veining patterns. Ideal for decorative pieces and luxury surfaces.',
                'description_ru': 'Элегантный метаморфический камень с красивыми прожилками. Идеален для декоративных элементов и роскошных поверхностей.',
                'display_order': 2,
                'is_active': True
            },
            {
                'name_az': 'Kvarsit',
                'name_en': 'Quartzite',
                'name_ru': 'Кварцит',
                'description_az': 'Qranitin davamlılığına və mərmərin gözəlliyinə malik təbii daş. İstiyə və cızıqlara qarşı davamlıdır.',
                'description_en': 'Natural stone with the durability of granite and the beauty of marble. Resistant to heat and scratches.',
                'description_ru': 'Натуральный камень с прочностью гранита и красотой мрамора. Устойчив к высоким температурам и царапинам.',
                'display_order': 3,
                'is_active': True
            },
            {
                'name_az': 'Oniks',
                'name_en': 'Onyx',
                'name_ru': 'Оникс',
                'description_az': 'Möhtəşəm vizual dərinliyə malik yarı şəffaf daş. Arxa işıqlandırmalı xüsusiyyətlər və dekorativ elementlər üçün idealdır.',
                'description_en': 'Translucent stone with dramatic visual depth. Perfect for backlit features and decorative elements.',
                'description_ru': 'Полупрозрачный камень с впечатляющей визуальной глубиной. Идеален для подсвечиваемых элементов и декора.',
                'display_order': 4,
                'is_active': True
            },
            {
                'name_az': 'Kvars',
                'name_en': 'Quartz',
                'name_ru': 'Кварц',
                'description_az': 'Naxış və rəngdə sabitlik təklif edən mühəndis daşı. Məsaməsizdir və az qulluq tələb edir.',
                'description_en': 'Engineered stone offering consistency in pattern and color. Non-porous and requires minimal maintenance.',
                'description_ru': 'Искусственный камень, обеспечивающий постоянство рисунка и цвета. Непористый и требует минимального ухода.',
                'display_order': 5,
                'is_active': True
            },
        ]
        
        for stone_data in stone_types_data:
            StoneType.objects.update_or_create(
                name_az=stone_data['name_az'],  # Lookup by Azerbaijani name
                defaults=stone_data
            )
        
        # Create or update About Page Content with all 3 languages
        # Note: We need to use django-modeltranslation to set values for each language
        from django.utils import translation
        
        AboutPageContent.objects.all().delete()  # Clear existing content
        about_content = AboutPageContent.objects.create(is_active=True)
        
        # Azerbaijani (az)
        translation.activate('az')
        about_content.mission_title = 'Missiyamız'
        about_content.mission_description = 'Precision Gems Ltd.-də bizim missiyamız müştərilərimizə ən yüksək keyfiyyətli daş kəsmə və cilalama xidmətləri təqdim etməkdir. Biz hər layihənin unikal olduğunu başa düşürük və hər bir detalda mükəmməlliyə nail olmağa çalışırıq. Təcrübəli komandamız və qabaqcıl avadanlığımızla biz müştərilərimizin təsəvvürlərini həqiqətə çeviririk.'
        about_content.vision_title = 'Vizyonumuz'
        about_content.vision_description = 'Bizim vizyonumuz daş emal sənayesində lider olmaq, innovasiya, keyfiyyət və müştəri məmnuniyyətində standartlar yaratmaqdır. Biz davamlı təkmilləşmə və texnoloji irəliləyişlərə sadiq qalaraq, hər bir layihədə gözəl və davamlı nəticələr verməyə çalışırıq.'
        about_content.quality_title = 'Keyfiyyətli İşçilik'
        about_content.quality_description = 'Hər detalda mükəmməlliyə nail olmaq üçün təcrübəli ustaların bacarıqları'
        about_content.delivery_title = 'Vaxtında Çatdırılma'
        about_content.delivery_description = 'Keyfiyyətdən güzəştə getmədən layihələrin vaxtında tamamlanması'
        about_content.team_title = 'Ekspert Komanda'
        about_content.team_description = '15+ il təcrübəsi olan peşəkar daş emalı mütəxəssisləri'
        about_content.equipment_title = 'Müasir Avadanlıq'
        about_content.equipment_description = 'Dəqiq və səmərəli emal üçün ən son texnologiya'
        about_content.guarantee_title = 'Keyfiyyət Zəmanəti'
        about_content.guarantee_description = 'Bütün xidmətlərimiz üzrə tam məmnuniyyət zəmanəti'
        about_content.customer_title = 'Müştəri Mərkəzli'
        about_content.customer_description = 'Sizin ehtiyaclarınız və məmnuniyyətiniz bizim əsas prioritetimizdir'
        about_content.save()
        
        # English (en)
        translation.activate('en')
        about_content.mission_title = 'Our Mission'
        about_content.mission_description = 'At Precision Gems Ltd., our mission is to provide the highest quality stone cutting and polishing services to our customers. We understand that every project is unique and we strive to achieve perfection in every detail. With our experienced team and advanced equipment, we turn our customers\' visions into reality.'
        about_content.vision_title = 'Our Vision'
        about_content.vision_description = 'Our vision is to be a leader in the stone processing industry, setting standards for innovation, quality, and customer satisfaction. We strive to deliver beautiful and lasting results in every project, while staying committed to continuous improvement and technological advancement.'
        about_content.quality_title = 'Quality Craftsmanship'
        about_content.quality_description = 'Skilled artisans delivering perfection in every detail'
        about_content.delivery_title = 'Timely Delivery'
        about_content.delivery_description = 'Projects completed on time without compromising quality'
        about_content.team_title = 'Expert Team'
        about_content.team_description = 'Professional stone processing specialists with 15+ years experience'
        about_content.equipment_title = 'Modern Equipment'
        about_content.equipment_description = 'State-of-the-art technology for precise and efficient processing'
        about_content.guarantee_title = 'Quality Guarantee'
        about_content.guarantee_description = 'Full satisfaction guarantee on all our services'
        about_content.customer_title = 'Customer Focus'
        about_content.customer_description = 'Your needs and satisfaction are our top priority'
        about_content.save()
        
        # Russian (ru)
        translation.activate('ru')
        about_content.mission_title = 'Наша Миссия'
        about_content.mission_description = 'В Precision Gems Ltd. наша миссия состоит в том, чтобы предоставлять нашим клиентам услуги по резке и полировке камня высочайшего качества. Мы понимаем, что каждый проект уникален, и стремимся к совершенству в каждой детали. С нашей опытной командой и современным оборудованием мы превращаем видение наших клиентов в реальность.'
        about_content.vision_title = 'Наше Видение'
        about_content.vision_description = 'Наше видение — быть лидером в индустрии обработки камня, устанавливая стандарты инноваций, качества и удовлетворенности клиентов. Мы стремимся обеспечивать красивые и долговечные результаты в каждом проекте, сохраняя приверженность постоянному совершенствованию и технологическому прогрессу.'
        about_content.quality_title = 'Качественное Мастерство'
        about_content.quality_description = 'Опытные мастера достигают совершенства в каждой детали'
        about_content.delivery_title = 'Своевременная Доставка'
        about_content.delivery_description = 'Проекты выполняются вовремя без ущерба для качества'
        about_content.team_title = 'Команда Экспертов'
        about_content.team_description = 'Профессиональные специалисты по обработке камня с опытом 15+ лет'
        about_content.equipment_title = 'Современное Оборудование'
        about_content.equipment_description = 'Передовые технологии для точной и эффективной обработки'
        about_content.guarantee_title = 'Гарантия Качества'
        about_content.guarantee_description = 'Полная гарантия удовлетворения по всем нашим услугам'
        about_content.customer_title = 'Ориентация на Клиента'
        about_content.customer_description = 'Ваши потребности и удовлетворение — наш главный приоритет'
        about_content.save()
        
        translation.deactivate()
        
        # Create or update Site Settings
        site_settings, created = SiteSettings.objects.update_or_create(
            site_title_az="Precision Gems Ltd.",
            defaults={
                'site_title_az': "Precision Gems Ltd.",
                'site_title_en': "Precision Gems Ltd.",
                'site_title_ru': "Precision Gems Ltd.",
                'default_phone': '+994501234567',
                'enable_contact_form': True,
                'footer_text_az': 'Premium Daş Kəsimi və Cilalama Xidmətləri',
                'footer_text_en': 'Premium Stone Cutting and Polishing Services',
                'footer_text_ru': 'Премиум Услуги по Резке и Полировке Камня',
                'copyright_text_az': '© 2024 Precision Gems Ltd. Bütün hüquqlar qorunur.',
                'copyright_text_en': '© 2024 Precision Gems Ltd. All rights reserved.',
                'copyright_text_ru': '© 2024 Precision Gems Ltd. Все права защищены.',
                'is_active': True
            }
        )
        
        # Create Navigation Items
        navigation_data = [
            {
                'title_az': 'Ana Səhifə',
                'title_en': 'Home',
                'title_ru': 'Главная',
                'url_name': 'home',
                'icon': 'fas fa-home',
                'display_order': 1,
                'is_active': True
            },
            {
                'title_az': 'Haqqımızda',
                'title_en': 'About',
                'title_ru': 'О нас',
                'url_name': 'about',
                'icon': 'fas fa-info-circle',
                'display_order': 2,
                'is_active': True
            },
            {
                'title_az': 'Xidmətlər',
                'title_en': 'Services',
                'title_ru': 'Услуги',
                'url_name': 'services',
                'icon': 'fas fa-cogs',
                'display_order': 3,
                'is_active': True
            },
            {
                'title_az': 'Daş Növləri',
                'title_en': 'Stone Types',
                'title_ru': 'Типы Камня',
                'url_name': 'stone_types',
                'icon': 'fas fa-gem',
                'display_order': 4,
                'is_active': True
            },
            {
                'title_az': 'Əlaqə',
                'title_en': 'Contact',
                'title_ru': 'Контакты',
                'url_name': 'contact',
                'icon': 'fas fa-envelope',
                'display_order': 5,
                'is_active': True
            },
        ]
        
        for nav_data in navigation_data:
            NavigationItem.objects.update_or_create(
                url_name=nav_data['url_name'],
                defaults=nav_data
            )
        
        # Create Business Hours
        business_hours_data = [
            {
                'day_label_az': 'Bazar ertəsi - Cümə',
                'day_label_en': 'Monday - Friday',
                'day_label_ru': 'Понедельник - Пятница',
                'time_range': '8:00 AM - 6:00 PM',
                'is_closed': False,
                'display_order': 1,
                'is_active': True
            },
            {
                'day_label_az': 'Şənbə',
                'day_label_en': 'Saturday',
                'day_label_ru': 'Суббота',
                'time_range': '9:00 AM - 2:00 PM',
                'is_closed': False,
                'display_order': 2,
                'is_active': True
            },
            {
                'day_label_az': 'Bazar',
                'day_label_en': 'Sunday',
                'day_label_ru': 'Воскресенье',
                'time_range': 'Bağlı',
                'is_closed': True,
                'display_order': 3,
                'is_active': True
            },
        ]
        
        for hours_data in business_hours_data:
            BusinessHours.objects.update_or_create(
                day_label_az=hours_data['day_label_az'],
                defaults=hours_data
            )
        
        # Create Home Page Content
        HomePageContent.objects.all().delete()
        home_content = HomePageContent.objects.create(is_active=True)
        
        translation.activate('az')
        home_content.services_title = 'Xidmətlərimiz'
        home_content.services_subtitle = 'Ehtiyaclarınıza uyğun tam həllli daş emal həlləri'
        home_content.stone_types_title = 'İşlədiyimiz Daş Növləri'
        home_content.stone_types_subtitle = 'Müxtəlif daş materialları üçün ekspert emal'
        home_content.cta_title = 'Daş Materiallarınızı Dəyişdirməyə Hazırsınız?'
        home_content.cta_subtitle = 'Pulsuz konsultasiya və qiymət təklifi üçün bu gün bizimlə əlaqə saxlayın!'
        home_content.get_quote_button = 'Pulsuz Qiymət Alın'
        home_content.our_services_button = 'Xidmətlərimiz'
        home_content.view_all_services_button = 'Bütün Xidmətlərə Baxın'
        home_content.view_all_stones_button = 'Bütün Daş Növlərinə Baxın'
        home_content.start_project_button = 'Layihənizi Başladın'
        home_content.call_now_button = 'İndi Zəng Edin'
        home_content.save()
        
        translation.activate('en')
        home_content.services_title = 'Our Services'
        home_content.services_subtitle = 'Comprehensive stone processing solutions tailored to your needs'
        home_content.stone_types_title = 'Stone Types We Work With'
        home_content.stone_types_subtitle = 'Expert processing for various stone materials'
        home_content.cta_title = 'Ready to Transform Your Stone Materials?'
        home_content.cta_subtitle = 'Contact us today for a free consultation and quote!'
        home_content.get_quote_button = 'Get Free Quote'
        home_content.our_services_button = 'Our Services'
        home_content.view_all_services_button = 'View All Services'
        home_content.view_all_stones_button = 'View All Stone Types'
        home_content.start_project_button = 'Start Your Project'
        home_content.call_now_button = 'Call Now'
        home_content.save()
        
        translation.activate('ru')
        home_content.services_title = 'Наши Услуги'
        home_content.services_subtitle = 'Комплексные решения по обработке камня, адаптированные к вашим потребностям'
        home_content.stone_types_title = 'Типы Камня, с Которыми Мы Работаем'
        home_content.stone_types_subtitle = 'Экспертная обработка различных каменных материалов'
        home_content.cta_title = 'Готовы Преобразовать Ваши Каменные Материалы?'
        home_content.cta_subtitle = 'Свяжитесь с нами сегодня для бесплатной консультации и расчета стоимости!'
        home_content.get_quote_button = 'Получить Бесплатную Расценку'
        home_content.our_services_button = 'Наши Услуги'
        home_content.view_all_services_button = 'Посмотреть Все Услуги'
        home_content.view_all_stones_button = 'Посмотреть Все Типы Камня'
        home_content.start_project_button = 'Начать Ваш Проект'
        home_content.call_now_button = 'Позвонить Сейчас'
        home_content.save()
        
        # Create Services Page Content
        ServicesPageContent.objects.all().delete()
        services_content = ServicesPageContent.objects.create(is_active=True)
        
        translation.activate('az')
        services_content.page_title = 'Xidmətlərimiz'
        services_content.page_subtitle = 'Bütün ehtiyaclarınız üçün tam həllli daş emal həlləri'
        services_content.cta_title = 'Başlamağa Hazırsınız?'
        services_content.cta_subtitle = 'Layihə tələblərinizi müzakirə etmək üçün bu gün bizimlə əlaqə saxlayın'
        services_content.consultation_button = 'Pulsuz Konsultasiya Alın'
        services_content.save()
        
        translation.activate('en')
        services_content.page_title = 'Our Services'
        services_content.page_subtitle = 'Comprehensive stone processing solutions for all your needs'
        services_content.cta_title = 'Ready to Get Started?'
        services_content.cta_subtitle = 'Contact us today to discuss your project requirements'
        services_content.consultation_button = 'Get Free Consultation'
        services_content.save()
        
        translation.activate('ru')
        services_content.page_title = 'Наши Услуги'
        services_content.page_subtitle = 'Комплексные решения по обработке камня для всех ваших потребностей'
        services_content.cta_title = 'Готовы Начать?'
        services_content.cta_subtitle = 'Свяжитесь с нами сегодня, чтобы обсудить требования к вашему проекту'
        services_content.consultation_button = 'Получить Бесплатную Консультацию'
        services_content.save()
        
        # Create Stone Types Page Content
        StoneTypesPageContent.objects.all().delete()
        stone_types_content = StoneTypesPageContent.objects.create(is_active=True)
        
        translation.activate('az')
        stone_types_content.page_title = 'İşlədiyimiz Daş Növləri'
        stone_types_content.page_subtitle = 'Müxtəlif təbii daş materialları üçün ekspert emal'
        stone_types_content.cta_title = 'Hansı Daşın Sizin Üçün Uyğun Olduğuna Əminsiniz?'
        stone_types_content.cta_subtitle = 'Ekspertlərimiz layihəniz üçün mükəmməl daşı seçməyinizə kömək edə bilər'
        stone_types_content.expert_advice_button = 'Ekspert Məsləhəti Alın'
        stone_types_content.save()
        
        translation.activate('en')
        stone_types_content.page_title = 'Stone Types We Work With'
        stone_types_content.page_subtitle = 'Expert processing for various natural stone materials'
        stone_types_content.cta_title = 'Not Sure Which Stone is Right for You?'
        stone_types_content.cta_subtitle = 'Our experts can help you choose the perfect stone for your project'
        stone_types_content.expert_advice_button = 'Get Expert Advice'
        stone_types_content.save()
        
        translation.activate('ru')
        stone_types_content.page_title = 'Типы Камня, с Которыми Мы Работаем'
        stone_types_content.page_subtitle = 'Экспертная обработка различных натуральных каменных материалов'
        stone_types_content.cta_title = 'Не Уверены, Какой Камень Подходит Вам?'
        stone_types_content.cta_subtitle = 'Наши эксперты могут помочь вам выбрать идеальный камень для вашего проекта'
        stone_types_content.expert_advice_button = 'Получить Экспертный Совет'
        stone_types_content.save()
        
        # Create Contact Page Content
        ContactPageContent.objects.all().delete()
        contact_content = ContactPageContent.objects.create(is_active=True)
        
        translation.activate('az')
        contact_content.page_title = 'Əlaqə'
        contact_content.page_subtitle = 'Ekspert komandamızla əlaqə saxlayın'
        contact_content.form_title = 'Bizə Mesaj Göndərin'
        contact_content.contact_info_title = 'Əlaqə Məlumatları'
        contact_content.send_message_button = 'Mesaj Göndərin'
        contact_content.save()
        
        translation.activate('en')
        contact_content.page_title = 'Contact Us'
        contact_content.page_subtitle = 'Get in touch with our expert team'
        contact_content.form_title = 'Send us a Message'
        contact_content.contact_info_title = 'Contact Information'
        contact_content.send_message_button = 'Send Message'
        contact_content.save()
        
        translation.activate('ru')
        contact_content.page_title = 'Контакты'
        contact_content.page_subtitle = 'Свяжитесь с нашей командой экспертов'
        contact_content.form_title = 'Отправить Нам Сообщение'
        contact_content.contact_info_title = 'Контактная Информация'
        contact_content.send_message_button = 'Отправить Сообщение'
        contact_content.save()
        
        translation.deactivate()
        
        self.stdout.write(
            self.style.SUCCESS('Successfully loaded sample data for Precision Gems Ltd. in 3 languages (az, en, ru)!')
        )
