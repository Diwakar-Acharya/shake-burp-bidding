from datetime import timedelta

from django.shortcuts import (
    render,
    redirect,
    get_object_or_404
)

from django.contrib import messages
from django.utils import timezone

from .models import (
    AuctionProduct,
    Bid
)


def place_bid(request):

    if not request.user.is_authenticated:
        return redirect('/')


    if request.user.is_staff:

        messages.error(
            request,
            'Owner cannot bid'
        )

        return redirect('/')


    if request.method!="POST":

        return redirect('/')


    product=AuctionProduct.objects.first()

    amount=request.POST.get(
        'amount'
    )


    try:

        amount=float(amount)

    except:

        return redirect('/')


    if product.ended:

        messages.error(
            request,
            'Auction ended'
        )

        return redirect('/')


    if amount<=float(
        product.current_price
    ):

        messages.error(
            request,
            'Bid too low'
        )

        return redirect('/')


    Bid.objects.create(

        user=request.user,

        product=product,

        amount=amount

    )

    messages.success(
        request,
        'Bid submitted'
    )

    return redirect('/')



def approve_bid(
    request,
    bid_id
):

    if not request.user.is_staff:

        return redirect('/')


    bid=get_object_or_404(
        Bid,
        id=bid_id
    )

    bid.status='approved'

    bid.save()

    messages.success(
        request,
        'Bid approved'
    )

    return redirect('/owner/')




def reject_bid(
    request,
    bid_id
):

    if not request.user.is_staff:

        return redirect('/')


    bid=get_object_or_404(
        Bid,
        id=bid_id
    )

    bid.status='rejected'

    bid.save()

    messages.success(
        request,
        'Bid rejected'
    )

    return redirect('/owner/')