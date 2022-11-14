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
