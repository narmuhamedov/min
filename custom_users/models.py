from django.contrib.auth.models import User
from django.db import models


class CustomUser(User):
    class Meta:
        verbose_name = 'type_user'
        verbose_name_plural = 'type_users'

    ADMIN = 1
    VIPClient = 2
    CLIENT = 3

    USER_TYPE = (
        (ADMIN, "ADMIN"),
        (VIPClient, "VIPClient"),
        (CLIENT, "CLIENT")
    )

    MALE = 1
    FEMALE = 2
    OTHER = 3

    GENDER_TYPE = (
        (MALE, "MALE"),
        (FEMALE, "FEMALE"),
        (OTHER, "OTHER")
    )

    user_type = models.IntegerField(choices=USER_TYPE, verbose_name='type_user', default=CLIENT)
    phone_number = models.CharField('phone_number', max_length=50)
    age = models.IntegerField()
    gender = models.IntegerField(choices=GENDER_TYPE, verbose_name='gender')

    def __str__(self):
        return self.USER_TYPE
