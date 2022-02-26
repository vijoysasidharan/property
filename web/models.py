from django.urls import reverse
from django.db import models

class PropertyType(models.Model):
    property_type_name      = models.CharField(max_length=50, unique=True)
    slug                    = models.SlugField(max_length=50, unique=True)

    class Meta:
        verbose_name        = 'Property Type'
        verbose_name_plural = 'Property Types'

    def get_slug_url(self):
        return reverse('property_by_type', args=[self.slug])

    def __str__(self):
        return self.property_type_name

class PropertyCategory(models.Model):
    property_category_name  = models.CharField(max_length=50, unique=True)
    slug                    = models.SlugField(max_length=50, unique=True)

    class Meta:
        verbose_name        = 'Category'
        verbose_name_plural = 'Categories'

    def get_slug_url(self):
        return reverse('property_by_category', args=[self.slug])

    def __str__(self):
        return self.property_category_name

class Property(models.Model):
    property_title          = models.CharField(max_length=250, unique=True)
    slug                    = models.SlugField(max_length=250, unique=True)
    property_type           = models.ForeignKey(PropertyType, on_delete=models.CASCADE)
    property_category       = models.ForeignKey(PropertyCategory, on_delete=models.CASCADE)
    created_on              = models.DateTimeField(auto_now_add=True)
    updated_on              = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name                = 'Property'
        verbose_name_plural         = 'Properties'
    
    def get_slug_url(self):
        return reverse('property_detail', args=[self.property_category.slug, self.slug])

    def __str__(self):
        return self.property_title