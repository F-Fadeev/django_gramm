from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    is_email_confirmed = models.BooleanField(default=False)
    middle_name = models.CharField(max_length=255, blank=True, null=True)
    date_of_birth = models.DateTimeField(blank=True, null=True)
    avatar = models.ImageField(upload_to='avatars', blank=True, null=True)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['id']

    def __str__(self):
        return f'User(username={self.get_username()}, email={self.email})'
