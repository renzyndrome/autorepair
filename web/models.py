from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class ItemImage(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='item',
                              verbose_name='Image')