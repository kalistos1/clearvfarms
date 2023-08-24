from django.contrib.auth.models import AbstractUser

from django.db import models
from django_tenants.models import TenantMixin, DomainMixin
from guardian.mixins import GuardianUserMixin
from client.models import Client

# Custom User Model
class User(AbstractUser, GuardianUserMixin):
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True)
    # Add additional fields for your user model

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_short_name(self):
        return self.username

# Tenant User Model (Linking user to tenant with roles)
class TenantUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tenant = models.ForeignKey(Client, on_delete=models.CASCADE)
    
    ROLE_CHOICES = (
        ('farm_worker', 'Farm Worker'),
        ('agronomist', 'Agronomist'),
        ('harvester', 'Harvester'),
        ('tractor_operator', 'Tractor Operator'),
        ('irrigation_specialist', 'Irrigation Specialist'),
        ('livestock_manager', 'Livestock Manager'),
        ('veterinarian', 'Veterinarian'),
    )
    role = models.CharField(max_length=50, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.user.username} - {self.get_role_display()} at {self.tenant.name}"

# Buyer User Model (For buyers not linked to tenants)
class BuyerUser(User):
    organization = models.CharField(max_length=100)
    # Additional fields for buyers

# System User Model (For platform management)
class SystemUser(User):
    is_administrator = models.BooleanField(default=False)
    # Additional fields for system users

# Farm Advisory User Model
class FarmAdvisoryUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    expertise = models.TextField()
    # Additional fields specific to farm advisory users

    def __str__(self):
        return f"{self.user.username} - Farm Advisory"

