from django.db import models
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
import binascii
import os
from django.utils import timezone

# Create your models here.


class UserModel(models.Model):
    username = models.CharField(verbose_name="نام کاربری", max_length=50)
    email = models.EmailField(verbose_name="ایمیل", max_length=254)
    password = models.CharField(
        max_length=20, verbose_name="رمز", blank=False, null=False
    )
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "کاربر"
        verbose_name_plural = "کاربران"

    def __str__(self):
        return self.username


@receiver(post_save, sender=UserModel)
def create_auth_token(sender, instance=UserModel, created=False, **kwargs):
    if created:
        MyOwnToken.objects.create(userTokens=instance)


class MyOwnToken(models.Model):
    key = models.CharField(("Key"), max_length=40, primary_key=True)

    userTokens = models.OneToOneField(
        UserModel,
        related_name="auth_token",
        on_delete=models.CASCADE,
        verbose_name="user_token",
    )
    created = models.DateTimeField(("Created"), auto_now_add=True)

    class Meta:
        verbose_name = "userToken"
        verbose_name_plural = "userTokens"

    def save(self, *args, **kwargs):
        if not self.key:
            self.key = self.generate_key()
        return super(MyOwnToken, self).save(*args, **kwargs)

    def generate_key(self):
        return binascii.hexlify(os.urandom(20)).decode()

    def __str__(self):
        return self.key

    class Meta:
        verbose_name = "Users Token"
        verbose_name_plural = "User Token"
