from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    def _create_user(self, email,phone,location,full_name, password=None,password2=None,**extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email,
                          phone=phone,
                          location=location,
                          full_name=full_name,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email,phone,location,full_name, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email,phone,location,full_name, password,**extra_fields)

    def create_superuser(self, email, phone,location,full_name,password=None, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_admin', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email,phone,location,full_name, password,**extra_fields)

class Permission(models.Model):
    name=models.CharField(max_length=80)
class Features(models.Model):
    name=models.CharField(max_length=80)
    permission=models.ForeignKey(Permission,on_delete=models.CASCADE)
class Role(models.Model):
    name=models.CharField(max_length=50)
    permissions=models.ManyToManyField(Permission,blank=False)
class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    phone=models.IntegerField(null=False)
    location=models.CharField(max_length=200,null=False)
    full_name=models.CharField(max_length=150,null=False)
    role=models.ForeignKey(Role,on_delete=models.CASCADE,null=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    groups = models.ManyToManyField('auth.Group',
                                    related_name="users",
                                    blank=True,
                                    verbose_name='groups',
                                    help_text="uihubjbjhbjhbhnj  h hbujnjbn")

    user_permissions =models.ManyToManyField('auth.Permission',
                                    related_name="users",
                                    blank=True,
                                    verbose_name='user permission ',
                                    help_text="uihubjbjhbjhbhnj  h hbujnjbn")


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone','location','full_name']

    objects = CustomUserManager()

    def __str__(self):
        return self.full_name

