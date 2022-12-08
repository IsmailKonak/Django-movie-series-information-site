from codecs import backslashreplace_errors
from re import T
from django.utils.timezone import now
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class CustomAccountManager(BaseUserManager):

    def create_superuser(self, email, fname, lname, username, password, **other_fields):
        other_fields.setdefault("is_staff",True)
        other_fields.setdefault("is_superuser",True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                "Superuser must be assigned to is_staff = True"
            )
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                "Superuser must be assigned to is_superuser = True"
            )

        return self.create_user(email, fname, lname, username, password, **other_fields)

    
    def create_user(self, email, fname, lname, username, password, **other_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, fname=fname,lname=lname, username=username, **other_fields)
        user.set_password(password)
        user.save()
        return user


class NewUser(AbstractBaseUser, PermissionsMixin):
    #Required
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=75)
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True,max_length=100)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    #Optional
    profile_pic = models.ImageField(null=True, blank=True, upload_to="users/")
    birthday = models.DateField(null=True,blank=True)
    join_date = models.DateField(default=now)
    instagram = models.CharField(max_length=100, null=True, blank=True)
    twitter = models.CharField(max_length=100, null=True, blank=True)
    facebook = models.CharField(max_length=100, null=True, blank=True)
    

    objects= CustomAccountManager()

    USERNAME_FIELD = "username"
    
    REQUIRED_FIELDS= ["email","fname","lname"]

    def get_fullname(self):
        return self.fname+" "+self.lname

    def __str__(self):
        return self.username
    
