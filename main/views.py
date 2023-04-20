from django.shortcuts import render,HttpResponse
from main.models import *
from django.core.files.storage import FileSystemStorage
from datetime import date,datetime 
from django.conf import settings
from django.core.mail import send_mail
import random
from datetime import datetime, timedelta
import razorpay
from razorpay import Client

# Create your views here.

################################################# public #########################################
def home(request):
    q=category.objects.all()
    print(q)
    q1=product.objects.all()
    print(q1,"**********************")
   
    return render(request,'home.html',{'q':q})


def about(request):
    return render(request,'about.html')



def public_view_products(request,id):
    q1=product.objects.filter(id=id)
    print(q1,"**********************")
    if request.method=='POST':
        pla=request.POST['pla']
        
        q1=product.objects.filter(product_name=pla)|product.objects.filter(category__category=pla)
        print(q1,"$$$$$$$$$$$$$$$$$$$$$$$$$$")
    return render(request,'public_view_products.html',{'q1':q1})



def loginss(request):
    if request.method=="POST":
        uname=request.POST['uname']
        pwd=request.POST['pwd']
        print(uname,pwd)
        
        try:
            lg=login.objects.get(username=uname,password=pwd)
            print(lg,"........................")
   
            request.session['login_id']=lg.pk
            if lg.usertype=='admin':
               
                return HttpResponse("<script>alert('Welcome Admin......!');window.location='adminhome';</script>")
            elif lg.usertype=='user':
                return HttpResponse("<script>alert('Welcome User......!');window.location='user_home';</script>")
            elif lg.usertype=='dealer':
                de=dealer.objects.get(login_id=lg.pk)
                request.session['dealer_id']=de.id
                return HttpResponse("<script>alert('Welcome Dealer......!');window.location='dealer_home';</script>")
      
        except:
            return HttpResponse("<script>alert('login Failed...!!!!');window.location='loginss';</script>")
    return render(request,'login.html')




def user_register(request):
    if request.method=="POST":
        fn=request.POST['fn']
        ln=request.POST['ln']
        pl=request.POST['pl']
        ph=request.POST['ph']
        em=request.POST['em']
        pwd=request.POST['pwd']
        pin=request.POST['pin']
        
        print(fn,ln,pl,ph,em,em,pwd)
        q=login.objects.filter(username=em)
        if q:
            return HttpResponse("<script>alert('Username Already Exist....!!!');window.location='user_register';</script>")
        else:
            lg=login(username=em,password=pwd,usertype='pending')
            lg.save()
            pt=user(fname=fn,lname=ln,place=pl,phone=ph,pincode=pin,email=em,login=lg)
            pt.save()
            subject = 'Confirmation Link'
            message = f"Sir/Madam,\n Your <a href=http://127.0.0.1:8000/acceptcustomer_username/{lg.id}>verify</a>"
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [em, ]
            send_mail( subject, message, email_from, recipient_list )
            return HttpResponse("<script>alert('Added Successfully....!!!');window.location='user_register';</script>")
    return render(request,'user_reg.html')


def acceptcustomer_username(request,id):
    cus=login.objects.get(id=id)
    cus.usertype='user'
    cus.save()
    return HttpResponse("<script>alert('Verified');window.location='/loginss'</script>")


def forgot(request):
    if request.method=="POST":
        unamee=request.POST['uname']
        phone=request.POST['ph']
        ob=login.objects.get(username=unamee)
        print("###################################")
        print(ob)
        if ob:
            request.session['llid']=ob.pk
            utype=ob.usertype
            if utype=="user":
                ob1=user.objects.filter(phone=phone,login_id=ob.pk)
                if ob1: 
                    import random
                    number = random.randint(1111,9999)
                    request.session['otp']=number
                    print(number)        
                    for i in ob1:
                        print(i.email)
                        subject = 'One Time Password'
                        message = f"sir,\n One Time Password :"+ str(number)
                        email_from = settings.EMAIL_HOST_USER
                        recipient_list = [unamee, ]
                        send_mail( subject, message, email_from, recipient_list )
                            
                        return HttpResponse('''<script>alert("mail sended");window.location='otp'</script>''')
            elif utype=="dealer":
                ob1=dealer.objects.filter(phone=phone,login_id=ob.pk)
                if ob1: 
                    import random
                    number = random.randint(1111,9999)
                    request.session['otp']=number
                    print(number)        
                    for i in ob1:
                        print(i.email)
                        subject = 'One Time Password'
                        message = f"sir,\n One Time Password :"+ str(number)
                        email_from = settings.EMAIL_HOST_USER
                        recipient_list = [unamee, ]
                        send_mail( subject, message, email_from, recipient_list )
                            
                        return HttpResponse('''<script>alert("mail sended");window.location='otp'</script>''')
            else:
                return HttpResponse('''<script>alert("Invalid Details");window.location='/loginss'</script>''') 
    return render(request,'forgotpass.html')  



def otp(request):
    # print("##############")
    if request.method=="POST":
        otpnum=int(request.POST['otpp'])
        # print("SSSS : ",otpnum)

        ottp=int(request.session['otp'])
        # print("*****************")
        # print("UUUUUUUUUUU",ottp)
        if ottp==otpnum:
            # print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            return HttpResponse('''<script>alert("Success");window.location='newpas'</script>''') 

    return render(request, 'optmsg.html') 


def newpas(request):
    lo=login.objects.get(pk=request.session['llid'])
    if request.method=="POST":
        npass=request.POST['passw']
        cpass=request.POST['cpassw']
       
        lo.password=npass
        lo.save()
        return HttpResponse('''<script>alert("confirm");window.location='/'</script>''')   
    return render(request, 'newpass.html')  

def dealer_register(request):
    if request.method=="POST":
        com=request.POST['com']
        pl=request.POST['pl']
        ph=request.POST['ph']
        em=request.POST['em']
        pwd=request.POST['pwd']
        # print(fn,ph,em,em,pwd)
        q=login.objects.filter(username=em)
        if q:
            return HttpResponse("<script>alert('Username Already Exist....!!!');window.location='dealer_register';</script>")
        else:
            lg=login(username=em,password=pwd,usertype='pending')
            lg.save()
            pt=dealer(company_name=com,place=pl,phone=ph,email=em,login=lg)
            pt.save()
            return HttpResponse("<script>alert('Added Successfully....!!!');window.location='dealer_register';</script>")
    return render(request,'dealer_register.html')


################################################# admin #######################################################

def adminhome(request):
    cuser=user.objects.all().count()

    pro=product.objects.all().count()

    ord=booking.objects.all().count()

    return render(request,'adminhome.html',{'cuser':cuser,'pro':pro,'ord':ord})



def admin_view_user(request):
    q=user.objects.all()
    return render(request,'admin_view_users.html',{'q':q})


def admin_view_company(requset):
    ss=dealer.objects.all()
    return render(requset,'admin_view_company.html',{'ss':ss})
    

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


def admin_manage_ram(request):
    if request.method=="POST":
        rams=request.POST['ram']
        q=ramss.objects.filter(rams=rams)
        if q:
             return HttpResponse("<script>alert('Already Exist....!!!');window.location='/admin_manage_ram';</script>")
        else:
            lg=ramss(rams=rams)
            lg.save()
            return HttpResponse("<script>alert('Added Successfully....!!!');window.location='/admin_manage_ram';</script>")

    q=ramss.objects.all()
    return render(request,'admin_manage_ram.html',{'q':q})


def admin_remove_ram(request,id):
    q=ramss.objects.filter(id=id)
    q.delete()
    return HttpResponse("<script>alert('Removed...!!!');window.location='/admin_manage_ram';</script>")



def admin_manage_rom(request):
    if request.method=="POST":
        rams=request.POST['ram']
        q=romss.objects.filter(roms=rams)
        if q:
             return HttpResponse("<script>alert('Already Exist....!!!');window.location='/admin_manage_rom';</script>")
        else:
            lg=romss(roms=rams)
            lg.save()
            return HttpResponse("<script>alert('Added Successfully....!!!');window.location='/admin_manage_rom';</script>")

    q=romss.objects.all()
    return render(request,'admin_manage_rom.html',{'q':q})


def admin_remove_ram(request,id):
    q=romss.objects.filter(id=id)
    q.delete()
    return HttpResponse("<script>alert('Removed...!!!');window.location='/admin_manage_ram';</script>")


def admin_remove_category(request,id):
    q=category.objects.filter(id=id)
    q.delete()
    return HttpResponse("<script>alert('Removed...!!!');window.location='/admin_manage_category';</script>")




def admin_remove_subcategory(request,id):
    q=sub_category.objects.filter(id=id)
    q.delete()
    return HttpResponse("<script>alert('Removed...!!!');window.location='/admin_manage_subcategory';</script>")






def admin_manage_product(request):
    from datetime import date,datetime
    today=date.today()
    print(today) 
    lid=request.session['login_id']

    d=dealer.objects.all()

    q2=ramss.objects.all()
    q3=romss.objects.all()
    if 'submit' in request.POST:

        dea=request.POST['dea']
        pro=request.POST['pro']
        img=request.FILES['img']
        rt=request.POST['rate']
        qu=request.POST['qu']  
        des=request.POST['des']
        cat=request.POST['cat']
        ram=request.POST['ram']
        print(ram)
        rom=request.POST['rom']
        fs=FileSystemStorage()
        vv=fs.save(img.name,img)
        q=product(product_name=pro,rate=rt,stock=qu,image=vv,p_description=des,sub_category_id=cat,dealer_id=dea,ram_id=ram,rom_id=rom)
        q.save()
        return HttpResponse("<script>alert('Added Successfully....!!!');window.location='/admin_manage_product';</script>")
    
    q=product.objects.all()

    q1=sub_category.objects.all()


    if 'search' in request.POST:
        pla=request.POST['pla']
        
        q=product.objects.filter(sub_category__category__category=pla)|product.objects.filter(sub_category__subcategory=pla)
        print(q,"$$$$$$$$$$$$$$$$$$$$$$$$$$")
    
    
    return render(request,'admin_manage_product.html',{'q':q,'q1':q1,'q3':q3,'d':d,'today':str(today),'q2':q2})



def admin_view_products(request):

    q=product.objects.filter(stock__lte=5)


    # q=product.objects.all()
    # if q:
    #     for i in q:
    #         st=int(i.stock)
    #         pid=i.id
    #         print(st,"___________")
    #         amt=i.rate

    #         if st<=10:
    #             print("hello..........................")
    #             print(st,"____________***********")
    #             print(pid,"%%%%%%%%%%%%%%%%%")
    #             print(amt,"%%%%%%%%%%%%%%%%%")
    #             return HttpResponse("<script>alert('Send Stock Request......!');window.location='admin_send_stock_request/%s/%s/%s';</script>" % (st,pid,amt))
    return render(request,'admin_view_products.html',{'q':q})




def admin_send_stock_request(request,st,pid,amt):
    today=date.today()
    print(today)
    q=product.objects.get(id=pid)
    print(q,"___________")

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
    return render(request,'admin_send_stock_request.html',{'amt':amt,'q':q})



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
    q=payment.objects.filter(booking_id=id)
    print(q)
    print("______________________________________")
    return render(request,'admin_view_payments.html',{'q':q})



def admin_update_status(request,id):
    lgs=booking.objects.get(id=id)
    lgs.status="Delivered"
    lgs.save()
    return HttpResponse("<script>alert('Delivered....!!!!');window.location='/admin_view_bookings';</script>")



# @login_required(login_url='loginss')
def admin_accept_dealer(request,id):
    lgs=login.objects.get(id=id)
    lgs.usertype="dealer"
    lgs.save()
    q=dealer.objects.get(login_id=id)
    if q:
        em=q.email 
        print(em)

    
    subject = 'Notification'
    message = f"sir,\n You Are Accepted By Admin \n"
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [em, ]
    send_mail( subject, message, email_from, recipient_list )
    return HttpResponse("<script>alert('Accepted....!!!!');window.location='/admin_view_company';</script>")


# @login_required(login_url='loginss')
def admin_reject_dealer(requset,id):
    lgs=login.objects.get(id=id)
    lgs.usertype="Reject"
    lgs.save()
    q=dealer.objects.get(login_id=id)
    if q:
        em=q.email 
        print(em)

    
    subject = 'Notification'
    message = f"sir,\n You Are Rejected By Admin \n"
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [em, ]
    send_mail( subject, message, email_from, recipient_list )
    return HttpResponse("<script>alert('Rejected....!!!!');window.location='/admin_view_company';</script>")



################################################# dealer ################################################

def dealer_home(request):
    lid=request.session['login_id']

    c=dealer.objects.get(login_id=lid)
    return render(request,'dealer_home.html',{'name':c.company_name})



def dealer_view_request(request):
    lid=request.session['login_id']

    c=dealer.objects.filter(login_id=lid)
    if c:
        did=c[0].id 
        print(did)

    q=requests.objects.filter(product__dealer_id=did)
    print(q)
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
    from datetime import date 
    today=date.today()
    q=category.objects.all()
    print(q) 

    q1=product.objects.all()
    print(q1,"**********************")

    lid=request.session['login_id']

    c=user.objects.filter(login_id=lid)
    if c:
        cid=c[0].id 
        print(cid)

    if 'filter' in request.POST:
        amount=request.POST['amount']
        amt=int(amount)
        q1 = product.objects.filter(rate__lte=amt)

    if 'ser' in request.POST:
        pla=request.POST['pla']
        
        q1=product.objects.filter(product_name=pla)|product.objects.filter(sub_category__subcategory=pla)
        print(q1,"$$$$$$$$$$$$$$$$$$$$$$$$$$")

        if q1:
            pid=q1[0].id 
            print(pid,"++++++++++++++++++++")
            q=history.objects.filter(user_id=cid,product_id=pid)
            if not q:
                q7=history(user_id=cid,product_id=pid,date=today)
                q7.save()

        #print(q1,"$$$$$$$$$$$$$$$$$$$$$$$$$$")
    q4=history.objects.filter(user_id=cid).order_by('-id')
    return render(request,'user_home.html',{'q1':q1,'q4':q4})



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
                        oup.amount=int(t_amt)+int(ttotal)
                        oup.quantity=int(t_qty)+int(qty)
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




def rpay(request):
    print("Haiiiiiiiii")
    
    

    # Get the order ID
    order_id = request.GET['order_id']
    order_id = request.GET['order_id']
    print(order_id)
    s=booking.objects.get(id=id)
    if s:
        s.status='Shipped'
        s.order_id=order_id
        s.save() 
    od=bookingchild.objects.filter(booking_id=id)
    print(od)
    if od:
        for i in od:
            pid=i.product_id
            qtys=i.quantity
            print(pid,"....................proid")
            print(qtys,"..................qty")

            pp=product.objects.get(id=pid)
            # print(p,"!!!!!!!!!!!!!!!!!!!!!!!!")
            if pp:
                pro_qty=pp.stock
                print(pro_qty,"############pro_qty")
                pp.stock=int(pro_qty)-int(qtys)
                pp.save()
    return HttpResponse("<script>alert('Payment Completed....!!!');window.location='/user_home';</script>")
   
    return render(request, 'orders.html',context)

def user_payment_complete(request,id):

    # print(order_id)
    s=booking.objects.get(id=id)
    if s:
        s.status='Shipped'
        s.order_id=id
        s.save() 
    od=bookingchild.objects.filter(booking_id=id)
    print(od)
    if od:
        for i in od:
            pid=i.product_id
            qtys=i.quantity
            print(pid,"....................proid")
            print(qtys,"..................qty")

            pp=product.objects.get(id=pid)
            # print(p,"!!!!!!!!!!!!!!!!!!!!!!!!")
            if pp:
                pro_qty=pp.stock
                print(pro_qty,"############pro_qty")
                pp.stock=int(pro_qty)-int(qtys)
                pp.save()
    return HttpResponse("<script>alert('Payment Completed....!!!');window.location='/user_home';</script>")


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
    #         s.status='Shipped'
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
    #     return HttpResponse("<script>alert('Payment Completed....!!!');window.location='/user_home';</script>")
   
    ss={}
   
    ss['total']=total
    return render(request,'user_make_payment.html',{'total':total,'ids':id})




def customer_remove_cart_product(request,odid,oid):
    
    print(odid,"___________________")
    print(oid,"*****************")
    q=bookingchild.objects.get(id=odid)
    if q:
        oamt=q.amount
        q.delete()

        up=booking.objects.get(id=oid)
        if up:
            up.total=int(up.total)-int(oamt)
            up.save()
            q=booking.objects.get(id=oid)
            if q:
                tot=up.total
                print(tot,"__________________")
                if int(tot) == 0:
                    q1=booking.objects.get(id=oid)
                    q1.delete()
        
    return HttpResponse("<script>alert('Removed....!!');window.location='/user_view_cart';</script>")


def user_view_order_history(request):
    lid=request.session['login_id']

    c=user.objects.filter(login_id=lid)
    if c:
        cid=c[0].id 
        print(cid)

    q=booking.objects.filter(user=cid,status ='Shipped')|booking.objects.filter(user=cid,status ='Delivered')
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


# @login_required(login_url='loginss')
def user_change_password(request):
    lid=request.session['login_id']
    if request.method=="POST":
        un=request.POST['un']
        pwd=request.POST['pwd']
        q=login.objects.get(username=un)
        print(q)
        if q:
            print("!!!!!!!!!!!!!!!!!!!!!")
            return HttpResponse("<script>window.location='/patient_set_password';</script>")
        else:
            return HttpResponse("<script>alert('Invalid Username Or Password');window.location='/user_change_password';</script>")
    return render(request,'user_change_password.html')


# @login_required(login_url='loginss')
def patient_set_password(request):
    lid=request.session['login_id']
    if request.method=="POST":
        psw=request.POST['psw']
        cpsw=request.POST['cpsw']
        if psw!=cpsw:
            return HttpResponse("<script>alert('Check Password...!!!!');window.location='/patient_change_password'</script>")
        else:
            q=login.objects.get(id=lid)
            q.password=psw 
            q.save()
            return HttpResponse("<script>alert('Password changed...!!!!');window.location='/loginss'</script>")
    return render(request,'patient_set_password.html')



def dealer_change_password(request):
    lid=request.session['login_id']
    if request.method=="POST":
        un=request.POST['un']
        pwd=request.POST['pwd']
        q=login.objects.get(username=un)
        print(q)
        if q:
            print("!!!!!!!!!!!!!!!!!!!!!")
            return HttpResponse("<script>window.location='/dealer_set_password';</script>")
        else:
            return HttpResponse("<script>alert('Invalid Username Or Password');window.location='/dealer_change_password';</script>")
    return render(request,'dealer_change_password.html')


# @login_required(login_url='loginss')
def dealer_set_password(request):
    lid=request.session['login_id']
    if request.method=="POST":
        psw=request.POST['psw']
        cpsw=request.POST['cpsw']
        if psw!=cpsw:
            return HttpResponse("<script>alert('Check Password...!!!!');window.location='/dealer_change_password'</script>")
        else:
            q=login.objects.get(id=lid)
            q.password=psw 
            q.save()
            return HttpResponse("<script>alert('Password changed...!!!!');window.location='/loginss'</script>")
    return render(request,'dealer_set_password.html')


def customer_add_ratings(request,id):
    today=date.today()
    print(today)

    lid=request.session['login_id']

    c=user.objects.filter(login_id=lid)
    if c:
        cid=c[0].id 
        print(cid)


    if request.method=="POST":
        rate=request.POST['r']
        re=request.POST['review']
        q=review(rate=rate,reviews=re,date=today,user_id=cid,product_id=id)
        q.save()
        return HttpResponse("<script>alert('Added....!!!');window.location='/user_home';</script>")
    ss={}
    lid=request.session['login_id']
    print(lid)

    return render(request,'customer_add_ratings.html',ss)


def dealer_manage_product(request):
    from datetime import date,datetime
    today=date.today()
    print(today) 
    lid=request.session['login_id']
    c=dealer.objects.filter(login_id=lid)
    if c:
        did=c[0].id 
        print(did)

    d=dealer.objects.all()

    q1=category.objects.all()
    if request.method=="POST":
        pro=request.POST['pro']
        img=request.FILES['img']
        rt=request.POST['rate']
        qu=request.POST['qu']  
        des=request.POST['des']
        cat=request.POST['cat']
        # date=request.POST['date']
        fs=FileSystemStorage()
        vv=fs.save(img.name,img)
        q=product(product_name=pro,rate=rt,stock=qu,image=vv,p_description=des,category_id=cat,dealer_id=request.session['dealer_id'])
        q.save()
        return HttpResponse("<script>alert('Added Successfully....!!!');window.location='/dealer_manage_product';</script>")
    
    q=product.objects.filter(dealer_id=did)

    return render(request,'dealer_manage_product.html',{'q':q,'q1':q1,'d':d,'today':str(today)})


def customer_update_profile(request):
    lid=request.session['login_id']
    print(lid)
    
    q1=user.objects.filter(login_id=lid)
    print(q1)

    ss={}
    lid=request.session['login_id']
    print(lid)
    

    
    ss['q1']=q1
    return render(request,'customer_update_profile.html',ss)


def customer_edit_profile(request,id):
    lid=request.session['login_id']
    print(lid)

    up=user.objects.get(login_id=lid)
    print(up)

    if request.method=="POST":
       fn=request.POST['fn']
       ln=request.POST['ln']
       ph=request.POST['ph']
       em=request.POST['em'] 
       up.fname=fn 
       up.lname=ln 
       up.phone=ph 
       up.emil=em 
       up.save()
       return HttpResponse("<script>alert('Updated....!!');window.location='/customer_update_profile'</script>")
    
    ss={}
    lid=request.session['login_id']
    print(lid)
   
    ss['up']=up
    return render(request,'customer_update_profile.html',ss)

def customer_remove_cart_product(request,odid,oid):
    
    print(odid,"___________________")
    print(oid,"*****************")
    q=bookingchild.objects.get(id=odid)
    if q:
        oamt=q.amount
        q.delete()

        up=booking.objects.get(id=oid)
        if up:
            up.total=int(up.total)-int(oamt)
            up.save()
            q=booking.objects.get(id=oid)
            if q:
                tot=up.total
                print(tot,"__________________")
                if int(tot) == 0:
                    q1=booking.objects.get(id=oid)
                    q1.delete()
        
    return HttpResponse("<script>alert('Removed....!!');window.location='/user_view_cart';</script>")


# @login_required(login_url='loginss')
def user_change_password(request):
    lid=request.session['login_id']
    if request.method=="POST":
        un=request.POST['un']
        pwd=request.POST['pwd']
        q=login.objects.get(username=un)
        print(q)
        if q:
            print("!!!!!!!!!!!!!!!!!!!!!")
            return HttpResponse("<script>window.location='/patient_set_password';</script>")
        else:
            return HttpResponse("<script>alert('Invalid Username Or Password');window.location='/user_change_password';</script>")
    return render(request,'user_change_password.html')



def sales_report(request):
    q=booking.objects.all()

    if request.method=="POST":
        sd=request.POST['sd']
        ed=request.POST['ed']
        q = booking.objects.filter(date__range=[sd, ed])
        print(q,"__________________")


    return render(request,'sales_report.html',{'q':q})




def admin_manage_sub_category(request):
    q1=category.objects.all()
    if request.method=="POST":
        cat=request.POST['cat']
        scat=request.POST['scat']
        q=sub_category.objects.filter(subcategory=scat)
        if q:
             return HttpResponse("<script>alert('Already Exist....!!!');window.location='/admin_manage_sub_category';</script>")
        else:
            lg=sub_category(category_id=cat,subcategory=scat)
            lg.save()
            return HttpResponse("<script>alert('Added Successfully....!!!');window.location='/admin_manage_sub_category';</script>")

    q=sub_category.objects.all()
    return render(request,'admin_mange_subcategory.html',{'q':q,'q1':q1})


def generate_payment_invoice(request,id):
    number=random.randint(1000,9999)
    print(number)

    q=booking.objects.filter(id=id)
    if q:
        amt=q[0].total
    q2=bookingchild.objects.filter(booking_id=id)
    
    return render(request,'generate_payment_invoice.html',{'number':number,'q':q,'q2':q2,'amt':amt})

def admin_remove_subcategory(request,id):
    q=sub_category.objects.filter(id=id)
    q.delete()
    return HttpResponse("<script>alert('Removed...!!!');window.location='/admin_manage_sub_category';</script>")



def user_buy_product(request,id,rate):
    from datetime import date
    today=date.today()
    lid=request.session['login_id']

    c=user.objects.filter(login_id=lid)
    if c:
        cid=c[0].id 
        print(cid)


   

    oid=booking(total=rate,date=today,status='pending',order_id='0',user_id=cid)
    oid.save()
    q3=bookingchild(amount=rate,quantity='1',booking=oid,product_id=id)
    q3.save()
    return HttpResponse("<script>alert('Booked....!!');window.location='/user_make_payment/%s/%s';</script>"% (id,rate))



def admin_accept_request(request,id):
    lgs=requests.objects.get(id=id)
    lgs.rstatus="Accepted"
    lgs.save()
    q=login.objects.get(usertype='admin')
    if q:
        em=q.username 
        print(em)

    
    subject = 'Notification'
    message = f"sir,\n Your Stock Request Accepted \n"
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [em, ]
    send_mail( subject, message, email_from, recipient_list )
    return HttpResponse("<script>alert('Accepted....!!!!');window.location='/dealer_view_request';</script>")


# @login_required(login_url='loginss')
def admin_reject_request(requset,id):
    lgs=requests.objects.get(id=id)
    lgs.rstatus="Rejected"
    lgs.save()
    q=dealer.objects.get(login_id=id)
    if q:
        em=q.username 
        print(em)

    
    subject = 'Notification'
    message = f"sir,\n Your Stock Request Accepted \n"
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [em, ]
    send_mail( subject, message, email_from, recipient_list )
    return HttpResponse("<script>alert('Rejected....!!!!');window.location='/dealer_view_request';</script>")


def admin_view_request(request):
    q=requests.objects.all()
    return render(request,'admin_view_request.html',{'q':q})




def admin_payment_complete(request,id):

    # print(order_id)
    s=requests.objects.get(id=id)
    if s:
        s.rstatus='paid'
        s.save() 
    return HttpResponse("<script>alert('Payment Completed....!!!');window.location='/adminhome';</script>")


def admin_make_payment(request,id,total):
    from datetime import datetime,date
    today=date.today()
    print(today)
    print(">>>>>>>>>>>>>>>>",total)


    # s=booking.objects.get(id=id)
    # if s:
    #     s.status='Shipped'
    #     s.order_id=order_id
    #     s.save() 
    # od=bookingchild.objects.filter(booking_id=id)
    # print(od)
    # if od:
    #     for i in od:
    #         pid=i.product_id
    #         qtys=i.quantity
    #         print(pid,"....................proid")
    #         print(qtys,"..................qty")

    #         pp=product.objects.get(id=pid)
    #         # print(p,"!!!!!!!!!!!!!!!!!!!!!!!!")
    #         if pp:
    #             pro_qty=pp.stock
    #             print(pro_qty,"############pro_qty")
    #             pp.stock=int(pro_qty)-int(qtys)
    #             pp.save()



    # if request.method=="POST":
        # q=payment(amount=total,date=today,booking_id=id)
        # q.save()
        # amount = total
        # currency="INR"

        #     # Create Razorpay client object

        # razorpay_client = Client(auth=("rzp_test_myOF7jDpkIqeD0", "lGAkCY9inaIl4fS1apPqP7Gi"))

        #     # Create a payment
        # order = razorpay_client.order.create({
        #     "amount": amount,
        #     "currency": currency,
        #     'receipt': 'receipt_id'
        # })

        # # Get the order ID
        # order_id = order['id']
        # print(order_id)
        # s=booking.objects.get(id=id)
        # if s:
        #     s.status='Shipped'
        #     s.order_id=order_id
        #     s.save() 
        # od=bookingchild.objects.filter(booking_id=id)
        # print(od)
        # if od:
        #     for i in od:
        #         pid=i.product_id
        #         qtys=i.quantity
        #         print(pid,"....................proid")
        #         print(qtys,"..................qty")

        #         pp=product.objects.get(id=pid)
        #         # print(p,"!!!!!!!!!!!!!!!!!!!!!!!!")
        #         if pp:                              
        #             pro_qty=pp.stock
        #             print(pro_qty,"############pro_qty")
        #             pp.stock=int(pro_qty)-int(qtys)
        #             pp.save()
        # return HttpResponse("<script>alert('Payment Completed....!!!');window.location='/user_home';</script>")
   
    ss={}
   
    ss['total']=total
    return render(request,'admin_make_payment.html',{'total':total,'ids':id})



def dealer_delete_product(request,id):
    q=product.objects.get(id=id)
    q.delete()
    return HttpResponse("<script>alert('Removed....!!!');window.location='/dealer_manage_product';</script>")




def dealer_update_product(request,id):
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
        return HttpResponse("<script>alert('Updated...!!!');window.location='/dealer_manage_product';</script>")
    return render(request,'dealer_manage_product.html',{'up':up})




def admin_view_rating(request):
    q=review.objects.all()
    return render(request,'admin_view_rating.html',{'q':q})