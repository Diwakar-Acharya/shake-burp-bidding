from django.shortcuts import render

from django.utils import timezone

from apps.auction.models import (
AuctionProduct,
Bid
)


def home(request):

    product=AuctionProduct.objects.first()

    bids=[]

    highest=None

    ended=False


    if product:

        bids=Bid.objects.filter(
            product=product
        ).order_by(
            '-amount'
        )[:10]


        highest=Bid.objects.filter(
            product=product
        ).order_by(
            '-amount'
        ).first()


        if timezone.now()>product.end_time:

            ended=True

            product.active=False

            product.save()


    return render(

        request,

        'core/home.html',

        {

            'product':product,

            'bids':bids,

            'highest':highest,

            'ended':ended

        }

    )