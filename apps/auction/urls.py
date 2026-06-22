from django.urls import path

from .views import *


urlpatterns=[

path(
'bid/',
place_bid
),

path(
'checkout/<int:bid_id>/',
checkout
)

]