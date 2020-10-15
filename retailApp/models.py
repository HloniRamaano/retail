from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

class Product(models.Model):
    name = models.CharField(max_length = 200)
    image = models.ImageField(upload_to='product', null=True, blank=True, verbose_name='image')
    price = models.FloatField()
    description = models.TextField()
    category = models.CharField(max_length = 200)

    def __str__(self):
        return self.name

class ShoppingCart(models.Model):
    product_id = models.CharField(max_length=100)
    name = models.CharField(max_length = 200)
    price = models.FloatField()
    quantity = models.IntegerField()

    def __str__(self):
        return self.name

class Payment(models.Model):
    
    name = models.CharField(max_length = 200)
    bank_name = models.CharField(max_length = 200)	#First National Bank (FNB)
    account_name = models.CharField(max_length = 200)	#Unisa Student Fees Account
    account_number = models.CharField(max_length = 200)	#627 9963 0382
    account_type = models.CharField(max_length = 200)	#Cheque
    branch_code = models.CharField(max_length = 200)	#210554
    reference = models.CharField(max_length = 200)
    amount = models.FloatField()

    def __str__(self):
        return self.reference
    
#Account Model
class MyAccountManager(BaseUserManager):
    def create_user(self, firstname, lastname, email, username, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have a username')
        if not firstname:
            raise ValueError('Users must have a firstname')
        if not username:
            raise ValueError('Users must have a lastname')
        user = self.model(
            email=self.normalize_email(email),
            username=username,
            firstname=firstname,
            lastname=lastname,
            )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email,firstname,lastname, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username,
            firstname = firstname,
            lastname = lastname,
            )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
class Account(AbstractUser):
    firstname               = models.CharField(max_length=30, unique=True)
    lastname                = models.CharField(max_length=30, unique=True)
    email 					= models.EmailField(verbose_name="email", max_length=60, unique=True)
    username 				= models.CharField(max_length=30, unique=True)
    date_joined				= models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login				= models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin				= models.BooleanField(default=False)
    is_active				= models.BooleanField(default=True)
    is_staff				= models.BooleanField(default=False)
    is_superuser			= models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['firstname','lastname','username']
    
    objects = MyAccountManager()
    def _str_(self):
        return self.firstname + ' ' + self.lastname
    
    # For checking permissions. to keep it simple all admin have ALL permissons
    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    # Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)
    def has_module_perms(self, app_label):
        return True
