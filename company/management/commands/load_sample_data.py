from django.core.management.base import BaseCommand
from company.models import CompanyInfo, Service, StoneType, AboutPageContent

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
        about_data = {
            # Mission
            'mission_title_az': 'Missiyamız',
            'mission_title_en': 'Our Mission',
            'mission_title_ru': 'Наша Миссия',
            'mission_description_az': 'Precision Gems Ltd.-də bizim missiyamız müştərilərimizə ən yüksək keyfiyyətli daş kəsmə və cilalama xidmətləri təqdim etməkdir. Biz hər layihənin unikal olduğunu başa düşürük və hər bir detalda mükəmməlliyə nail olmağa çalışırıq. Təcrübəli komandamız və qabaqcıl avadanlığımızla biz müştərilərimizin təsəvvürlərini həqiqətə çeviririk.',
            'mission_description_en': 'At Precision Gems Ltd., our mission is to provide the highest quality stone cutting and polishing services to our customers. We understand that every project is unique and we strive to achieve perfection in every detail. With our experienced team and advanced equipment, we turn our customers\'  visions into reality.',
            'mission_description_ru': 'В Precision Gems Ltd. наша миссия состоит в том, чтобы предоставлять нашим клиентам услуги по резке и полировке камня высочайшего качества. Мы понимаем, что каждый проект уникален, и стремимся к совершенству в каждой детали. С нашей опытной командой и современным оборудованием мы превращаем видение наших клиентов в реальность.',
            
            # Vision
            'vision_title_az': 'Vizyonumuz',
            'vision_title_en': 'Our Vision',
            'vision_title_ru': 'Наше Видение',
            'vision_description_az': 'Bizim vizyonumuz daş emal sənayesində lider olmaq, innovasiya, keyfiyyət və müştəri məmnuniyyətində standartlar yaratmaqdır. Biz davamlı təkmilləşmə və texnoloji irəliləyişlərə sadiq qalaraq, hər bir layihədə gözəl və davamlı nəticələr verməyə çalışırıq.',
            'vision_description_en': 'Our vision is to be a leader in the stone processing industry, setting standards for innovation, quality, and customer satisfaction. We strive to deliver beautiful and lasting results in every project, while staying committed to continuous improvement and technological advancement.',
            'vision_description_ru': 'Наше видение — быть лидером в индустрии обработки камня, устанавливая стандарты инноваций, качества и удовлетворенности клиентов. Мы стремимся обеспечивать красивые и долговечные результаты в каждом проекте, сохраняя приверженность постоянному совершенствованию и технологическому прогрессу.',
            
            # Quality
            'quality_title_az': 'Keyfiyyətli İşçilik',
            'quality_title_en': 'Quality Craftsmanship',
            'quality_title_ru': 'Качественное Мастерство',
            'quality_description_az': 'Hər detalda mükəmməlliyə nail olmaq üçün təcrübəli ustaların bacarıqları',
            'quality_description_en': 'Skilled artisans delivering perfection in every detail',
            'quality_description_ru': 'Опытные мастера достигают совершенства в каждой детали',
            
            # Delivery
            'delivery_title_az': 'Vaxtında Çatdırılma',
            'delivery_title_en': 'Timely Delivery',
            'delivery_title_ru': 'Своевременная Доставка',
            'delivery_description_az': 'Keyfiyyətdən güzəştə getmədən layihələrin vaxtında tamamlanması',
            'delivery_description_en': 'Projects completed on time without compromising quality',
            'delivery_description_ru': 'Проекты выполняются вовремя без ущерба для качества',
            
            # Team
            'team_title_az': 'Ekspert Komanda',
            'team_title_en': 'Expert Team',
            'team_title_ru': 'Команда Экспертов',
            'team_description_az': '15+ il təcrübəsi olan peşəkar daş emalı mütəxəssisləri',
            'team_description_en': 'Professional stone processing specialists with 15+ years experience',
            'team_description_ru': 'Профессиональные специалисты по обработке камня с опытом 15+ лет',
            
            # Equipment
            'equipment_title_az': 'Müasir Avadanlıq',
            'equipment_title_en': 'Modern Equipment',
            'equipment_title_ru': 'Современное Оборудование',
            'equipment_description_az': 'Dəqiq və səmərəli emal üçün ən son texnologiya',
            'equipment_description_en': 'State-of-the-art technology for precise and efficient processing',
            'equipment_description_ru': 'Передовые технологии для точной и эффективной обработки',
            
            # Guarantee
            'guarantee_title_az': 'Keyfiyyət Zəmanəti',
            'guarantee_title_en': 'Quality Guarantee',
            'guarantee_title_ru': 'Гарантия Качества',
            'guarantee_description_az': 'Bütün xidmətlərimiz üzrə tam məmnuniyyət zəmanəti',
            'guarantee_description_en': 'Full satisfaction guarantee on all our services',
            'guarantee_description_ru': 'Полная гарантия удовлетворения по всем нашим услугам',
            
            # Customer Focus
            'customer_title_az': 'Müştəri Mərkəzli',
            'customer_title_en': 'Customer Focus',
            'customer_title_ru': 'Ориентация на Клиента',
            'customer_description_az': 'Sizin ehtiyaclarınız və məmnuniyyətiniz bizim əsas prioritetimizdir',
            'customer_description_en': 'Your needs and satisfaction are our top priority',
            'customer_description_ru': 'Ваши потребности и удовлетворение — наш главный приоритет',
            
            # Non-translatable field
            'is_active': True
        }
        
        AboutPageContent.objects.all().delete()  # Clear existing content
        AboutPageContent.objects.create(**about_data)
        
        self.stdout.write(
            self.style.SUCCESS('Successfully loaded sample data for Precision Gems Ltd. in 3 languages (az, en, ru)!')
        )
