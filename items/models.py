from django.db import models

# Create your models here.
class Item(models.Model):
	item_image = models.ImageField(upload_to = 'item_images/')
	item_text = models.CharField(max_length = 300)