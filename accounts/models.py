from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.crypto import get_random_string

from shipping.models import Country

# Create your models here.


def new_email_token():
    return get_random_string(40)


class UserProfile(AbstractUser):
    email_token = models.CharField(max_length=40, unique=True, default=new_email_token)
    email_confirmed = models.BooleanField(default=False)
    country = models.ForeignKey(Country, verbose_name='Страна', default=Country.default_country_id, blank=True)
    address = models.TextField(verbose_name='Адрес', blank=True)
    phone = models.CharField(verbose_name='Телефон', max_length=255, blank=True)
    middle_name = models.CharField(verbose_name='Отчество', max_length=255, blank=True)


class UsernameAddition(models.Model):
    name = models.CharField(max_length=15, unique=True)

    LEFT = 0
    RIGHT = 1
    LEFT_RIGHT = 2
    POSITION_CHOICES = (
        (LEFT, 'Слева'),
        (RIGHT, 'Справа'),
        (LEFT_RIGHT, 'Слева или справа')
    )
    position = models.IntegerField(choices=POSITION_CHOICES)

    def __str__(self):
        return self.name
