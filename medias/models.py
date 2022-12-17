from django.db import models
from common.models import CommonModel

# Create your models here.


class Photo(CommonModel):
    file = models.ImageField()
    description = models.CharField(
        max_length=140,
    )
    # one room can have many photos but
    # the photo can only belong to one room
    room = models.ForeignKey(
        "rooms.Room",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    experience = models.ForeignKey(
        "experiences.Experience",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    def __str__(self) -> str:
        return "Photo File"


class Video(CommonModel):
    file = models.FileField()
    experience = models.OneToOneField(
        "experiences.Experience",
        on_delete=models.CASCADE,
    )
    # Foreign Key VS OneToOneField
    # Foreign Key: Can create many photos and all those photos belongs to a same room
    # OneToOneField: Video can belong to one experience and NO OTHER video can belong to this same experience

    def __str__(self) -> str:
        return "Video File"
