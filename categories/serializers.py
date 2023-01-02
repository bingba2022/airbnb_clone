from rest_framework import serializers
from .models import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            # 1. 하나씩 지정해도 되고
            "name",
            "kind",
            # 2. 전체를 지정해도 되고
            # "__all__"
        )

        # 3. Exclude 를 사용해도 됨
        # exclude = (
        #     "name",
        #     "kind"
        # )
