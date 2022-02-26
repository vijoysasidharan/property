from django.contrib import admin
from .models import *
# Register your models here.

class PropertyTypeAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('property_type_name', )}
    list_display = ('id', 'property_type_name', 'slug')

class PropertyCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('property_category_name', )}
    list_display = ('id', 'property_category_name', 'slug')

class PropertyAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('property_title', )}
    list_display = ('id', 'property_title', 'property_type', 'property_category', 'created_on')


admin.site.register(PropertyType, PropertyTypeAdmin)
admin.site.register(PropertyCategory, PropertyCategoryAdmin)
admin.site.register(Property, PropertyAdmin)
