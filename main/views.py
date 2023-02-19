from django.shortcuts import render,HttpResponse
from main.models import *
from django.core.files.storage import FileSystemStorage
from datetime import date,datetime 
# import razorpay
# from razorpay import Client



# Create your views here.

################################################# public #########################################
def home(request):
    q1=product.objects.all()
    print(q1,"**********************")
   
    return render(request,'home.html',{'q1':q1})


def about(request):
    return render(request,'about.html')



def products(request):
    q1=product.objects.all()
    print(q1,"**********************")
    # if request.method=='POST':
    #     pla=request.POST['pla']
        
    #     q1=product.objects.filter(product_name=pla)|product.objects.filter(category__category=pla)
    #     print(q1,"$$$$$$$$$$$$$$$$$$$$$$$$$$")
    return render(request,'products.html',{'q1':q1})



def logins(request):
    if request.method=="POST":
        uname=request.POST['uname']
        pwd=request.POST['pwd']
        print(uname,pwd)
        
        try:
            lg=login.objects.get(username=uname)
            print(lg,"........................")
   
            request.session['login_id']=lg.pk
            if lg.usertype=='admin':
               
                return HttpResponse("<script>alert('Welcome Admin......!');window.location='adminhome';</script>")
            elif lg.usertype=='user':
                return HttpResponse("<script>alert('Welcome User......!');window.location='user_home';</script>")
            elif lg.usertype=='dealer':
                return HttpResponse("<script>alert('Welcome Dealer......!');window.location='dealer_home';</script>")
      
        except:
            return HttpResponse("<script>alert('login Failed...!!!!');window.location='logins';</script>")
    return render(request,'login.html')




def user_register(request):
    if request.method=="POST":
        fn=request.POST['fn']
        ln=request.POST['ln']
        pl=request.POST['pl']
        ph=request.POST['ph']
        em=request.POST['em']
        uname=request.POST['uname']
        pwd=request.POST['pwd']
        print(fn,ln,pl,ph,em,uname,pwd)
        q=login.objects.filter(username=uname)
        if q:
            return HttpResponse("<script>alert('Username Already Exist....!!!');window.location='user_register';</script>")
        else:
            lg=login(username=uname,password=pwd,usertype='user')
            lg.save()
            pt=user(fname=fn,lname=ln,place=pl,phone=ph,email=em,login=lg)
            pt.save()
            return HttpResponse("<script>alert('Added Successfully....!!!');window.location='user_register';</script>")
    return render(request,'user_reg.html')



def dealer_register(request):
    if request.method=="POST":
        fn=request.POST['fn']
        ln=request.POST['ln']
        pl=request.POST['pl']
        ph=request.POST['ph']
        em=request.POST['em']
        uname=request.POST['uname']
        pwd=request.POST['pwd']
        print(fn,ln,pl,ph,em,uname,pwd)
        q=login.objects.filter(username=uname)
        if q:
            return HttpResponse("<script>alert('Username Already Exist....!!!');window.location='dealer_register';</script>")
        else:
            lg=login(username=uname,password=pwd,usertype='pending')
            lg.save()
            pt=dealer(fname=fn,lname=ln,place=pl,phone=ph,email=em,login=lg)
            pt.save()
            return HttpResponse("<script>alert('Added Successfully....!!!');window.location='dealer_register';</script>")
    return render(request,'dealer_register.html')



################################################# admin #######################################################

def adminhome(request):
    us=user.objects.all().count() 

    de=dealer.objects.all().count()


    
    return render(request,'adminhome.html',{'us':us,'de':de})



def admin_view_user(request):
    q=user.objects.all()
    return render(request,'admin_view_users.html',{'q':q})




def admin_manage_category(request):
    if request.method=="POST":
        cat=request.POST['cat']
        q=category.objects.filter(category=cat)
        if q:
             return HttpResponse("<script>alert('Already Exist....!!!');window.location='/admin_manage_category';</script>")
        else:
            lg=category(category=cat)
            lg.save()
            return HttpResponse("<script>alert('Added Successfully....!!!');window.location='/admin_manage_category';</script>")

    q=category.objects.all()
    return render(request,'admin_manage_category.html',{'q':q})




def admin_remove_category(request,id):
    q=category.objects.filter(id=id)
    q.delete()
    return HttpResponse("<script>alert('Removed...!!!');window.location='/admin_manage_category';</script>")







def admin_manage_product(request):
    lid=request.session['login_id']

    d=dealer.objects.all()

    q1=category.objects.all()
    if request.method=="POST":
        dea=request.POST['dea']
        pro=request.POST['pro']
        img=request.FILES['img']
        rt=request.POST['rate']
        qu=request.POST['qu']  
        des=request.POST['des']
        cat=request.POST['cat']
        fs=FileSystemStorage()
        vv=fs.save(img.name,img)
        q=product(product_name=pro,rate=rt,stock=qu,image=vv,p_description=des,category_id=cat,dealer_id=dea)
        q.save()
        return HttpResponse("<script>alert('Added Successfully....!!!');window.location='/admin_manage_product';</script>")
    
    q=product.objects.all()

    return render(request,'admin_manage_product.html',{'q':q,'q1':q1,'d':d})




def admin_view_products(request):

    q=product.objects.all()


    q=product.objects.all()
    if q:
        for i in q:
            st=int(i.stock)
            pid=i.id
            print(st,"___________")
            amt=i.rate

            if st<=10:
                print("hello..........................")
                print(st,"____________***********")
                print(pid,"%%%%%%%%%%%%%%%%%")
                print(amt,"%%%%%%%%%%%%%%%%%")
                return HttpResponse("<script>alert('Send Stock Request......!');window.location='admin_send_stock_request/%s/%s/%s';</script>" % (st,pid,amt))
    return render(request,'admin_view_products.html',{'q':q})




def admin_send_stock_request(request,st,pid,amt):
    today=date.today()
    print(today)

    if request.method=="POST":
        qu=request.POST['qu']
        rate=request.POST['rate']
        tt=request.POST['tt']
        n=requests.objects.filter(date=today,product_id=pid)
        if n:
            return HttpResponse("<script>alert('Already Exist....!!!');window.location='/adminhome';</script>")
        else:
            q=requests(qty=qu,date=today,amount=tt,rstatus='pending',product_id=pid)
            q.save()
            return HttpResponse("<script>alert('Requested....!!!');window.location='/adminhome';</script>")
    return render(request,'admin_send_stock_request.html',{'amt':amt})




def admin_delete_product(request,id):
    q=product.objects.get(id=id)
    q.delete()
    return HttpResponse("<script>alert('Removed....!!!');window.location='/admin_manage_product';</script>")




def admin_update_product(request,id):
    up=product.objects.get(id=id)

    if request.method=="POST":
        pro=request.POST['pro']
        rt=request.POST['rate']
        qu=request.POST['qu']
        des=request.POST['des']
        up.product_name=pro 
        up.rate=rt 
        up.stock=qu 
        up.p_description=des
        up.save()
        return HttpResponse("<script>alert('Updated...!!!');window.location='/admin_manage_product';</script>")
    return render(request,'admin_manage_product.html',{'up':up})




def admin_view_bookings(request):
    q=booking.objects.all()
    print(q)
    return render(request,'admin_view_bookings.html',{'q':q})



def admin_view_cart_product(request,id):
    print("hhhhhhhhhhhhhhhhhhhhhhhhhhhhh")
    q=bookingchild.objects.filter(booking_id=id)
    if q:
        omtotal=q[0].booking.total 
        print(omtotal,">>>>>>>>>>>>>>>>>>>>>>total")
    return render(request,'admin_view_cart_product.html',{'q':q,'omtotal':omtotal})


def admin_view_payments(request,id):
    q=booking.objects.filter(id=id)
    print(q)
    print("______________________________________")
    return render(request,'admin_view_payments.html',{'q':q})



def admin_update_status(request,id):
    lgs=booking.objects.get(id=id)
    lgs.status="Delivered"
    lgs.save()
    return HttpResponse("<script>alert('Delivered....!!!!');window.location='/admin_view_bookings';</script>")


def admin_view_company(requset):
    ss=dealer.objects.all()
    return render(requset,'admin_view_company.html',{'ss':ss})


def admin_accept_dealer(request,id):
    lgs=login.objects.get(id=id)
    lgs.usertype="dealer"
    lgs.save()
    return HttpResponse("<script>alert('Accepted....!!!!');window.location='/admin_view_company';</script>")

def admin_reject_dealer(requset,id):
    lgs=login.objects.get(id=id)
    lgs.usertype="Reject"
    lgs.save()
    return HttpResponse("<script>alert('Rejected....!!!!');window.location='/admin_view_company';</script>")
################################################# dealer ################################################

def dealer_home(request):
    return render(request,'dealer_home.html')



def dealer_view_request(request):
    lid=request.session['login_id']

    c=dealer.objects.filter(login_id=lid)
    if c:
        did=c[0].id 
        print(did)

    q=requests.objects.filter(product__dealer_id=did)
    return render(request,'dealer_view_request.html',{'q':q})




def dealer_update_stock(request,id,qty,rid):
    qty=int(qty)
    print(qty,"________________")

    q=product.objects.get(id=id)
    if q:
        stock=int(q.stock)
        print(stock,"****************")

        q.stock=stock+qty 
        q.save()

        q1=requests.objects.get(id=rid)
        q1.rstatus='Stock Added'
        q1.save()
        return HttpResponse("<script>alert('Stock Added');window.location='/dealer_view_request';</script>")
    return render(request,'dealer_view_request.html')
################################################# user ################################################


def user_home(request):
    q1=product.objects.all()
    return render(request,'user_home.html',{'q1':q1})



def user_view_products(request):
    ss={}
    q1=product.objects.all()

    if request.method=='POST':
        pla=request.POST['pla']
        
        q1=product.objects.filter(product_name=pla)|product.objects.filter(category__category=pla)
        print(q1,"$$$$$$$$$$$$$$$$$$$$$$$$$$")

    ss['q1']=q1
    return render(request,'user_view_products.html',ss)


def user_view_more_details(request,id):
    q1=product.objects.filter(id=id)
    return render(request,'user_view_more_details.html',{'q1':q1})



def user_add_product_to_carts(request,pid,pname,rate,quantity):

    today=date.today()
    print(today)

    lid=request.session['login_id']

    c=user.objects.filter(login_id=lid)
    if c:
        cid=c[0].id 
        print(cid)


    if request.method=="POST":
        qty=request.POST['qty']
        amount=request.POST['amount']
        ttotal=request.POST['total']

        if int(qty)<=int(quantity):
            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            q=booking.objects.filter(user_id=cid,status='pending')
            if q:
                oid=q[0].id
                total=q[0].total
                print("omaster_id...............",oid)
                print("total...............",total)


                q2=bookingchild.objects.filter(booking=oid,product_id=pid)
                if q2:
                    od_id=q2[0].id
                    t_qty=q2[0].quantity 
                    t_amt=q2[0].amount
                    print("odetail_id......",od_id)
                    print("t_qty........",t_qty)
                    print("t_amt........",t_amt)


                    c=int(t_qty)+int(qty)

                    if int(c)>int(quantity):
                        return HttpResponse("<script>alert('OUT OF STOCK');window.location='/user_home';</script>")
                    
                    else:
                        oup=bookingchild.objects.get(id=od_id)
                        oup.amont=int(t_amt)+int(ttotal)
                        oup.qty=int(t_qty)+int(qty)
                        oup.save()

                        up=booking.objects.get(id=oid)
                        up.total=int(total)+int(ttotal)
                        up.save() 

                else:
                    q3=bookingchild(amount=ttotal,quantity=qty,booking_id=oid,product_id=pid)
                    q3.save()
                    up1=booking.objects.get(id=oid)
                    up1.total=int(total)+int(ttotal)
                    up1.save() 
                    return HttpResponse("<script>alert('Booked....!!');window.location='/user_home';</script>")
            
            else:
                oid=booking(total=ttotal,date=today,status='pending',order_id='0',user_id=cid)
                oid.save()
                q3=bookingchild(amount=ttotal,quantity=qty,booking=oid,product_id=pid)
                q3.save()
                return HttpResponse("<script>alert('Booked....!!');window.location='/user_home';</script>")
           
        else:
            return HttpResponse("<script>alert('Enter Less Quantity....!!');window.location='/user_home';</script>")
    
    ss={}
    
    ss['pname']=pname
    ss['rate']=rate
    return render(request,'user_add_product_to_carts.html',ss)



def user_view_cart(request):
    lid=request.session['login_id']

    c=user.objects.filter(login_id=lid)
    if c:
        cid=c[0].id 
        print(cid)

    q=booking.objects.filter(user=cid,status ='pending')
    print(q)
    
    
    ss={}
    lid=request.session['login_id']
    print(lid)
    ss['q']=q
    return render(request,'user_view_cart.html',ss)



def user_view_cart_product(request,id):
    q=bookingchild.objects.filter(booking_id=id)
    if q:
        omtotal=q[0].booking.total 
        print(omtotal,">>>>>>>>>>>>>>>>>>>>>>total")
        st=q[0].booking.status 
        print(st,">>>>>>>>>>>>>>>>>>>>>>status")
        oid=q[0].booking.id 
        print(oid,">>>>>>>>>>>>>>>>>>>>>>omaster_id")
        od_qty=q[0].quantity 
        print(od_qty,">>>>>>>>>>>>>>>>>>>>>>odetail_qty")
    
    
    ss={}
   
    ss['q']=q
    ss['omtotal']=omtotal
    ss['st']=st
    ss['oid']=oid
    ss['od_qty']=od_qty
    
    return render(request,'user_view_cart_product.html',ss)


def user_make_payment(request,id,total):
    today=date.today()
    print(today)
    print(">>>>>>>>>>>>>>>>",total)


    # if request.method=="POST":
    #     amount = total
    #     currency="INR"

    #         # Create Razorpay client object

    #     razorpay_client = Client(auth=("rzp_test_myOF7jDpkIqeD0", "lGAkCY9inaIl4fS1apPqP7Gi"))

    #         # Create a payment
    #     order = razorpay_client.order.create({
    #         "amount": amount,
    #         "currency": currency,
    #         'receipt': 'receipt_id'
    #     })

    #     # Get the order ID
    #     order_id = order['id']
    #     print(order_id)
    #     s=booking.objects.get(id=id)
    #     if s:
    #         s.status='Paid'
    #         s.order_id=order_id
    #         s.save() 
    #     od=bookingchild.objects.filter(booking_id=id)
    #     print(od)
    #     if od:
    #         for i in od:
    #             pid=i.product_id
    #             qtys=i.quantity
    #             print(pid,"....................proid")
    #             print(qtys,"..................qty")

    #             pp=product.objects.get(id=pid)
    #             # print(p,"!!!!!!!!!!!!!!!!!!!!!!!!")
    #             if pp:
    #                 pro_qty=pp.stock
    #                 print(pro_qty,"############pro_qty")
    #                 pp.stock=int(pro_qty)-int(qtys)
    #                 pp.save()
    #        # return HttpResponse("<script>alert('Payment Completed....!!!');window.location='/customer_view_order_history/';</script>")
   
    ss={}
   
    ss['total']=total
    return render(request,'user_make_payment.html',{'total':total})


def user_view_order_history(request):
    lid=request.session['login_id']

    c=user.objects.filter(login_id=lid)
    if c:
        cid=c[0].id 
        print(cid)

    q=booking.objects.filter(user=cid,status ='Paid')|booking.objects.filter(user=cid,status ='Delivered')
    print(q)
    print("______________________________________")


    ss={}
    lid=request.session['login_id'] 
    print(lid)
    
    ss['q']=q
    return render(request,'user_view_order_history.html',ss)



def user_view_cart_history_product(request,id):
    q=bookingchild.objects.filter(booking_id=id)
    if q:
        omtotal=q[0].booking.total 
        print(omtotal,">>>>>>>>>>>>>>>>>>>>>>total")
        st=q[0].booking.status 
        print(st,">>>>>>>>>>>>>>>>>>>>>>status")
        oid=q[0].booking.id 
        print(oid,">>>>>>>>>>>>>>>>>>>>>>omaster_id")
        od_qty=q[0].quantity 
        print(od_qty,">>>>>>>>>>>>>>>>>>>>>>odetail_qty")
    
    
    ss={}
    lid=request.session['login_id']
    print(lid)
    
    ss['q']=q
    ss['omtotal']=omtotal
    ss['st']=st
    ss['oid']=oid
    ss['od_qty']=od_qty
    return render(request,'user_view_cart_history_product.html',ss)


def user_view_payment_details(request,id):
    q=booking.objects.filter(id=id)
    print(q)
    print("______________________________________")


    ss={}
    lid=request.session['login_id']
    print(lid)
    ss['q']=q
    return render(request,'user_view_payment_details.html',ss)