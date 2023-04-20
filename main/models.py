from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class login(models.Model):
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=1000)
    usertype=models.CharField(max_length=50)

class user(models.Model):
    login=models.ForeignKey(login,on_delete=models.CASCADE)
    fname=models.CharField(max_length=50)
    lname=models.CharField(max_length=50)
    place=models.CharField(max_length=50)
    phone=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    pincode=models.CharField(max_length=50)


class dealer(models.Model):
    login=models.ForeignKey(login,on_delete=models.CASCADE)
    company_name=models.CharField(max_length=50)
    place=models.CharField(max_length=50)
    phone=models.CharField(max_length=50)
    email=models.CharField(max_length=50)

class category(models.Model):
    category=models.CharField(max_length=50)


class sub_category(models.Model):
    category=models.ForeignKey(category,on_delete=models.CASCADE)
    subcategory=models.CharField(max_length=50)


class ramss(models.Model):
    rams=models.CharField(max_length=50)

class romss(models.Model):
    roms=models.CharField(max_length=50)


class product(models.Model):
    ram=models.ForeignKey(ramss,on_delete=models.CASCADE)
    rom=models.ForeignKey(romss,on_delete=models.CASCADE)
    sub_category=models.ForeignKey(sub_category,on_delete=models.CASCADE)
    dealer=models.ForeignKey(dealer,on_delete=models.CASCADE)
    product_name=models.CharField(max_length=50)
    rate=models.IntegerField(max_length=50)
    stock=models.IntegerField(max_length=50)
    image=models.CharField(max_length=1000)
    p_description=models.CharField(max_length=1000)


class requests(models.Model):
    product=models.ForeignKey(product,on_delete=models.CASCADE)
    qty=models.CharField(max_length=50)
    date=models.CharField(max_length=50)
    amount=models.CharField(max_length=50)
    rstatus=models.CharField(max_length=50)


class booking(models.Model):
    user=models.ForeignKey(user,on_delete=models.CASCADE)
    total=models.CharField(max_length=50)
    date=models.CharField(max_length=50)
    status=models.CharField(max_length=50)
    order_id=models.CharField(max_length=50)

class bookingchild(models.Model):
    booking=models.ForeignKey(booking,on_delete=models.CASCADE)
    product=models.ForeignKey(product,on_delete=models.CASCADE)
    quantity=models.CharField(max_length=50)
    amount=models.CharField(max_length=50)

class payment(models.Model):
    booking=models.ForeignKey(booking,on_delete=models.CASCADE)
    amount=models.CharField(max_length=50)
    date=models.CharField(max_length=50)

  
class review(models.Model):
    user=models.ForeignKey(user,on_delete=models.CASCADE)
    product=models.ForeignKey(product,on_delete=models.CASCADE)
    rate=models.CharField(max_length=50)
    reviews=models.CharField(max_length=50)
    date=models.CharField(max_length=50)



class history(models.Model):
    user=models.ForeignKey(user,on_delete=models.CASCADE)
    product=models.ForeignKey(product,on_delete=models.CASCADE)
    date=models.CharField(max_length=50)
