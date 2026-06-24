from django.urls import path

from .views import (
    place_bid,
    approve_bid,
    reject_bid
)

urlpatterns=[

    path(
        'bid/',
        place_bid
    ),

    path(
        'approve/<int:bid_id>/',
        approve_bid
    ),

    path(
        'reject/<int:bid_id>/',
        reject_bid
    ),

]