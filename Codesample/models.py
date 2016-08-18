from __future__ import unicode_literals

from django.db import models
from django import forms
# # Create your models here.
# class Sample():
#
import time
from datetime import datetime
from django.contrib.auth.models import User, AbstractBaseUser, BaseUserManager, PermissionsMixin, UserManager
from django.utils import timezone
from django.core.mail import send_mail

class UserModel(AbstractBaseUser,PermissionsMixin):
    first_name = models.CharField(max_length=15,default='')
    last_name = models.CharField(max_length=20, default='')
    username = models.CharField(max_length=20,)
    email = models.EmailField(max_length=30,unique=True)
    # password = models.CharField(max_length=20)
    city_town=models.CharField(max_length=20)
    mobile=models.CharField(max_length=10)
    dp=models.FileField(upload_to='dps/%Y%m%d')
    USERNAME_FIELD='email'
    REQUIRED_FIELDS = ['username']
    is_staff = models.BooleanField(('staff status'), default=False, help_text=(
            'Designates whether the user can log into this admin site.'))
    is_active = models.BooleanField(('active'), default=True, help_text=(
        'Designates whether this user should be treated as '
        'active. Unselect this instead of deleting accounts.'))
    date_joined = models.DateTimeField(('date joined'), default=timezone.now)
    is_admin = models.BooleanField(default=False)

    def get_username(self):
        return self.email





    objects=UserManager()

    def __str__(self):
        return self.email

    def get_full_name(self):
        """Return the email."""
        return self.email

    def get_short_name(self):
        """Return the email."""
        return self.email

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this User."""
        send_mail(subject, message, from_email, [self.email], **kwargs)



        # class CodePost(models.Model):
#     title = models.CharField(max_length=20,)
#     text = models.CharField(max_length=1000)
#     postid=models.ForeignKey(User,on_delete=models.CASCADE,default='')
#     def __str__(self):
#         return self.title

    # def save(self):
    # #     self.save()
    # def __str__(self):
    #     return self.title
    #
    # title = forms.CharField(max_length=20, label='title', widget=forms.TextInput)
    # text = forms.CharField(label='code', widget=forms.Textarea)
    #
    # def __str__(self):
    #     return self.title



class Fotos(models.Model):
    name=models.CharField(max_length=20,default=time.strftime("%Y%m%d_%H%M%S"))
    author=models.ForeignKey(UserModel,on_delete=models.CASCADE)
    date=models.DateTimeField(default=datetime.now())
    likes=models.IntegerField(default=0)
    comments=models.CharField(max_length=200,default='')
    shares=models.IntegerField(default=0)
    foto = models.FileField(upload_to='posts/fotos/%Y/%m/%d')

    def __str__(self):
        return self.name





