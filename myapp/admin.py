from django.contrib import admin
from .models import PersonDetailModel, ImageModel

@admin.register(PersonDetailModel)
class PersonDetailAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "email", "date_of_birth")

@admin.register(ImageModel)
class ImageAdmin(admin.ModelAdmin):
    list_display = ("id", "image", "owner")
