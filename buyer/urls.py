
from django.urls import path
from .views import *

urlpatterns = [
    path('',index,name="index"),
    path('about/',about,name="about"),
    path('bread/',bread,name="bread"),
    path('checkout/',checkout,name="checkout"),
    path('drinks/',drinks,name="drinks"),
    path('events/',events,name="events"),
    path('faqs/',faqs,name="faqs"),
    path('frozen/',frozen,name="frozen"),
    path('household/',household,name="household"),
    path('kitchen/',kitchen,name="kitchen"),
    path('login/',login,name="login"),
    path('mail/',mail,name="mail"),
    path('payment/',payment,name="payment"),
    path('pet/',pet,name="pet"),
    path('privacy/',privacy,name="privacy"),
    path('products/',products,name="products"),
    path('services/',services,name="services"),
    path('short_codes/',short_codes,name="short_codes"),
    path('single/',single,name="single"),
    path('vegetables/',vegetables,name="vegetables"),
    path('register/',register,name="register"),
    path('otp/',otp,name="otp"),
    path('logout/',logout,name="logout"),
    path('cart/',cart,name="cart"),
    path('add_to_cart/', add_to_cart, name="add_to_cart"),
    path('delete_cart/<int:pk>', delete_cart, name="delete_cart"),
    path('cart/paymenthandler/',paymenthandler, name='paymenthandler'),
    path('del_cart_item/',del_cart_item, name='del_cart_item'),
    
    # path('add_data/',add_data,name="add_data"),
    # path('delete_row/',delete_row,name="delete_row"),
    

]
