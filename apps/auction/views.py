from django.shortcuts import redirect
from .models import AuctionProduct
from .models import Bid


def place_bid(request):


    if not request.user.is_authenticated:

        return redirect('/')


    if request.method == 'POST':

        product_id = request.POST.get(
            'product'
        )

        amount = request.POST.get(
            'amount'
        )


        product = AuctionProduct.objects.get(
            id=product_id
        )


        # BLOCK IF AUCTION ENDED
        if product.ended:

            return redirect('/')


        Bid.objects.create(

            user=request.user,

            product=product,

            amount=amount,

            status='pending'

        )


    return redirect('/')