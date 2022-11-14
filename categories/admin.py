from django.contrib import admin
from .models import Category

# Register your models here.


# register 를 해야 화면에 보임
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass
