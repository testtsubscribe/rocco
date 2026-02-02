# Rocco Ltd. - Corporate Website

A modern, responsive corporate website for a stone cutting and polishing company built with Django.

## 🏢 About The Project

Rocco Ltd. specializes in premium stone cutting, polishing, and finishing services for gemstones, marble, granite, and decorative stones. This website showcases their services, stone types, and provides a professional online presence.

## ✨ Features

- Modern Responsive Design - Works perfectly on all devices
- Professional UI/UX - Clean, corporate design with Bootstrap 5
- Essential Business Pages - Home, About, Services, Stone Types, Contact
- Functional Contact Form - Database-backed inquiry system
- Admin Interface - Full Django admin for content management
- Sample Data - Pre-loaded with realistic company information

## 🛠 Technology Stack

- **Backend:** Django 4.2+
- **Frontend:** Bootstrap 5, Font Awesome
- **Database:** SQLite (development)
- **Templates:** Django Template Language
- **Static Files:** CSS3, JavaScript

## 📁 Project Structure

```
precisiongems/
├── manage.py
├── requirements.txt
├── rocco/                # Project configuration
├── company/              # Main application
│   ├── models.py         # Database models
│   ├── views.py          # View functions
│   ├── admin.py          # Admin configuration
│   ├── management/
│   │   └── commands/     # Custom management commands
├── templates/            # HTML templates
│   └── company/
├── static/               # CSS, JS, images
└── db.sqlite3            # Database (created after setup)
```

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Installation Steps

1. **Clone or download the project:**
   ```bash
   cd precisiongems
   ```

2. **Create and activate virtual environment:**
   ```bash
   # Linux/Mac
   python3 -m venv venv
   source venv/bin/activate

   # Windows
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run setup commands:**
   ```bash
   # Create database tables
   python manage.py makemigrations
   python manage.py migrate

   # Load sample data
   python manage.py load_sample_data

   # Collect static files
   python manage.py collectstatic --noinput
   ```

5. **Create admin user (optional):**
   ```bash
   python manage.py createsuperuser
   ```

6. **Start development server:**
   ```bash
   python manage.py runserver
   ```

7. **Access the website:**
   - Main site: `http://127.0.0.1:8000`
   - Admin panel: `http://127.0.0.1:8000/admin`

### 🎯 One-Line Setup Scripts

**Linux/Mac:**
```bash
chmod +x setup.sh && ./setup.sh
```

**Windows:**
```cmd
setup.bat
```

## 📋 Available Management Commands

```bash
# Start development server
python manage.py runserver

# Load sample company data
python manage.py load_sample_data

# Create database migrations
python manage.py makemigrations

# Apply database migrations
python manage.py migrate

# Create admin user
python manage.py createsuperuser

# Collect static files for production
python manage.py collectstatic
```

## 🗃 Database Models

- **CompanyInfo** - Company details and contact information
- **Service** - Stone processing services offered
- **StoneType** - Types of stones worked with
- **ContactInquiry** - Customer contact form submissions

## 🎨 Customization

### Updating Company Information

1. Access the admin panel: `/admin`
2. Navigate to "Company Information"
3. Update company details, contact information, and description

### Adding New Services

1. Go to Admin → Company → Services
2. Click "Add Service"
3. Fill in:
   - Name
   - Description
   - Font Awesome icon class
   - Display order

### Modifying Stone Types

1. Admin → Company → Stone Types
2. Add or edit stone types with descriptions

## 🌐 Pages Overview

- **Home** (`/`) - Hero section, services preview, stone types
- **About** (`/about/`) - Company story, mission, vision
- **Services** (`/services/`) - Detailed services list
- **Stone Types** (`/stone-types/`) - Stone materials worked with
- **Contact** (`/contact/`) - Contact form and company info

## 🔧 Development

### Adding New Features

1. Create new models in `company/models.py`
2. Generate migrations: `python manage.py makemigrations`
3. Apply migrations: `python manage.py migrate`
4. Create views in `company/views.py`
5. Add URL patterns in `company/urls.py`
6. Create templates in `templates/company/`

### Static Files

- **CSS:** `static/css/custom.css`
- **JavaScript:** `static/js/main.js`
- **Images:** `static/images/`

### Template Structure

- `base.html` - Main layout template
- `home.html` - Homepage
- `about.html` - About page
- `services.html` - Services listing
- `contact.html` - Contact form

## 🚨 Troubleshooting

### "no such table" error
```bash
python manage.py makemigrations
python manage.py migrate
```

### Static files not loading
```bash
python manage.py collectstatic
```

### Module not found errors
```bash
pip install -r requirements.txt
```

### Database connection issues
- Delete `db.sqlite3`
- Re-run migrations

### Reset Database
```bash
# Delete database and start fresh
rm db.sqlite3
python manage.py makemigrations
python manage.py migrate
python manage.py load_sample_data
```

## 📞 Support

For issues or questions:
- Check the troubleshooting section above
- Verify all installation steps were followed
- Ensure virtual environment is activated
- Confirm database migrations are applied

## 🎉 Success Checklist

After installation, verify:
- ✅ Website loads at `http://127.0.0.1:8000`
- ✅ All pages are accessible (Home, About, Services, Contact)
- ✅ Sample data is displayed (services, stone types)
- ✅ Contact form works and saves submissions
- ✅ Admin panel is accessible at `/admin`
- ✅ Website is responsive on different screen sizes

## 📄 License

This project is for demonstration purposes. Feel free to use as a template for corporate websites.

---

**Rocco Ltd.** - Transforming Raw Stones into Exquisite Finished Products

