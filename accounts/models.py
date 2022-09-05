from django.db import models

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)
    def __str__(self):
        return self.name


class Product(models.Model):
    # this give you the option in the admin panel
    CATEGORY = (
             ('Indoor', 'Indoor'),
             ('Out door', 'Out door'),
             ('Delivered', 'Delivered'),
    )
    # this model values will be called in the views and products class
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY, blank=True)
    description = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name

class Order(models.Model):
    # this give you the option in the admin panel
    STATUS = (
             ('Pending', 'Pending'),
             ('Out for Delivery', 'Out for Delivery'),
             ('Delivered', 'Delivered'),
    )
    # this model populates to be a 
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    product =  models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
 
    def __str__(self):
        return self.product.name