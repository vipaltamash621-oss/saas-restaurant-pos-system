
from django.db import models
from django.conf import settings
import uuid




# 1. Restaurant Model
class Restaurant(models.Model):
    owner = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='owned_restaurant')
    name = models.CharField(max_length=100)
    
    # Contact Info
    address = models.TextField(blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    logo = models.CharField(max_length=500, blank=True, null=True, help_text="Image URL or path")
    
    # Settings (This was missing)
    is_active = models.BooleanField(default=True)
    
    # Geo Location
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    allowed_radius = models.IntegerField(default=50, help_text="Radius in meters")
    
    # Payment Settings (upi_id is removed)
    payment_qr = models.CharField(max_length=500, blank=True, null=True, help_text="QR Code image URL or path")
    # NEW: Dynamic QR ke liye UPI ID zaroori hai
    upi_id = models.CharField(max_length=50, blank=True, null=True, help_text="Ex: 9876543210@paytm or merchant@upi")
    razorpay_key_id = models.CharField(max_length=100, blank=True, null=True)
    razorpay_key_secret = models.CharField(max_length=100, blank=True, null=True)

    # QR Menu Slug
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = f"{self.name.replace(' ', '').lower()}-{str(uuid.uuid4())[:4]}"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

# ... (Keep the rest of your models: Category, MenuItem, Table, Order, etc.) ...


# 2. Categories
class Category(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='categories')
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=500, blank=True, null=True, help_text="Image URL or path")
    
    def __str__(self):
        return f"{self.name} ({self.restaurant.name})"


# 1. ADD-ON GROUP (e.g., "Choose Size", "Add Extra")
class AddOnGroup(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    name = models.CharField(max_length=100) # e.g. "Choice of Crust"
    is_required = models.BooleanField(default=False) # True = Customer must select one
    is_multiple = models.BooleanField(default=False) # True = Can select many (Checkbox), False = Only one (Radio)
    
    def __str__(self):
        return f"{self.name} ({self.restaurant.name})"

# 2. ADD-ON OPTIONS (e.g., "Cheese Burst", "Thin Crust")
class AddOnOption(models.Model):
    group = models.ForeignKey(AddOnGroup, on_delete=models.CASCADE, related_name='options')
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0) # Extra cost
    
    def __str__(self):
        return f"{self.name} (+₹{self.price})"
    



# 3. Menu Items
class MenuItem(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='items')
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.CharField(max_length=500, blank=True, null=True, help_text="Food image URL or path")
    addon_groups = models.ManyToManyField(AddOnGroup, blank=True, related_name='menu_items') 
    is_veg = models.BooleanField(default=True)
    is_available = models.BooleanField(default=True)
    
    # Ye field missing tha, isliye form error deta. Ab add kar diya h:
    preparation_time = models.PositiveIntegerField(default=15, help_text="Time in minutes") 
    
    def __str__(self):
        return self.name



# 4. Tables & QR Code Generation
class Table(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='tables')
    table_number = models.CharField(max_length=50)
    qr_code = models.CharField(max_length=500, blank=True, null=True, help_text="QR code image URL or path")
    unique_id = models.UUIDField(default=uuid.uuid4, editable=False)

    def save(self, *args, **kwargs):
        # QR code generation disabled temporarily (no Pillow)
        # Core POS functionality works without QR images
        super().save(*args, **kwargs)
        
    def __str__(self):
        return f"{self.restaurant.name} - Table {self.table_number}"


# 5. Orders
class Order(models.Model):
    STATUS_CHOICES = (
        ('RECEIVED', 'Received'),
        ('PREPARING', 'Preparing'),
        ('READY', 'Ready'),
        ('SERVED', 'Served'),
        ('PAID', 'Paid'),
    )
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='orders')
    table = models.ForeignKey(Table, on_delete=models.SET_NULL, null=True, blank=True)
    order_id = models.CharField(max_length=20, unique=True, editable=False)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='RECEIVED')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
     # --- YE DO LINE ADD KAREIN ---
    payment_status = models.BooleanField(default=False)  # Paid hai ya nahi
    payment_method = models.CharField(max_length=50, blank=True, null=True) # Cash/Online
    # --- NEW FIELDS FOR ONLINE PAYMENT HISTORY ---
    transaction_id = models.CharField(max_length=100, blank=True, null=True, help_text="UPI Ref ID / Txn ID")
    payer_name = models.CharField(max_length=100, blank=True, null=True, help_text="Paid by")
# --- NEW FIELD ---
    payment_proof = models.CharField(max_length=500, blank=True, null=True, help_text="Payment screenshot URL or path")
    

    updated_at = models.DateTimeField(auto_now=True) # Ye track karega ki order last kab update hua

    def save(self, *args, **kwargs):
        if not self.order_id:
            self.order_id = str(uuid.uuid4())[:8].upper()
        super().save(*args, **kwargs)



class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    food_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity_cooked = models.PositiveIntegerField(default=0)
    customizations = models.JSONField(default=dict, blank=True)
    is_prepared = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def qty_to_cook(self):
        return self.quantity - self.quantity_cooked


