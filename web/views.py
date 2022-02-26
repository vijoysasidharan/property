from django.shortcuts import render, get_object_or_404
from .models import *
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q

def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

def buyerpricing(request):
    return render(request, "buyer-pricing.html")

def sellerpricing(request):
    return render(request, "seller-pricing.html")

def property_type(request, property_type_slug=None):
    type = None
    properties = None
    if property_type_slug != None:
        type = get_object_or_404(PropertyType, slug=property_type_slug)
        properties = Property.objects.all().filter(property_type=type).order_by('id')
        property_count = properties.count()
    else:
        properties = Property.objects.all().order_by('id')
        property_count = properties.count()

    paginator = Paginator(properties, 10) #Numer of products per page
    page = request.GET.get('page')
    paged_properties = paginator.get_page(page)
    
    context = {
        'type': type,
        'properties': paged_properties,
        'products_count': property_count,
    }
    return render(request, 'properties.html', context)

def property_category(request, property_category_slug=None):
    category = None
    properties = None
    if property_category_slug != None:
        category = get_object_or_404(PropertyCategory, slug=property_category_slug)
        properties = Property.objects.all().filter(property_category=category).order_by('id')
        property_count = properties.count()
    else:
        properties = Property.objects.all().order_by('id')
        property_count = properties.count()

    paginator = Paginator(properties, 10) #Numer of products per page
    page = request.GET.get('page')
    paged_properties = paginator.get_page(page)
    
    context = {
        'type': type,
        'properties': paged_properties,
        'products_count': property_count,
    }
    return render(request, 'properties.html', context)

def property_detail(request, property_category_slug, property_slug):
    try:
        single_property = Property.objects.get(property_category__slug=property_category_slug, slug=property_slug)
    except Exception as ex:
        raise ex

    context = {
        'single_property': single_property,
    }    
    return render(request, 'product_detail.html', context)