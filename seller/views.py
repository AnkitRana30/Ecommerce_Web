from django.shortcuts import render,redirect
from .models import *
from django.core.mail import send_mail
from random import randint
from django.conf import settings
from django.http import HttpResponse
# Create your views here.
def seller_index(request):
    try:
        seller=Seller.objects.get(email=request.session['seller_email'])
        return render(request,'seller_index.html',{'seller_data':seller})
    except:
        return render(request,'seller_login.html')


def seller_signup(request):
    if request.method=='GET':
        return render(request,'seller_signup.html')
    else:
        try:
            Seller.objects.get(email=request.POST['email'])
            return render(request,'seller_signup.html',{'msg':'Email Is Already Exist'})
        except:
            if request.POST['password']==request.POST['repassword']:
                global user_data
                user_data=[
                    request.POST['full_name'],
                    request.POST['email'],
                    request.POST['gst_no'],
                    request.POST['password']
                ]

                s="Registration!!!"
                global c_otp
                c_otp=randint(1000,9999)
                m=f"Hello User!!\nYour OTP is {c_otp}"
                f=settings.EMAIL_HOST_USER
                r=[request.POST['email']]
                send_mail(s,m,f,r)
                return render(request,'seller_otp.html',{'msg':'Cheack MailBox'})
            else:
                return render(request,'seller_signup.html',{'msg':'Both Password Do not Match!!'})

def seller_otp(request):
    if request.POST['u_otp']== str(c_otp):
        Seller.objects.create(
            full_name=user_data[0],
            email=user_data[1],
            gst_no=user_data[2], 
            password=user_data[3]
            
        )
        return render(request,'seller_login.html',{'ar':'Account Create Succsfully'})
    else:
        return render(request,'seller_otp.html',{'msg':'Incorrect OTP!!'})

def seller_login(request):
    if request.method=='GET':
        return render(request,'seller_login.html')
    else:
        try:
            seller_obj=Seller.objects.get(email=request.POST['email'])
            if seller_obj.password==request.POST['password']:
                request.session['seller_email']=request.POST['email']
                return redirect('seller_index')
            else:
                return render(request,'seller_login.html',{'ar':'Passward Invalied'})
        except:
            return render(request,'seller_login.html',{'ar':'Email Is Not Registered!!'})
def seller_logout(request):
    del request.session['seller_email']
    return redirect('seller_login')

def add_product(request):
    if request.method=='GET':
        sellerdata=Seller.objects.get(email=request.session['seller_email'])
        return render(request,'add_product.html',{'seller_data':sellerdata})
    else:
        seller_obj=Seller.objects.get(email=request.session['seller_email'])
        Products.objects.create(
            product_name = request.POST['product_name'],
            des = request.POST['des'],
            price = request.POST['price'],
            product_stock = request.POST['product_stock'],
            pic = request.FILES['pic'],
            seller = seller_obj
        )
        return render(request,'add_product.html',{'msg':'Successfully Added'})

def my_products(request):
    seller_data=Seller.objects.get(email=request.session['seller_email'])
    session_seller=Products.objects.filter(seller=seller_data)
    return render(request,'my_products.html',{'seller_data':seller_data,'user_products':session_seller})

def delete_product(request,pk):
    delete_prod=Products.objects.get(id=pk)
    delete_prod.delete()
    return redirect('my_products')

def edit_product(request,pid):
    s_product=Products.objects.get(id=pid)
    if request.method=='GET':
        seller_data=Seller.objects.get(email=request.session['seller_email'])
        return render(request,'edit_product.html',{'product_data':s_product , 'seller_data':seller_data})
    else:
        s_product.product_name = request.POST['product_name']
        s_product.price = request.POST['price']
        s_product.des = request.POST['des']
        s_product.product_stock = request.POST['product_stock']
        if request.FILES:
            s_product.pic = request.FILES['pic']
        s_product.save()
        return redirect('my_products')



def seller_404(request):
    return render(request,'404.html')
def seller_blank(request):
    return render(request,'blank.html')
def seller_buttons(request):
    return render(request,'buttons.html')
def seller_charts(request):
    return render(request,'charts.html')
def seller_grids(request):
    return render(request,'grids.html')
def seller_icons(request):
    return render(request,'icons.html')
def seller_inbox_details(request):
    return render(request,'inbox_details.html')
def seller_inbox(request):
    return render(request,'inbox.html')
def seller_maps(request):
    return render(request,'maps.html')
def seller_portlet(request):
    return render(request,'portlet.html')
def seller_price(request):
    return render(request,'price.html')
def seller_order(request):
        seller=Seller.objects.get(email=request.session['seller_email'])
        my_order=MyOrders.objects.filter(product__seller=seller)
        return render(request,'seller_order.html',{'seller_data':seller,'my_orders':my_order})
def seller_typography(request):
    return render(request,'typography.html')
def dispatched(request,pk):
    m_row=MyOrders.objects.get(id=pk)
    m_row.status=2
    m_row.save()
    return redirect('seller_order')



