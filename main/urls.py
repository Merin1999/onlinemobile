from django.contrib import admin
from django.urls import path,include

# Create your views here.
from . import views


urlpatterns = [
    path('',views.home),
    path('about',views.about),
    path('public_view_products/<id>',views.public_view_products),
    path('loginss',views.loginss),
    path('user_register',views.user_register),
    path('dealer_register',views.dealer_register),
    path('sales_report',views.sales_report),
    path('admin_remove_subcategory/<id>',views.admin_remove_subcategory),
    


    path('adminhome',views.adminhome),
    path('admin_view_company',views.admin_view_company),
    path('admin_view_user',views.admin_view_user),
    path('admin_manage_category',views.admin_manage_category),
    path('admin_manage_sub_category',views.admin_manage_sub_category),
    
    path('admin_remove_category/<id>',views.admin_remove_category),
    path('admin_manage_product',views.admin_manage_product),
    path('admin_update_product/<id>',views.admin_update_product),
    path('admin_delete_product/<id>',views.admin_delete_product),  
    path('admin_view_bookings',views.admin_view_bookings),
    path('admin_view_cart_product/<id>',views.admin_view_cart_product),
    path('admin_view_payments/<id>',views.admin_view_payments),
    path('admin_update_status/<id>',views.admin_update_status),
    path('admin_view_products',views.admin_view_products),
    path('admin_send_stock_request/<st>/<pid>/<amt>',views.admin_send_stock_request),
    path('admin_manage_ram',views.admin_manage_ram),
    path('admin_manage_rom',views.admin_manage_rom),
    path('rpay',views.rpay,name='rpay'),
    path('user_payment_complete/<id>',views.user_payment_complete),
    path('customer_remove_cart_product/<odid>/<oid>',views.customer_remove_cart_product),
    path('user_buy_product/<id>/<rate>',views.user_buy_product),
    path('admin_send_stock_request/<st>/<pid>/<amt>',views.admin_send_stock_request),





    path('forgot',views.forgot), 
    path('newpas',views.newpas),  
    path('otp',views.otp,name='otp'),


    path('dealer_home',views.dealer_home),
    path('dealer_view_request',views.dealer_view_request),
    path('dealer_update_stock/<id>/<qty>/<rid>',views.dealer_update_stock),

    path('admin_accept_dealer/<id>',views.admin_accept_dealer),   
    path('admin_reject_dealer/<id>',views.admin_reject_dealer), 


    path('user_home',views.user_home),
    path('user_view_products',views.user_view_products),
    path('user_view_more_details/<id>',views.user_view_more_details),
    path('user_add_product_to_carts/<pid>/<pname>/<rate>/<quantity>',views.user_add_product_to_carts),
    path('user_view_cart',views.user_view_cart),
    path('user_view_cart_product/<id>',views.user_view_cart_product),
    path('user_make_payment/<id>/<total>',views.user_make_payment),
    path('user_view_order_history',views.user_view_order_history),
    path('user_view_cart_history_product/<id>',views.user_view_cart_history_product),
    path('user_view_payment_details/<id>',views.user_view_payment_details),

    path('user_change_password',views.user_change_password),
    path('patient_set_password',views.patient_set_password),
    path('dealer_change_password',views.dealer_change_password),
    path('dealer_set_password',views.dealer_set_password),
    path('dealer_manage_product',views.dealer_manage_product),
    path('customer_add_ratings/<id>',views.customer_add_ratings),
    path('dealer_manage_product',views.dealer_manage_product),
    path('customer_update_profile',views.customer_update_profile),
    path('customer_edit_profile/<id>',views.customer_edit_profile),
    path('acceptcustomer_username/<id>',views.acceptcustomer_username),
    path('admin_remove_subcategory/<id>',views.admin_remove_subcategory),
    path('admin_remove_rom/<id>',views.admin_manage_rom),
    path('admin_remove_ram/<id>',views.admin_manage_ram),
    path('customer_add_ratings/<id>',views.customer_add_ratings),

    path('admin_accept_request/<id>',views.admin_accept_request),   
    path('admin_reject_request/<id>',views.admin_reject_request), 
    path('admin_view_request',views.admin_view_request),
    path('admin_make_payment/<id>/<total>',views.admin_make_payment),
    path('admin_payment_complete/<id>',views.admin_payment_complete),
     path('dealer_update_product/<id>',views.dealer_update_product),
    path('dealer_delete_product/<id>',views.dealer_delete_product),  

    path('admin_view_rating',views.admin_view_rating),
    path('generate_payment_invoice/<id>',views.generate_payment_invoice),
    # path('admin_payment_complete/<id>',views.admin_payment_complete),
    
    

    
    

]