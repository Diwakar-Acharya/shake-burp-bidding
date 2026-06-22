from django.urls import path

from .views import *


urlpatterns=[

path(
'',
owner_dashboard
),

path(
'payment/<int:bid_id>/',
payment_done
)

]