from django.urls import path

from .views import *


urlpatterns=[

path(
'',
owner_dashboard
),

path(
'approve/<int:bid_id>/',
approve_bid
),

path(
'reject/<int:bid_id>/',
reject_bid
)

]