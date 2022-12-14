from django.db import models
from common.models import CommonModel


# Create your models here.


class Wishlist(CommonModel):
    """Wishlist Model Definition"""

    name = models.CharField(
        max_length=150,
    )
    rooms = models.ManyToManyField(  # wishlist can have many rooms -> many to many
        "rooms.Room",  # application.model
    )
    experiences = models.ManyToManyField(  # wishlist can have many experiences
        "experiences.Experience",
    )

    user = models.ForeignKey(  # one to many or many to one
        "users.User", on_delete=models.CASCADE  # wishlist is deleted when user deletes an account
    )

    def __str__(self) -> str:
        return self.name  # changes the name of wishlists to what we have set
