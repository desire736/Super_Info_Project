from django.contrib import admin
from .models import Hashtags, Publications, Category, Contacts

@admin.register(Hashtags)
class HashtagsAdmin(admin.ModelAdmin):
   list_display = ['title']

@admin.register(Publications)
class PublicationsAdmin(admin.ModelAdmin):
   list_display = ['title']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
   list_display = ['title']

@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
   list_display = ['name']

   # def has_add_permission(self, request):
   #    return False
   #
   # def has_change_permission(self, request, obj):
   #    return False