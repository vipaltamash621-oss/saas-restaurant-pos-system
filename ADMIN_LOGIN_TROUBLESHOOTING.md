# 🔐 ADMIN LOGIN TROUBLESHOOTING

## Problem: "Invalid username or password"

Your app deployed successfully but login is not working. Here's how to fix it:

---

## 🔧 Solution 1: Redeploy with New Build (RECOMMENDED)

1. Go to Render Dashboard → Your Service
2. Click "Manual Deploy" → "Deploy latest commit"
3. Wait 5-10 minutes for deployment
4. Check logs for: ✅ "Successfully created superuser"
5. Try login: `admin` / `admin123`

The new custom management command should create the admin user automatically.

---

## 🔧 Solution 2: Use Render Shell to Create Admin Manually

If redeploy still doesn't work:

1. Go to Render Dashboard → Your Service
2. Click "Shell" tab
3. Run this command:

```bash
cd saas_pos && python manage.py create_admin
```

4. You should see: ✅ "Successfully created superuser: admin / admin123"
5. Now try login

---

## 🔧 Solution 3: Direct Database Command

In Render Shell, run:

```bash
cd saas_pos && python manage.py shell
```

Then paste:

```python
from django.contrib.auth import get_user_model
User = get_user_model()
User.objects.filter(username='admin').delete()
User.objects.create_superuser('admin', 'admin@example.com', 'admin123', role='SUPERADMIN')
print('Admin user created!')
exit()
```

---

## 📋 Login Details

**After admin user is created:**

- **URL:** `https://saas-restaurant-pos-system.onrender.com/admin/`
- **Username:** `admin`
- **Password:** `admin123`

---

## ✅ Verification Steps

1. Go to admin URL
2. Enter username: `admin`
3. Enter password: `admin123`
4. Click "Sign In"
5. You should see Django Admin Dashboard

---

## 🎯 If Still Not Working

Check Render logs for errors:

1. Render Dashboard → Your Service → Logs
2. Look for errors related to:
   - Database connection issues
   - Migration failures
   - User creation errors
3. Share error messages if needed

---

## 💡 Alternative: Create User Through Admin Form

If admin login still fails, check if there's a registration form:

- Try: `https://saas-restaurant-pos-system.onrender.com/register/`
- Or: `https://saas-restaurant-pos-system.onrender.com/signup/`

---

## 🚀 Quick Summary

**New automated process:**
1. Deployed → Redeploy triggered
2. build.sh runs → Migrations applied
3. Management command runs → Admin created
4. Login works! ✅

**All changes pushed to GitHub. Redeploy now!**
