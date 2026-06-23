from django.shortcuts import (
render,
redirect
)

from django.contrib.admin.views.decorators import (
staff_member_required
)

from apps.auction.models import *



@staff_member_required
def owner_dashboard(request):


    product=AuctionProduct.objects.first()


    bids=Bid.objects.all().order_by(
        '-created'
    )


    return render(

request,

'dashboard/dashboard.html',

{

'product':product,

'bids':bids

}

)



@staff_member_required
def approve_bid(

request,

bid_id

):


    bid=Bid.objects.get(
        id=bid_id
    )


    bid.status='approved'

    bid.save()


    product=bid.product


    product.current_price=bid.amount

    product.save()


    return redirect(
        '/owner/'
    )



@staff_member_required
def reject_bid(

request,

bid_id

):


    bid=Bid.objects.get(
        id=bid_id
    )


    bid.status='rejected'

    bid.save()


    return redirect(
        '/owner/'
    )