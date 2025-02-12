from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

from config import settings


class CustomUserManager(BaseUserManager):
    def create_user(self, phone, password=None, **extra_fields):
        if not phone:
            raise ValueError('The Phone field must be set')
        user = self.model(phone=phone, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(phone, password, **extra_fields)

class CustomUser(AbstractUser):
    username = None  # username maydonini o‘chirib tashlaymiz
    phone = models.CharField(max_length=15, unique=True)
    name = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    full_name = models.CharField(max_length=255, blank=True, null=True)

    USERNAME_FIELD = 'phone'  # username o‘rniga telefon raqamini ishlatamiz
    REQUIRED_FIELDS = ['name', 'lastname']  # 'name' va 'lastname' talab qilinadi

    objects = CustomUserManager()

    def __str__(self):
        return f"{self.name} {self.lastname}"  # 'full_name' ni birlashtirib ko'rsatish

    def save(self, *args, **kwargs):
        self.full_name = f"{self.name} {self.lastname}"  # full_name maydonini birlashtiramiz
        super().save(*args, **kwargs)


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)  # Profilga qo'shimcha maydonlar qo'shish mumkin
    birth_date = models.DateField(blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.user.full_name} Profile"