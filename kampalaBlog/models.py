from django.db import models

#Create your models here.
class Destination(models.Model):   
    Name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media')
    description = models.TextField()
    price = models.IntegerField()
    special_offer = models.BooleanField(default=False)

class Message(models.Model):
    author = models.CharField(max_length=100,null=False,blank=False)
    email = models.EmailField(blank=False,null=False)
    comment = models.CharField(max_length=200, blank=False)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.author


class Products(models.Model):
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='products/')

    def __str__(self):
        return self.name


