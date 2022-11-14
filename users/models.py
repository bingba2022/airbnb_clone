from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

# Class User inherits from AbstractUser
class User(AbstractUser):
    class GenderChoices(models.TextChoices):
        # (Value, Label)
        MALE = ("male", "Male")
        FEMALE = ("female", "Female")

    class LanguageChoices(models.TextChoices):
        KR = ("kr", "Korean")
        EN = ("en", "English")

    class CurrencyChoices(models.TextChoices):
        # 튜플 만들때 괄호 안 해도 상관 없음
        WON = "won", "Korean Won"
        USD = "usd", "Dollar"

    # # 원래 있는 first name, last name은 make it uneditable
    first_name = models.CharField(max_length=150, editable=False)
    last_name = models.CharField(max_length=150, editable=False)

    # profile phoeo
    # blank = True : allows field to not be required on the form
    # null = True : field to be 'null' on the db layer
    avatar = models.ImageField(blank=True)

    # 새로 만들 이름 필드
    name = models.CharField(max_length=150, default="")
    # Non-nullable fields 2 options : 1. default = False, 2. null = True
    is_host = models.BooleanField(default=False)
    gender = models.CharField(
        max_length=10,
        choices=GenderChoices.choices,
    )
    language = models.CharField(
        max_length=2,
        choices=LanguageChoices.choices,
    )
    currency = models.CharField(
        max_length=5,
        choices=CurrencyChoices.choices,
    )
