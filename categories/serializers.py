from rest_framework import serializers


class CategorySerializer(serializers.Serializer):
    # field that we want to expose about our categories
    # explaining to the serializer how should the name and kind should be represented when we turn then into json
    pk = serializers.IntegerField(read_only=True)
    name = serializers.CharField(
        required=True,
        max_length=50,
    )
    kind = serializers.CharField(
        max_length=15,
    )
    created_at = serializers.DateTimeField(read_only=True)
