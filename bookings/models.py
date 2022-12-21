from django.db import models
from common.models import CommonModel

# Create your models here.

# one booking model for rooms and experiences
class Booking(CommonModel):

    """Booking Model Definition"""

    class BookingKindChoices(models.TextChoices):
        ROOM = "room", "Room"
        EXPERIENCE = "experience", "Experience"

    kind = models.CharField(
        max_length=15,
        choices=BookingKindChoices.choices,
    )

    # one user can have many bookings but A booking can have one user
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="bookings",
    )
    # one room can have many bookings but A booking can have one room
    room = models.ForeignKey(
        "rooms.Room",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,  # we still want to keep the record
        related_name="bookings",
    )

    # same as room
    experience = models.ForeignKey(
        "experiences.Experience",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,  # we still want to keep the record
        related_name="bookings",
    )

    check_in = models.DateField(
        null=True,
        blank=True,
    )

    check_out = models.DateField(
        null=True,
        blank=True,
    )

    experience_time = models.DateTimeField(
        null=True,
        blank=True,
    )

    guests = models.PositiveBigIntegerField()

    def __str__(self) -> str:
        return f"{self.kind.title()} booking for: {self.user}"
