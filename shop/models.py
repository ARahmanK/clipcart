from django.db import models


class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=80)
    description = models.CharField(max_length=200)
    category = models.CharField(max_length=50, default='')
    subcategory = models.CharField(max_length=50, default='')
    price = models.FloatField(default=0.0)
    date = models.DateField()
    image = models.ImageField(upload_to='shop/images', default='')

    def __str__(self):
        return self.product_name
