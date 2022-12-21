from django.db import models
from common.models import CommonModel

# Create your models here.


class Review(CommonModel):

    """Review from a User to a Room or Experience"""

    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="reviews",
    )

    room = models.ForeignKey(
        "rooms.Room",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="reviews",
    )

    experience = models.ForeignKey(
        "experiences.Experience",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="reviews",
    )
    # Even the user is deleted, maybe the reviews might still stays on a room or an experience

    payload = models.TextField()
    rating = models.PositiveBigIntegerField()

    def __str__(self) -> str:
        return f"{self.user} / {self.rating}⭐"
