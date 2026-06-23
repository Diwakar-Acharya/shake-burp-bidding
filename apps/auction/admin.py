from django.contrib import admin

from .models import AuctionProduct
from .models import Bid


@admin.register(AuctionProduct)
class ProductAdmin(admin.ModelAdmin):

    list_display=(

        'id',

        'name',

        'current_price',

        'auction_end',

        'active'

    )

    list_editable=(

        'active',

    )



@admin.register(Bid)
class BidAdmin(admin.ModelAdmin):

    list_display=(

        'id',

        'user',

        'product',

        'amount',

        'status',

        'created'

    )

    list_filter=(

        'status',

    )

    list_editable=(

        'status',

    )