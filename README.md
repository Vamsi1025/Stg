# Srinivasa Tiles & Sanitary

Production-ready Django website for Srinivasa Tiles & Sanitary, Gajuwaka, Visakhapatnam.

## Features
- Mobile-first responsive design (Tailwind CSS via CDN)
- Product catalog with categories (Vitrified Tiles, Bathroom Tiles, Sanitaryware, Granite)
- WhatsApp click-to-chat integration (floating + per-product buttons)
- Django Admin for product management (add/edit/delete, image upload)
- Contact form, Google Maps embed, SEO meta tags
- Category filter & search on products page
- Lazy-loaded images
- SQLite database

## Run Locally

```bash
# 1. Create virtual environment
python -m venv venv
source venv/bin/activate          # Linux/Mac
# venv\Scripts\activate           # Windows

# 2. Install dependencies
pip install -r requirements.txt

# 3. Migrate database
python manage.py migrate

# 4. Load sample products
python manage.py loaddata sample_data.json

# 5. Create admin user
python manage.py createsuperuser

# 6. Run server
python manage.py runserver
```

Visit:
- Site: http://127.0.0.1:8000/
- Admin: http://127.0.0.1:8000/admin/

## Configure WhatsApp Number
Edit `srinivasa_tiles/settings.py` and change:
```python
WHATSAPP_NUMBER = "919999999999"  # your number with country code, no +
BUSINESS_PHONE = "+91 99999 99999"
```

## Project Structure
```
srinivasa_tiles/    # Django project settings
core/               # Home, About, Contact pages
products/           # Product model, listing, admin
templates/          # HTML templates
static/             # CSS/JS
media/              # Uploaded product images
```

## Deploy Notes
- Set `DEBUG = False` and `ALLOWED_HOSTS` for production
- Run `python manage.py collectstatic`
- Use a real WSGI server (gunicorn) behind nginx
- For media uploads in production, use S3 or similar
