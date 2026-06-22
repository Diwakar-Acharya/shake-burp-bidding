from django.shortcuts import render, redirect, get_object_or_404
from .models import AuctionProduct, Bid
from .forms import CheckoutForm


def place_bid(request):

    if not request.user.is_authenticated:
        return redirect('/')

    if request.method == "POST":

        amount = request.POST.get('amount')

        if not amount:
            return redirect('/')

        try:
            amount = int(amount)
        except ValueError:
            return redirect('/')

        product = AuctionProduct.objects.first()

        if not product:
            return redirect('/')

        current_price = int(product.current_price)

        # reject lower bids
        if amount < current_price:
            return redirect('/')

        Bid.objects.create(
            user=request.user,
            amount=amount,
            product=product
        )

        product.current_price = amount
        product.save()

    return redirect('/')


def checkout(request, bid_id):

    bid = get_object_or_404(Bid, id=bid_id)

    if request.method == "POST":

        form = CheckoutForm(request.POST)

        if form.is_valid():

            order = form.save(commit=False)
            order.bid = bid
            order.save()

            return redirect('/')

    else:
        form = CheckoutForm()

    return render(
        request,
        'checkout.html',
        {
            'form': form,
            'bid': bid
        }
    )