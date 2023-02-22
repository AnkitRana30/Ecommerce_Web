from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.core.mail import send_mail
from random import randint
from django.conf import settings
from seller.models import *
import razorpay
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseBadRequest

# Create your views here.
def index(request):
    all_products=Products.objects.all()
    try:
        user_data=Buyer.objects.get(email=request.session['email'])
        return render(request,'index.html',{'user_data':user_data,'all_products':all_products})

    except:
        return render(request,'index.html',{'all_products':all_products})
def about(request):
    try:
        user_obj=Buyer.objects.get(email=request.session['email'])
        return render(request,'about.html',{'user_data':user_obj})
    except:
        return render(request,'about.html')
def bread(request):
    try:
        user_data=Buyer.objects.get(email=request.session['email'])
        return render(request,'bread.html',{'user_data':user_data})
    except:
        return render(request,'bread.html')


        
def checkout(request):
    try:
        user_data=Buyer.objects.get(email=request.session['email'])
        return render(request,'checkout.html',{'user_data':user_data})
    except:
        return render(request,'checkout.html')




def drinks(request):
    try:
        user_data=Buyer.objects.get(email=request.session['email'])
        return render(request,'drinks.html',{'user_data':user_data})
    except:
        return render(request,'drinks.html')
def events(request):
    try:
        user_data=Buyer.objects.get(email=request.session['email'])
        return render(request,'events.html',{'user_data':user_data})
    except:
        return render(request,'events.html')
def faqs(request):
    try:
        user_data=Buyer.objects.get(email=request.session['email'])
        return render(request,'faqs.html',{'user_data':user_data})
    except:
        return render(request,'faqs.html')
def frozen(request):
    try:
        user_data=Buyer.objects.get(email=request.session['email'])
        return render(request,'frozen.html',{'user_data':user_data})
    except:
        return render(request,'frozen.html')
def household(request):
    try:
        user_data=Buyer.objects.get(email=request.session['email'])
        return render(request,'household.html',{'user_data':user_data})
    except:
        return render(request,'household.html')
def kitchen(request):
    try:
        user_data=Buyer.objects.get(email=request.session['email'])
        return render(request,'kitchen.html',{'user_data':user_data})
    except:
        return render(request,'kitchen.html')
def mail(request):
    try:
        user_data=Buyer.objects.get(email=request.session['email'])
        return render(request,'mail.html',{'user_data':user_data})
    except:
        return render(request,'mail.html')
def payment(request):
    try:
        user_data=Buyer.objects.get(email=request.session['email'])
        return render(request,'payment.html',{'user_data':user_data})
    except:
        return render(request,'payment.html')
def pet(request):
    try:
        user_data=Buyer.objects.get(email=request.session['email'])
        return render(request,'pet.html',{'user_data':user_data})
    except:
        return render(request,'pet.html')
def privacy(request):
    try:
        user_data=Buyer.objects.get(email=request.session['email'])
        return render(request,'privacy.html',{'user_data':user_data})
    except:
        return render(request,'privacy.html')
def products(request):
    try:
        user_data=Buyer.objects.get(email=request.session['email'])
        return render(request,'products.html',{'user_data':user_data})
    except:
        return render(request,'products.html')
def services(request):
    try:
        user_data=Buyer.objects.get(email=request.session['email'])
        return render(request,'services.html',{'user_data':user_data})
    except:
        return render(request,'services.html')
def short_codes(request):
    try:
        user_data=Buyer.objects.get(email=request.session['email'])
        return render(request,'short_codes.html',{'user_data':user_data})
    except:
        return render(request,'short_codes.html')
def single(request):
    try:
        user_data=Buyer.objects.get(email=request.session['email'])
        return render(request,'single.html',{'user_data':user_data})
    except:
        return render(request,'single.html')
def vegetables(request):
    try:
        user_data=Buyer.objects.get(email=request.session['email'])
        return render(request,'vegetables.html',{'user_data':user_data})
    except:
        return render(request,'vegetables.html')

# def add_data(request):
#     Buyer.objects.create(
#         first_name='Ankit',
#         last_name='Rana',
#         email='ankit12345@gmail.com',
#         password='ankit123',
#         address='1 jaganth socitey khatodara surat'
#     )
#     return HttpResponse('Creat Row')

# def delete_row(request):
#     user_object=Buyer.objects.get(email='ankit1234@gmail.com')
#     user_object.delete()
#     return HttpResponse('Delete Row')

def register(request):
    if request.method=='GET':
        return render(request,'register.html')
    else:
        try:
            Buyer.objects.get(email=request.POST['email'])
            return render(request,'register.html',{'msg':'Email Is Already Exist'})
        except:
            if request.POST['password']==request.POST['repassword']:
                global user_data
                user_data=[
                    request.POST['firstname'],
                    request.POST['lastname'],
                    request.POST['email'],
                    request.POST['password'],

                ]
                s="Registration!!!"
                global c_otp
                c_otp=randint(1000,9999)
                m=f"Hello User!!\nYour OTP is {c_otp}"
                f=settings.EMAIL_HOST_USER
                r=[request.POST['email']]
                send_mail(s,m,f,r)
                return render(request,'otp.html',{'message':'Check Your MailBox'})
            else:
                return render(request,'register.html',{'msg':'Both Password Do not Match!!'})

def otp(request):
    if request.POST['u_otp']==str(c_otp):
        Buyer.objects.create(
            first_name=user_data[0],
            last_name=user_data[1],
            email=user_data[2],
            password=user_data[3]
        )
        return render(request,'login.html',{'ar':'Account Created Succesfully'})
    else:
        return render(request,'otp.html',{'msg':'Incorrect OTP!!'})


def login(request):
    if request.method =='GET':
        return render(request,'login.html')
    else:
        try:
            user_obj= Buyer.objects.get(email =request.POST['email'])
            if user_obj.password==request.POST['password']:
                request.session['email']=request.POST['email']
                return redirect('index')
            else:
                return render(request,'login.html',{'ar':'Passward Invalied'})
        except:
            return render(request,'login.html',{'ar':'Email Is Not Registered!!'} )

def logout(request):
    del request.session['email']
    return redirect('login')

def add_to_cart(request,pk):
    try:
        buyer_obj = Buyer.objects.get(email = request.session['email'])
        Cart.objects.create(
            product = Products.objects.get(id = pk),
            buyer = buyer_obj
        )
        return redirect('index')
    except:
        return redirect('login')
    

razorpay_client = razorpay.Client(
auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))  


def cart(request):
    
    try:
        buyer_obj=Buyer.objects.get(email=request.session['email'])
        cart_data=Cart.objects.filter(buyer=buyer_obj)
        global total_amount
        total_amount=0
        for i in cart_data:
            total_amount += i.product.price

          
        currency = 'INR'
        if total_amount == 0:
            total_amount = 10
        amount = total_amount * 100  # Rs. 200
        
        # Create a Razorpay Order
        razorpay_order = razorpay_client.order.create(dict(amount=amount,
                                                        currency=currency,
                                                        payment_capture='0'))
        
        # order id of newly created order.
        razorpay_order_id = razorpay_order['id']
        callback_url = 'paymenthandler/'
        
        # we need to pass these details to frontend.
        context = {}
        context['razorpay_order_id'] = razorpay_order_id
        context['razorpay_merchant_key'] = settings.RAZOR_KEY_ID
        context['razorpay_amount'] = amount
        context['currency'] = currency
        context['callback_url'] = callback_url
        context['user_data'] = buyer_obj
        context['cart_data'] = cart_data
        context['p_count'] = len(cart_data)
        context['total_amount'] = total_amount

        return render(request, 'cart.html', context=context)


    # {'user_data':buyer_obj,'cart_data':cart_data,'p_count':len(cart_data),'total_amount':total_amount}
    except:
        return redirect('login')
    

def delete_cart(request,pk):
    cart_obj=Cart.objects.get(id=pk)
    cart_obj.delete()
    return redirect('cart')



@csrf_exempt
def paymenthandler(request):
 
    # only accept POST request.
    if request.method == "POST":
        try:
           
            # get the required parameters from post request.
            buyer_obj=Buyer.objects.get(email=request.session['email'])
            payment_id = request.POST.get('razorpay_payment_id', '')
            razorpay_order_id = request.POST.get('razorpay_order_id', '')
            signature = request.POST.get('razorpay_signature', '')
            params_dict = {
                'razorpay_order_id': razorpay_order_id,
                'razorpay_payment_id': payment_id,
                'razorpay_signature': signature
            }
 
            # verify the payment signature.
            result = razorpay_client.utility.verify_payment_signature(
                params_dict)
            if result is not None:
                amount = total_amount * 100  # Rs. 200
                try:
 
                    # capture the payemt
                    razorpay_client.payment.capture(payment_id, amount)
                    buyer_obj=Buyer.objects.get(email=request.session['email'])
                    c_data=Cart.objects.filter(buyer=buyer_obj)
                    for i in c_data:
                        MyOrders.objects.create(
                            buyer=buyer_obj,
                            product=i.product,
                            status=1
                        )
                        i.delete()
                    # render success page on successful caputre of payment
                    return render(request, 'successful.html',{'buyer_obj':buyer_obj,'amount':total_amount})
                except:
 
                    # if there is an error while capturing payment.
                    return render(request, 'fail.html')
            else:
 
                # if signature verification fails.
                return render(request, 'fail.html')
        except:
 
            # if we don't find the required parameters in POST data
            return HttpResponseBadRequest()
    else:
       # if other than POST request is made.
        return HttpResponseBadRequest()