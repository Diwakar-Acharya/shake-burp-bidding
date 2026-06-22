from django.contrib import admin

from .models import *


admin.site.register(
    AuctionProduct
)

admin.site.register(
    Bid
)