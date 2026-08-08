# 🚀 RENDER ENVIRONMENT VARIABLES SETUP

## Environment Variables for Your SaaS Restaurant POS System

On Render.com dashboard, add these variables one by one:

---

## 📋 REQUIRED VARIABLES

### 1. SECRET_KEY
**NAME:** `SECRET_KEY`  
**VALUE:** Generate a secure key using this command:
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```
Or use this example (CHANGE THIS):
```
django-insecure-8jclnbfduf@&-4bvxiqb32=i%rqt-3e9#5bw+8==sk1)$arh4+
```

**Important:** Use a DIFFERENT key for production. Generate a new one.

---

### 2. DEBUG
**NAME:** `DEBUG`  
**VALUE:** `False`

This disables debug mode for production security.

---

### 3. ALLOWED_HOSTS
**NAME:** `ALLOWED_HOSTS`  
**VALUE:** `your-app-name.onrender.com,localhost,127.0.0.1`

Replace `your-app-name` with your actual Render app name.

Example:
```
saas-restaurant-pos-system.onrender.com,localhost,127.0.0.1
```

---

### 4. DATABASE_URL (For PostgreSQL on Render)
**NAME:** `DATABASE_URL`  
**VALUE:** Render provides this automatically

Render will create a free PostgreSQL database and set this automatically. If not set:

You'll see it in Render dashboard under "Internal Database URL"

---

## 📝 OPTIONAL VARIABLES

### Razorpay Payment (if using payments)
**NAME:** `RAZORPAY_KEY_ID`  
**VALUE:** Your Razorpay key

**NAME:** `RAZORPAY_KEY_SECRET`  
**VALUE:** Your Razorpay secret

---

## 🎯 STEP-BY-STEP RENDER SETUP

### Step 1: Go to Render Dashboard
- URL: https://render.com/dashboard

### Step 2: Create New Web Service
- Click "New +" button
- Select "Web Service"
- Connect your GitHub repo: `saas-restaurant-pos-system`

### Step 3: Configure Service
```
Name: saas-restaurant-pos-system
Environment: Python 3
Region: (Choose closest to you)
Branch: main
Build Command: pip install -r saas_pos/requirements.txt && cd saas_pos && python manage.py migrate
Start Command: cd saas_pos && python manage.py runserver 0.0.0.0:8000
```

### Step 4: Add Environment Variables
In Render dashboard, find "Environment" section:

#### Add each variable:
1. Click "Add Environment Variable"
2. Enter NAME and VALUE
3. Click "Add"
4. Repeat for each variable

---

## ✅ ENVIRONMENT VARIABLES TO ADD (In Order)

| # | NAME | VALUE |
|---|------|-------|
| 1 | SECRET_KEY | `django-insecure-XXXXXXXXXXXXXXXXXXXX` (generate new) |
| 2 | DEBUG | `False` |
| 3 | ALLOWED_HOSTS | `your-app.onrender.com,localhost` |
| 4 | PYTHONUNBUFFERED | `1` |

---

## 🔧 UPDATING settings.py (ALREADY DONE)

Your settings.py is configured to read from environment variables:

```python
import os

SECRET_KEY = os.getenv('SECRET_KEY', 'django-insecure-...')
DEBUG = os.getenv('DEBUG', 'False') == 'True'
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '*').split(',')
```

**No changes needed - environment variables will be automatically picked up!**

---

## 🚀 QUICK CHECKLIST

Before clicking "Deploy":

- [ ] App name: `saas-restaurant-pos-system`
- [ ] Environment: Python 3
- [ ] Branch: main
- [ ] Build command added
- [ ] Start command added
- [ ] SECRET_KEY added
- [ ] DEBUG = False added
- [ ] ALLOWED_HOSTS added
- [ ] Free PostgreSQL selected (if available)

---

## ✅ AFTER DEPLOYMENT

Once deployed, your app will:
1. Install dependencies
2. Run migrations (DATABASE_URL will be set)
3. Start the Django server
4. Be accessible at: `https://saas-restaurant-pos-system.onrender.com`

---

## 🔐 SECURITY NOTES

✅ DO:
- Use strong SECRET_KEY
- Set DEBUG=False
- Use HTTPS (automatic on Render)
- Keep API keys in environment variables

❌ DON'T:
- Commit SECRET_KEY to GitHub
- Set DEBUG=True in production
- Share environment variables
- Use test API keys

---

## 💡 TROUBLESHOOTING

### Error: "SECRET_KEY not found"
→ Add SECRET_KEY environment variable

### Error: "ALLOWED_HOSTS error"
→ Check your app URL and add it to ALLOWED_HOSTS

### Database connection error
→ Render's DATABASE_URL should be automatic

### Static files not loading
→ Run: `python manage.py collectstatic --noinput`

---

## 📱 LOGIN AFTER DEPLOYMENT

Default admin login:
```
Username: admin
Password: admin123
```

Change these in production!

---

## 🎯 YOUR FINAL APP URL

After deployment:
```
https://saas-restaurant-pos-system.onrender.com/
```

---

## 📚 ADDITIONAL RESOURCES

- Render Docs: https://render.com/docs
- Django Docs: https://docs.djangoproject.com
- Environment Variables: https://render.com/docs/environment-variables

---

**Ready to deploy? Click "Create Web Service" on Render!** 🚀
