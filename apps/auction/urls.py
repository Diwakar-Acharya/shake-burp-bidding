from django.urls import path

from .views import place_bid


urlpatterns=[

path(

'bid/',

place_bid,

name='place_bid'

),

]