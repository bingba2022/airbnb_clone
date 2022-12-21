from django.contrib import admin
from .models import Review

# Register your models here.


class WordFilter(admin.SimpleListFilter):
    title = "Filter by words!"
    parameter_name = "word"

    def lookups(self, request, model_admin):
        return [
            ("good", "Good"),
            ("great", "Great"),
            ("awesome", "Awesome"),
        ]

    def queryset(self, request, reviews):
        word = self.value()
        if word:
            return reviews.filter(payload__contains=word)
        else:
            reviews


class RatingFilter(admin.SimpleListFilter):
    title = "Filter by ratings!"
    parameter_name = "Rating"

    def lookups(self, request, model_admin):
        return [
            ("good", "Good"),
            ("bad", "Bad"),
        ]

    def queryset(self, request, reviews):
        rating = request.GET.get("Rating")
        if rating == "good":
            return reviews.filter(rating__gte=3)
        elif rating == "bad":
            return reviews.filter(rating__lt=3)
        else:
            reviews


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        "__str__",
        "room",
        "experience",
        "payload",
    )

    list_filter = (
        WordFilter,
        RatingFilter,
        "rating",
        "user__is_host",  # filtering a review based on a foreign key
        "room__category",
        "room__pet_friendly",
    )
