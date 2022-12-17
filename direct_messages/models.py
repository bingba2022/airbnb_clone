from django.db import models
from common.models import CommonModel

# Create your models here.


# 채팅방
class ChattingRoom(CommonModel):

    """Room Model Definition"""

    users = models.ManyToManyField(
        "users.User",
    )

    def __str__(self) -> str:
        return "Chatting Room"


# 메세지
class Message(CommonModel):

    """Message Model Definition"""

    text = models.TextField()
    user = models.ForeignKey(
        "users.User",
        # If we delete the user account, should we delete the message?
        null=True,
        blank=True,
        on_delete=models.SET_NULL,  # message is not going to be deleted but the user will be null
    )
    room = models.ForeignKey(
        "direct_messages.ChattingRoom",
        on_delete=models.CASCADE,
    )

    def __str__(self) -> str:
        return f"{self.user} says: {self.text}"
