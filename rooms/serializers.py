from rest_framework.serializers import ModelSerializer
from .models import Amenity, Room
from users.serializers import TinyUserSerializer
from categories.serializers import CategorySerializer


class RoomListSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = (
            "pk",
            "name",
            "country",
            "city",
            "price",
        )


class AmenitySerializer(ModelSerializer):
    class Meta:
        model = Amenity
        fields = (
            "name",
            "description",
        )


class RoomDetailSerializer(ModelSerializer):

    owner = TinyUserSerializer(read_only=True)
    amenities = AmenitySerializer(
        read_only=True,
        many=True,
    )  # only use many=True if it is an array
    category = CategorySerializer(
        read_only=True,
    )  # Room model 이랑 이름 맞는지 확인

    class Meta:
        model = Room
        fields = "__all__"
        depth = 1

    def create(self, validated_data):
        return Room.objects.create(**validated_data)
