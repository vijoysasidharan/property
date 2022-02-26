from .models import *

def all_property_types(request):
    property_type_links = PropertyType.objects.all()
    return dict(property_type_links=property_type_links)

def all_property_categories(request):
    property_category_links = PropertyCategory.objects.all()
    return dict(property_category_links=property_category_links)