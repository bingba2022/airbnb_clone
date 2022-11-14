from django.db import models
from common.models import CommonModel

# Create your models here.


class Experience(CommonModel):

    """Experience Model Definition"""

    country = models.CharField(
        max_length=50,
        default="대한민국",
    )

    city = models.CharField(
        max_length=80,
        default="서울",
    )

    name = models.CharField(
        max_length=250,
    )

    host = models.ForeignKey(
        "users.User",
        # when the user deletes their account, it deletes the experience as well
        on_delete=models.CASCADE,
    )

    price = models.PositiveBigIntegerField()

    address = models.CharField(
        max_length=250,
    )

    # DateField: saves Day/Month/Year
    # TimeField: saves Hour/Min/Sec
    # DateTimeField: saves Day/Month/Year/Hour/Min/Sec
    start = models.TimeField()
    end = models.TimeField()

    description = models.TextField()

    perks = models.ManyToManyField(
        "experiences.Perk",
    )

    category = models.ForeignKey(
        "categories.Category",
        null=True,
        blank=True,
        # SET_NULL: make the category of experience 'NULL' if the categories in Category application is deleted
        # CASCADE: delete the experience if the category is deleted
        on_delete=models.SET_NULL,
    )

    def __str__(self) -> str:
        return self.name


class Perk(CommonModel):

    """What is included on an Experience"""

    name = models.CharField(
        max_length=100,
    )
    details = models.CharField(
        max_length=250,
        blank=True,
        null=True,  # act same as default = ""
    )
    explanation = models.TextField(
        blank=True,
        null=True,
    )

    def __str__(self) -> str:
        return self.name
