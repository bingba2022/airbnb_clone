from django.shortcuts import render
from .models import Category
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CategorySerializer
from rest_framework.exceptions import NotFound
from rest_framework.status import HTTP_204_NO_CONTENT

# from django.core import serializers
# from django.http import JsonResponse


# Create your views here.

# /category
@api_view(["GET", "POST"])
def categories(request):

    if request.method == "GET":
        all_categories = Category.objects.all()
        serializer = CategorySerializer(all_categories, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        # giving data that user sent to serializer
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            new_category = serializer.save()
            CategorySerializer(new_category).data
            return Response({"created": True})
        else:
            return Response(serializer.errors)


# /category/[category_id]
@api_view(["GET", "PUT", "DELETE"])
def category(request, pk):
    try:  # 1. get the category
        category = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        raise NotFound  # raise 밑에 있는 코드를 다 죽임 (실행 x)

    if request.method == "GET":  # if the user wants GET
        serializer = CategorySerializer(category)
        return Response(serializer.data)
    elif request.method == "PUT":  # if the user wants PUT
        category = Category.objects.get(pk=pk)
        # create a serializer that has a category from database + the data that the user sent
        serializer = CategorySerializer(
            category,
            data=request.data,
            partial=True,  # telling that we are just editing the data not creating
        )
        if serializer.is_valid():
            updated_category = serializer.save()
            return Response(CategorySerializer(updated_category).data)
        else:
            return Response(serializer.errors)

    elif request.method == "DELETE":
        category.delete()
        return Response(status=HTTP_204_NO_CONTENT)
