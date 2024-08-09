from django.contrib import admin
from .models import Hashtags, Publications, Category

@admin.register(Hashtags)
class HashtagsAdmin(admin.ModelAdmin):
   list_display = ['title']

@admin.register(Publications)
class PublicationsAdmin(admin.ModelAdmin):
   list_display = ['title']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
   list_display = ['title']