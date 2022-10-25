from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from . import models
from django import forms

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


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(required=True, max_length=100)
    age = forms.IntegerField(required=True)
    user_type = forms.ChoiceField(choices=USER_TYPE, required=True)
    gender = forms.ChoiceField(choices=GENDER_TYPE, required=True)

    class Meta:
        model = models.CustomUser
        fields = (
            "username",
            "email",
            "password1",
            "password2",
            "first_name",
            "last_name",
            "age",
            "user_type",
            "gender"
        )







