# 🍽️ SaaS Restaurant POS System

![Python](https://img.shields.io/badge/Python-3.11.9-blue)
![Django](https://img.shields.io/badge/Django-4.2.28-green)
![SQLite](https://img.shields.io/badge/Database-SQLite-lightgrey)
![Status](https://img.shields.io/badge/Status-Production%20Ready-success)

## 📌 Overview

SaaS Restaurant POS System is a full-stack Django-based web application designed to help restaurant owners efficiently manage their restaurants, staff, menus, orders, billing, QR-based ordering, reports, and customer operations through a centralized dashboard.

This project follows a SaaS (Software as a Service) architecture where multiple restaurants can be managed through a single platform with role-based access control.

---

## 🚀 Key Features

### 🔐 Authentication & Security
- User Registration & Login
- Role-Based Access Control (6 roles)
- Failed Login Attempt Protection
- Secure Dashboard Access

### 🏢 Restaurant Management
- Create & Manage Restaurants
- Restaurant Profile Settings
- Restaurant Logo Management
- Location-based Configuration

### 🍔 Menu Management
- Add/Edit/Delete Menu Items
- Food Categories
- Item Add-ons & Customizations
- Image Upload Support

### 👨‍🍳 Staff Management
- Add Staff Members
- Assign Roles (Manager, Waiter, Kitchen)
- Manage Staff Accounts
- Role-Based Staff Access

### 🍽️ Order Management
- Create Orders
- Real-time Order Tracking
- Order History
- Kitchen Order Updates

### 📱 QR Code Ordering
- QR Code Generation per Table
- Contactless Ordering
- Customer Self-Service Ordering

### 💳 Billing & Payments
- Automatic Bill Generation
- Receipt Generation
- Cash & Online Payment Support
- Payment Tracking

### 📊 Reports & Analytics
- Revenue Reports
- Order Reports
- Staff Performance Reports
- Operational Insights

---

## 🛠️ Tech Stack

- **Backend:** Python 3.11.9, Django 4.2.28
- **Frontend:** HTML5, CSS3, JavaScript
- **Database:** SQLite3
- **Libraries:** OpenCV, Pillow, QRCode, Razorpay
- **Server:** Django Development Server / Gunicorn

---

## ⚙️ Installation & Setup

### Prerequisites
- Python 3.11.9+
- pip (Python package manager)
- Virtual Environment (venv)

### Quick Start

```bash
# 1. Navigate to project
cd saas_pos

# 2. Activate virtual environment
.\venv\Scripts\Activate.ps1

# 3. Install dependencies
pip install -r requirements.txt

# 4. Apply migrations
python manage.py migrate

# 5. Run development server
python manage.py runserver
```

### Access Application
```
URL: http://127.0.0.1:8000/
Username: admin
Password: admin123
```

---

## 🏃 Running the Application

### Development
```bash
.\venv\Scripts\Activate.ps1
python manage.py runserver
```

### Production (with Gunicorn)
```bash
.\venv\Scripts\Activate.ps1
gunicorn config.wsgi:application --bind 0.0.0.0:8000
```

### Management Commands
```bash
# Create superuser
python manage.py createsuperuser

# Apply migrations
python manage.py migrate

# Check system
python manage.py check

# Collect static files
python manage.py collectstatic

# Run tests
python manage.py test
```

---

## 📁 Project Structure

```
saas_pos/
├── accounts/          → User authentication & models
├── restaurants/       → Main business logic
├── config/           → Django settings & URLs
├── templates/        → HTML templates (32 files)
├── static/           → CSS, JS, static assets
├── media/            → User uploads
├── db.sqlite3        → SQLite database
├── manage.py         → Django management
├── requirements.txt  → Python dependencies
└── venv/            → Virtual environment
```

---

## 🔐 User Roles

1. **SUPERADMIN** - Full system access, manage all restaurants
2. **RESTAURANT_ADMIN** - Own restaurant owner, full restaurant control
3. **MANAGER** - Restaurant manager, manage staff & operations
4. **WAITER** - Table service, process payments
5. **KITCHEN** - Kitchen staff, prepare orders
6. **CUSTOMER** - Guest customer, place orders

---

## 📊 Dashboard Features

### Super Admin Dashboard
- View all restaurants
- Monitor system statistics
- Manage staff across system
- Generate reports

### Restaurant Owner Dashboard
- Real-time revenue tracking
- Order monitoring
- Staff management
- Menu configuration

### Kitchen Dashboard
- Real-time order updates
- Order preparation tracking
- Mark items ready

### Waiter Dashboard
- Ready orders for pickup
- Table management
- Payment processing
- Bill generation

---

## 🔒 Security Features

✅ Password hashing (PBKDF2)  
✅ CSRF protection  
✅ Session security  
✅ Login required on protected pages  
✅ Role-based access control  
✅ Restaurant data isolation  
✅ Permission checks  

---

## 📱 Features Ready to Use

✅ User authentication system  
✅ Restaurant management  
✅ Menu & category management  
✅ Staff management with roles  
✅ Table management with QR codes  
✅ Guest ordering system  
✅ Shopping cart functionality  
✅ Real-time order tracking  
✅ Kitchen dashboard  
✅ Waiter dashboard  
✅ Bill generation  
✅ Payment processing (Cash & Online)  
✅ Revenue reports  
✅ Order history reports  
✅ Staff performance reports  

---

## 🚀 Deployment (FREE Options Available)

### FREE Deployment Guide
📖 **See [DEPLOYMENT_GUIDE.md](./DEPLOYMENT_GUIDE.md) for FREE hosting options:**
- ✅ **Render.com** (Recommended) - Completely Free
- ✅ **Railway.app** - $5 free credit/month
- ✅ **Oracle Cloud** - Always Free tier
- ✅ **PythonAnywhere** - Free subdomain
- ✅ **Free Domain** - Freenom.com (.tk, .ml, .ga)

### Quick Deploy Steps
1. Push code to GitHub
2. Create Render account (render.com)
3. Connect GitHub repository
4. Add environment variables
5. Deploy (automatic)
6. Get free domain
7. Your app is LIVE! 🎉

**Total Cost: ₹0/month** ✅

### Before Going Live
- [ ] Change `DEBUG = False` in settings.py
- [ ] Update `ALLOWED_HOSTS` to your domain
- [ ] Change `SECRET_KEY` to a unique value
- [ ] Configure PostgreSQL (instead of SQLite)
- [ ] Set up email backend (SMTP)
- [ ] Configure Razorpay credentials
- [ ] Enable HTTPS/SSL
- [ ] Set up database backups
- [ ] Configure logging

---

## 🐛 Troubleshooting

### Server won't start
```bash
python manage.py check
python manage.py migrate
python manage.py runserver
```

### Database errors
```bash
del db.sqlite3
python manage.py migrate
```

### Missing dependencies
```bash
pip install -r requirements.txt
```

---

## 📞 Support

For issues or questions:
1. Check Django documentation: https://docs.djangoproject.com/
2. Review project code structure
3. Run `python manage.py check`
4. Check database with `python manage.py dbshell`

---

## 📄 License

See LICENSE file for details

---

## 👨‍💻 Developer

**Pawan Sharma**  
- GitHub: https://github.com/pawansharma-python
- LinkedIn: https://www.linkedin.com/in/pawansharma-python/
- Portfolio: https://pawansharma-python-portfolio.netlify.app/

---

## ⭐ Status

**Status:** ✅ Production Ready  
**Database:** SQLite (42+ migrations applied)  
**Views:** 30+ functional views  
**Templates:** 32 HTML templates  
**Features:** All implemented & tested  

---

**Last Updated:** August 8, 2026  
**Version:** 1.0  
**Status:** Ready for Deployment
