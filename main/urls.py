from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
   path('',views.home),
    # path('about',views.about),
    # path('products',views.products),
    path('logins',views.logins),
    path('user_register',views.user_register),
    path('dealer_register',views.dealer_register),


    
    path('adminhome',views.adminhome),
    path('admin_view_user',views.admin_view_user),
    path('admin_view_company',views.admin_view_company),
    path('admin_accept_dealer/<id>',views.admin_accept_dealer),
    path('admin_reject_dealer/<id>',views.admin_reject_dealer),
    path('admin_manage_category',views.admin_manage_category),
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



    path('dealer_home',views.dealer_home),
    path('dealer_view_request',views.dealer_view_request),
    path('dealer_update_stock/<id>/<qty>/<rid>',views.dealer_update_stock),


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
]
