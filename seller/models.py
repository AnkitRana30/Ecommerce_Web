from django.db import models

# Create your models here.
class Seller(models.Model):
    full_name=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=50)
    gst_no=models.CharField(max_length=15)
    pic=models.FileField(upload_to='profile_pics',default='sad.jpg')

    def __str__(self):
        return self.email


class Products(models.Model):
    product_name = models.CharField(max_length=150)
    des = models.CharField(max_length=200)
    price = models.FloatField(default=1.0)
    product_stock = models.IntegerField(default=0)
    pic = models.FileField(upload_to='product_pics', default='sad.jpg')
    seller = models.ForeignKey(Seller, on_delete= models.CASCADE)

    def __str__(self):
        return self.product_name    

class MyOrders(models.Model):
    var1=[
        (1,'Pending'),
        (2,'Dispatched')
    ]
    buyer=models.ForeignKey(to="buyer.Buyer",on_delete=models.CASCADE)
    product=models.ForeignKey(Products,on_delete=models.CASCADE)
    status=models.CharField(max_length=40,choices=var1)

    def __str__(self):
        return self.buyer.first_name
    