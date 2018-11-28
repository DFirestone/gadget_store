from django.db import models

# Create your models here.
class Product(models.Model):
	product_name = models.CharField(max_length=200)
	product_description = models.CharField(max_length=500)
	price = models.DecimalField(decimal_places=2, max_digits=8)
	quantity = models.IntegerField()

	def __str__(self):
		return self.product_name
	
