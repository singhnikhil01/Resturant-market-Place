from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, first_name, last_name, username, email, password):
        if not email:
            raise ValueError('User must have an email address')
        if not username:
            raise ValueError('User must have a username')
        
        user = self.model(
            first_name=first_name,
            last_name=last_name,
            email=self.normalize_email(email),
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, last_name, username, email, password=None):
        user = self.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    RESTAURANT = 1
    CUSTOMER = 2
    
    ROLE_CHOICES = (
        (RESTAURANT, 'Restaurant'),
        (CUSTOMER, 'Customer'),
    )
    
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    phone_number = models.CharField(max_length=12, blank=True)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, null=True)
    
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    
    objects = UserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'username']
    
    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, app_label):
        return True

class UserProfie(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,blank=True,null=True) # one user can have one profile
    profile_picture = models.ImageField(upload_to='users/profile_picture',blank=True,null=True) #
    cover_picture = models.ImageField(upload_to='users/cover_picture',blank=True,null=True)
    address_line_1 = models.CharField(max_length=100, blank=True,null=True)
    country = models.CharField(max_length=15, blank=True,null=True)
    city = models.CharField(max_length=15, blank=True,null=True)
    pin_code = models.CharField(max_length=6, blank=True,null=True)
    latitude = models.CharField(max_length=50,blank=True,null=True)
    longitude = models.CharField(max_length=50,blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.user.email)
