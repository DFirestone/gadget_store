from django.db import models

# Create your models here.
class ProductPrice(models.Model):
	product_name = models.CharField(max_length=200)
	product_desription = models.CharField(max_length=500)
	price = models.DecimalField(decimal_places=2, max_digits=6)
	quantity = models.IntegerField()
	
