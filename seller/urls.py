
from django.urls import path
from .views import *


urlpatterns = [
    path('index/',seller_index,name="seller_index"),
    path('login/',seller_login,name="seller_login"),
    path('signup/',seller_signup,name="seller_signup"),
    path('otp/',seller_otp,name='seller_otp'),
    path('404/',seller_404,name='seller_404'),
    path('blank/',seller_blank,name='seller_blank'),
    path('buttons/',seller_buttons,name='seller_buttons'),
    path('charts/',seller_charts,name='seller_charts'),
    path('grids/',seller_grids,name='seller_grids'),
    path('icons/',seller_icons,name='seller_icons'),
    path('inbox-details/',seller_inbox_details,name='seller_inbox_details'),
    path('inbox/',seller_inbox,name='seller_inbox'),
    path('maps/',seller_maps,name='seller_maps'),
    path('portlet/',seller_portlet,name='seller_portlet'),
    path('price/',seller_price,name='seller_price'),
    path('typography/',seller_typography,name='seller_typography'),
    path('logout/',seller_logout,name='seller_logout'),
    path('add_product/',add_product,name='add_product'),
    path('my_products/',my_products,name='my_products'),
    path('delete_product/<int:pk>',delete_product,name='delete_product'),
    path('edit_product/<int:pid>',edit_product,name='edit_product'),
    path('order/',seller_order,name='seller_order'),
    path('dispatched/<int:pk>',dispatched,name='dispatched')

] 