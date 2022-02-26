from . import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('type/<slug:property_type_slug>/', views.property_type, name="property_by_type"),
    path('category/<slug:property_category_slug>/', views.property_category, name="property_by_category"),
    path('category/<slug:property_category_slug>/<slug:property_slug>/', views.property_detail, name="property_detail"),
]
