from django.db import models
from common.models import CommonModel

# Create your models here.
class Room(CommonModel):
    class RoomKindChoices(models.TextChoices):
        ENTIRE_PLACE = "entire_place", "Entire Place"
        PRIVATE_ROOM = "private_room", "Private Room"
        SHARED_ROOM = "shared_room", "Shared Room"

    """Room Model Definition"""

    name = models.CharField(
        max_length=180,
        default="",
    )
    country = models.CharField(
        max_length=50,
        default="한국",
    )
    city = models.CharField(
        max_length=80,
        default="서울",
    )
    price = models.PositiveIntegerField()
    rooms = models.PositiveBigIntegerField()
    toilets = models.PositiveBigIntegerField()
    description = models.TextField()
    address = models.CharField(
        max_length=250,
    )
    pet_friendly = models.BooleanField(
        default=True,
    )
    kind = models.CharField(
        max_length=20,
        choices=RoomKindChoices.choices,
    )
    owner = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="rooms",
    )

    amenities = models.ManyToManyField(
        "rooms.Amenity",
        related_name="rooms",
    )

    category = models.ForeignKey(
        "categories.Category",
        null=True,
        blank=True,
        # SET_NULL: make the category of experience 'NULL' if the categories in Category application is deleted
        # CASCADE: delete the experience if the category is deleted
        on_delete=models.SET_NULL,
        related_name="rooms",
    )

    def __str__(self) -> str:
        return self.name

    # auto_now_add : sets the filed to now when the object is first CREATED
    # auto_now : sets the filed to now when the object is SAVED


# Many To One : [Room1, Room2, Room3] => User1
# One To Many : User1 => [Room1, Room2, Room3]
# Many To Many : [Amenity1, Amenity2, Amenity3] => [Room1, Room2, Room3]


class Amenity(CommonModel):
    """Amenity Definition"""

    name = models.CharField(max_length=150)
    description = models.CharField(
        max_length=150,
        null=True,
        blank=True,
    )

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = "Amenities"
