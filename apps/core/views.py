from django.shortcuts import render
from apps.auction.models import AuctionProduct


def home(request):

    product = AuctionProduct.objects.first()

    ended = True

    if product:
        ended = product.ended


    context = {

        'product': product,

        'ended': ended

    }

    return render(

        request,

        'core/home.html',

        context

    )