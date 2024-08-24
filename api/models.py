from django.db import models
from decimal import Decimal
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    amount = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    win_game = models.BooleanField()
    email = models.EmailField(unique=True)