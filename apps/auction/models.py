from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver



class AuctionProduct(models.Model):

    name=models.CharField(
        max_length=300
    )

    description=models.TextField()

    story=models.TextField(
        blank=True,
        null=True
    )

    image=models.ImageField(
        upload_to='products/'
    )

    image2=models.ImageField(
        upload_to='products/',
        blank=True,
        null=True
    )

    image3=models.ImageField(
        upload_to='products/',
        blank=True,
        null=True
    )

    video=models.URLField(
        blank=True,
        null=True
    )

    current_price=models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=1
    )

    active=models.BooleanField(
        default=True
    )

    auction_end=models.DateTimeField(
        null=True,
        blank=True
    )

    winner=models.ForeignKey(
        User,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='won_products'
    )


    @property
    def ended(self):

        if self.auction_end:

            if timezone.now()>self.auction_end:

                if self.active:

                    self.close()

                return True

        return False


    def close(self):

        top=Bid.objects.filter(

            product=self,

            status='approved'

        ).order_by(
            '-amount'
        ).first()


        if top:

            self.winner=top.user

            self.current_price=top.amount


        self.active=False

        self.save()


    def __str__(self):

        return self.name




class Bid(models.Model):

    STATUS=(

        ('pending','Pending'),

        ('approved','Approved'),

        ('rejected','Rejected')

    )


    user=models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )


    product=models.ForeignKey(
        AuctionProduct,
        on_delete=models.CASCADE
    )


    amount=models.DecimalField(
        max_digits=12,
        decimal_places=2
    )


    created=models.DateTimeField(
        auto_now_add=True
    )


    status=models.CharField(
        max_length=20,
        choices=STATUS,
        default='pending'
    )


    def __str__(self):

        return f'{self.user} - ₹{self.amount}'




@receiver(
    post_save,
    sender=Bid
)
def update_price(
    sender,
    instance,
    **kwargs
):

    if instance.status=='approved':

        product=instance.product

        if instance.amount>product.current_price:

            product.current_price=instance.amount

            product.save()