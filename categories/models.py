from django.db import models
from common.models import CommonModel

# Create your models here.


class Category(CommonModel):

    """Room or Experience Category"""

    class CategoryKindChoices(models.TextChoices):
        ROOMS = ("rooms", "Rooms")
        EXPERIENCES = "experiences", "Experiences"

    name = models.CharField(
        max_length=50,
    )

    kind = models.CharField(
        max_length=15,
        choices=CategoryKindChoices.choices,
    )

    def __str__(self) -> str:
        # 이렇게 하면 카테고리 고를때 rooms 인지 experience 인지 admin 패널에서 안 헷갈림
        return f"{self.kind}: {self.name}"

    class Meta:
        verbose_name_plural = "Categories"
