from django.contrib import admin

from .models import *



@admin.register(BuyerRegistration)
class BuyerRegistrationadmin(admin.ModelAdmin):
    list_display = ['user', 'user_address', 'user_mobile_no', 'user_photo', 'buyer']



@admin.register(BuyerCheckout_details)
class BuyerAddressadmin(admin.ModelAdmin):
    list_display = ["address", "checkout_street_address", "checkout_apartment_address", "checkout_pincode", "checkout_city", "checkout_select_state", "checkout_ord_rec_name",
                "checkout_ord_rec_mobile_no", "checkout_buyer"]


@admin.register(BuyerCart)
class BuyerCartadmin(admin.ModelAdmin):
    list_display = ["Cart", "cart_buyer", "cart_product", "cart_qty", "cart_date_added", "cart_total"]


@admin.register(BuyerPurchase)
class BuyerPurchaseadmin(admin.ModelAdmin):
    list_display = ["purchase", "purchase_buyer", "purchase_qty", "purchase_product", "purchase_total", "purchase_cart", "purchase_checkout"]




@admin.register(BuyerFeedback)
class BuyerFeedbackadmin(admin.ModelAdmin):
  list_display = ["feedback", "feedback_description", "feedback_datetime", "feedback_rating", "feedback_photo",
                "feedback_product", "feedback_login"]



@admin.register(BuyerPayment)
class BuyerPaymentadmin(admin.ModelAdmin):
    list_display = ["payment", "payment_status", "payment_amount", "payment_currency", "payment_order_key", "payment_intent_id", "payment_created_at",
                    "payment_updated_at", "payment_cancel", "payment_details", "payment_buyer"]




@admin.register(BuyerReturn)
class Returnadmin(admin.ModelAdmin):
    list_display = ["order_return", "returns", "order_return_message", "return_shipping_Fee", "return_date", "return_status",
                    "return_buyer", "return_order"]
