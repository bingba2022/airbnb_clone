from rest_framework import serializers
from .models import Category


class CategorySerializer(serializers.Serializer):
    # field that we want to expose about our categories
    # explaining to the serializer how should the name and kind should be represented when we turn then into json
    pk = serializers.IntegerField(read_only=True)
    name = serializers.CharField(
        required=True,
        max_length=50,
    )
    kind = serializers.ChoiceField(
        choices=Category.CategoryKindChoices.choices,
    )
    created_at = serializers.DateTimeField(read_only=True)

    # create method has to return an object
    def create(self, validated_data):
        return Category.objects.create(**validated_data)
        # ** will take the dictionary and furn it into this
        # name = validated_data['name'] automatically

    def update(
        self, instance, validated_data
    ):  # instance: category (database data) # validated_data: data from user
        # updating with the data that user has given but if the user didn't send the data then leave it as it was (instance.name/instance.kind)
        instance.name = validated_data.get("name", instance.name)
        instance.kind = validated_data.get("kind", instance.kind)
        instance.save()
        return instance
