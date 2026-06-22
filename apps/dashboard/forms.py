from django import forms

from apps.auction.models import (
AuctionProduct
)


class ProductEditForm(
forms.ModelForm
):


    class Meta:

        model=AuctionProduct

        fields='__all__'