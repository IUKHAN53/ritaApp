from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import UserManager
from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
User_auth = get_user_model()


class User(AbstractUser):
    objects = UserManager()
    email = models.EmailField(('email address'), unique=True)

    class Meta:
        verbose_name = ('user')
        verbose_name_plural = ('users')
        db_table = 'auth_user'
        swappable = 'AUTH_USER_MODEL'


class GoogleCred(models.Model):
    user = models.ForeignKey(User_auth, on_delete=models.CASCADE, null=True)
    google_email_phone = models.CharField(max_length=150, null=True)
    google_password = models.CharField(max_length=150, null=True)


class FacebookCred(models.Model):
    user = models.ForeignKey(User_auth, on_delete=models.CASCADE, null=True)
    facebook_email_phone = models.CharField(max_length=150, null=True)
    facebook_password = models.CharField(max_length=150, null=True)


class GoogleFile(models.Model):
    user = models.ForeignKey(User_auth, on_delete=models.CASCADE, null=True)
    path_to_google_data = models.CharField(max_length=150, null=True)
    availible_stat = models.BooleanField(default=False)


class FacebookFile(models.Model):
    user = models.ForeignKey(User_auth, on_delete=models.CASCADE, null=True)
    path_to_facebook_data = models.CharField(max_length=150, null=True)
    availible_stat = models.BooleanField(default=False)
    date_created = models.DateTimeField(default=timezone.now)
