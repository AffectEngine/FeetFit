from django.db import models


class FoodCategory(models.Model):
	name = models.CharField(max_length=50)
	image = models.ImageField(upload_to='food_categories/', blank=True, null=True)

	def __str__(self):
		return self.name


class FoodItem(models.Model):
	category = models.ForeignKey(FoodCategory, on_delete=models.CASCADE)
	name = models.CharField(max_length=100)
	price = models.DecimalField(max_digits=6, decimal_places=2)
	is_on_sale = models.BooleanField(default=False)
	sale_price = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
	image = models.ImageField(upload_to='food_items/', blank=True, null=True)

	def __str__(self):
		return self.name
