from django.db import models
from django.conf import settings


class AuctionProduct(models.Model):

    name = models.CharField(max_length=300)
    description = models.TextField()

    image = models.ImageField(upload_to='products/')
    image2 = models.ImageField(upload_to='products/', blank=True)
    image3 = models.ImageField(upload_to='products/', blank=True)

    video = models.URLField(blank=True)
    story = models.TextField(blank=True)

    # ✅ INTEGER PRICES (PAISE)
    starting_price = models.IntegerField(default=0)
    current_price = models.IntegerField(default=0)

    end_time = models.DateTimeField()
    active = models.BooleanField(default=True)


class Bid(models.Model):

    PAYMENT = [
        ('pending', 'Pending'),
        ('paid', 'Paid')
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(AuctionProduct, on_delete=models.CASCADE)

    # ✅ INTEGER AMOUNT
    amount = models.IntegerField(default=0)

    payment = models.CharField(max_length=20, choices=PAYMENT, default='pending')
    shipment = models.TextField(blank=True)

    created = models.DateTimeField(auto_now_add=True)


class Order(models.Model):

    STATUS = [
        ('pending', 'Pending'),
        ('paid', 'Paid'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered')
    ]

    bid = models.OneToOneField(Bid, on_delete=models.CASCADE)

    full_name = models.CharField(max_length=300)
    phone = models.CharField(max_length=20)
    address = models.TextField()
    city = models.CharField(max_length=100)
    pincode = models.CharField(max_length=20)

    status = models.CharField(max_length=30, choices=STATUS, default='pending')

    created = models.DateTimeField(auto_now_add=True)