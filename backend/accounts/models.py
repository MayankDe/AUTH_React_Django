# from typing import Any
# from django.db import models
# from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager


# # Create your models here.
# class UserAccountManager(BaseUserManager):
#     def create_user(self, email,password=None,**extra_fields):
#         if not email:
#             raise ValueError('user must have an email address')
#         email = self.normalize_email(email)
#         user = self.model(email=email,**extra_fields)

      
#         user.first_name = extra_fields.get('first_name')
#         user.last_name = extra_fields.get('last_name')

#         user.set_password(password)
#         user.save(using=self._db)
        
#         return user
#     def create_superuser(self, email,first_name,last_name, password=None):
#         user = self.create_user(email,first_name,last_name, password)
#         user.is_staff = True
#         user.is_superuser = True
#         user.save(using=self._db)
#         return user

# class UserAccount(AbstractBaseUser,PermissionsMixin):
#     email = models.EmailField(max_length=255,unique=True)
#     first_name  = models.CharField(max_length=255,null=True, blank=True)
#     last_name  = models.CharField(max_length=255,null=True,blank=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)

#     objects = UserAccountManager()
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ["first_name","last_name"]
  


#     def get_full_name(self):
#         return self.first_name +' '+self.last_name
    
#     def get_short_name(self):
#         return self.first_name 
    
#     def __str__(self):
#         return self.email


from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class UserAccountManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('User must have an email address')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)

        user.first_name = extra_fields.get('first_name', '')
        user.last_name = extra_fields.get('last_name', '')

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, first_name, last_name, password=None):
        # Pass only the necessary arguments to create_user
        user = self.create_user(email, password, first_name=first_name, last_name=last_name)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class UserAccount(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserAccountManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_short_name(self):
        return self.first_name

    def __str__(self):
        return self.email
