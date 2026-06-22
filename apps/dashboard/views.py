from django.shortcuts import (
render,
redirect
)

from django.contrib.admin.views.decorators import (
staff_member_required
)

from apps.auction.models import *

from .forms import (
ProductEditForm
)



@staff_member_required
def owner_dashboard(request):


    product=AuctionProduct.objects.first()


    bids=[]

    form=None


    if product:

        bids=Bid.objects.filter(
            product=product
        ).order_by(
            '-amount'
        )

        form=ProductEditForm(
            instance=product
        )


    if request.method=="POST":

        form=ProductEditForm(

            request.POST,

            request.FILES,

            instance=product

        )

        if form.is_valid():

            form.save()

            return redirect(
                '/owner/'
            )


    return render(

        request,

        'dashboard/dashboard.html',

        {

            'product':product,

            'bids':bids,

            'form':form

        }

    )



@staff_member_required
def payment_done(

request,

bid_id

):


    bid=Bid.objects.get(
        id=bid_id
    )


    bid.payment='paid'

    bid.save()


    return redirect(
        '/owner/'
    )