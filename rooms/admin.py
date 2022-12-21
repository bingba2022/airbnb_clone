from django.contrib import admin
from .models import Room, Amenity

# Register your models here.


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):

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
