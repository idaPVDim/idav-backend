from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('L\'adresse email doit être renseignée')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Le superuser doit avoir is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Le superuser doit avoir is_superuser=True.')
        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    ROLE_CHOICES = (
        ('technicien', 'Technicien'),
        ('client', 'Client'),
        ('commercant', 'Commerçant'),
        ('admin', 'Admin'),
    )
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    telephone = models.CharField(max_length=20, blank=True, null=True)
    province = models.CharField(max_length=100, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    objects = CustomUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

class ProfilTechnicien(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    specialite = models.CharField(max_length=100, blank=True)
    certifications = models.TextField(blank=True)

class ProfilClient(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    adresse = models.TextField(blank=True)
    preferences_stockage = models.BooleanField(default=False)

class ProfilCommercant(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    nom_boutique = models.CharField(max_length=100)
    adresse_boutique = models.TextField()
