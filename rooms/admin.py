from django.contrib import admin
from .models import Room, Amenity

# Register your models here.


@admin.action(description="Set all prices to zero")
def reset_prices(model_admin, request, rooms):
    # model_admin: model that has the action
    # request: has information about who is calling this action
    # queryset: list of all the object that I selected

    for room in rooms.all():
        room.price = 0
        room.save()


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    actions = (reset_prices,)
    # filter list:
    list_display = (
        "name",
        "price",
        "kind",
        "total_amenities",
        "rating",
        "rooms",
        "toilets",
        "owner",
    )

    # filter by:
    list_filter = (
        "country",
        "city",
        "price",
        "rooms",
        "toilets",
        "pet_friendly",
        "kind",
    )

    search_fields = (
        # ^ : starts with
        # = : exact
        "name",
        "price",
        "=owner__username",  # search by owner's username
    )


@admin.register(Amenity)
class AmenityAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "description",
        "created_at",
        "updated_at",
    )

    list_filter = (
        "created_at",
        "updated_at",
    )

    # put this to show it on editing page (not just list page)
    readonly_fields = (
        "created_at",
        "updated_at",
    )
