from django.db import models
from seller.models import *
from datetime import datetime
from django.contrib.auth.models import User


class BuyerRegistration(models.Model):
    user = models.AutoField(primary_key=True)
    user_address = models.TextField(max_length=255)
    user_photo = models.ImageField(default='default.jpg', upload_to='buyer/', null=True)
    user_mobile_no = models.CharField(max_length=12, unique=True, default=None, null=True)
    buyer = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.buyer)

    class Meta:
        db_table = "Buyer_Registration"


class BuyerCart(models.Model):
    Cart = models.AutoField(primary_key=True)
    cart_qty = models.PositiveIntegerField(default=0)
    cart_date_added = models.DateTimeField(auto_now_add=True)
    cart_total = models.IntegerField(default=0)
    cart_product_color = models.CharField(max_length=50, null=True)
    cart_product_size = models.CharField(max_length=50, null=True)
    cart_status = models.BooleanField(default=True)
    cart_product = models.ForeignKey("seller.Product", on_delete=models.CASCADE)
    cart_buyer = models.ForeignKey(BuyerRegistration, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.Cart)
    class Meta:
        db_table = "Buyer_Cart"


class BuyerCheckout_details(models.Model):
    address = models.AutoField(primary_key=True)
    checkout_street_address = models.CharField(max_length=100)
    checkout_apartment_address = models.CharField(max_length=100)
    checkout_pincode = models.IntegerField()
    checkout_city = models.CharField(max_length=100)

    SELECT_STATE = (
        ('State Name', 'Andhra Pradesh'), ('State Name', 'Arunachal Pradesh'), ('State Name', 'Assam'),
        ('State Name', 'Bihar'), ('State Name', 'Chhattisgarh'), ('State Name', 'Goa'),
        ('State Name', 'Gujarat'), ('State Name', 'Haryana'), ('State Name', 'Himachal Pradesh'),
        ('State Name', 'Jharkhand'), ('State Name', 'Karnataka'), ('State Name', 'Kerala'),
        ('State Name', 'Madhya Pradesh'), ('State Name', 'Maharashtra'), ('State Name', 'Manipur'),
        ('State Name', 'Meghalaya'), ('State Name', 'Mizoram'), ('State Name', 'Nagaland'),
        ('State Name', 'Odisha'), ('State Name', 'Punjab'), ('State Name', 'Rajasthan'),
        ('State Name', 'Sikkim'), ('State Name', 'Tamil Nadu'), ('State Name', 'Telangana'),
        ('State Name', 'Tripura'), ('State Name', 'Uttar Pradesh'), ('State Name', 'Uttarakhand'),
        ('State Name', 'West Bengal'), ('State Name', 'Andaman and Nicobar Islands'), ('State Name', 'Chandigarh'),
        ('State Name', 'Dadra & Nagar Haveli and Daman & Diu'), ('State Name', 'Delhi'),
        ('State Name', 'Jammu and Kashmir'),
        ('State Name', 'Lakshadweep'), ('State Name', "Pondicherry"), ('State Name', "Ladakh"),
    )
    checkout_select_state = models.CharField(max_length=40, choices=SELECT_STATE)
    checkout_ord_rec_name = models.CharField(max_length=255)
    checkout_ord_rec_mobile_no = models.CharField(max_length=12)
    checkout_status = models.BooleanField(default=True)
    checkout_cart = models.ForeignKey(BuyerCart, on_delete=models.CASCADE, null=True)
    checkout_buyer = models.ForeignKey(BuyerRegistration, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.checkout_buyer)

    class Meta:
        db_table = "Buyer_Checkout_details"


def __str__(self):
    return str(self.cart_buyer)


class BuyerPurchase(models.Model):
    purchase = models.AutoField(primary_key=True)
    purchase_total = models.IntegerField(default=0)
    purchase_qty = models.PositiveIntegerField(default=0)
    purchase_product = models.ForeignKey("seller.Product", on_delete=models.CASCADE)
    purchase_buyer = models.ForeignKey(BuyerRegistration, on_delete=models.CASCADE)
    purchase_cart = models.ForeignKey(BuyerCart, on_delete=models.CASCADE, null=True)
    purchase_checkout = models.ForeignKey(BuyerCheckout_details, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.purchase_buyer) + " " + str(self.purchase_product)

    class Meta:
        db_table = "Buyer_Purchase"


class BuyerPayment(models.Model):
    payment = models.AutoField(primary_key=True)
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('success', 'Success'),
        ('failed', 'Failed'),
    ]

    payment_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_currency = models.CharField(max_length=3, default='IND')
    payment_status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    payment_intent_id = models.CharField(max_length=50)
    payment_created_at = models.DateTimeField(auto_now_add=True)
    payment_updated_at = models.DateTimeField(auto_now=True)
    payment_order_key = models.CharField(max_length=100, null=True)
    payment_cancel = models.BooleanField(default=True)
    payment_details = models.ForeignKey(BuyerPurchase, on_delete=models.CASCADE)
    payment_buyer = models.ForeignKey(BuyerRegistration, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.payment_amount} {self.payment_currency} "

    class Meta:
        db_table = "Buyer_Payment"


class BuyerFeedback(models.Model):
    feedback = models.AutoField(primary_key=True)
    feedback_description = models.TextField(max_length=500, null=False)
    feedback_datetime = models.DateTimeField(auto_now_add=True)
    feedback_rating = models.IntegerField(null=False)
    feedback_photo = models.FileField(upload_to='buyer/', null=True)
    feedback_product = models.ForeignKey("seller.Product", on_delete=models.CASCADE)
    feedback_login = models.ForeignKey(BuyerRegistration, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.feedback} - {self.feedback_description}"

    class Meta:
        db_table = "Buyer_feedback"


class BuyerReturn(models.Model):
    order_return = models.AutoField(primary_key=True)
    returns = models.CharField(max_length=100)
    order_return_message = models.CharField(max_length=100, null='N/A')
    return_shipping_Fee = models.IntegerField(default=0)
    return_date = models.DateTimeField(null=True, default=datetime.now)
    return_status = models.BooleanField(default=True)
    return_buyer = models.ForeignKey(BuyerRegistration, on_delete=models.CASCADE)
    return_order = models.ForeignKey(BuyerPayment, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.return_order} {self.return_buyer}"

    class Meta:
        db_table = "Buyer_Return"


class Payment(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    razorpay_payment_id = models.CharField(max_length=100)

# class Order(models.Model):
#     order_product = models.CharField(max_length=100)
#     order_amount = models.CharField(max_length=25)
#     order_payment_id = models.CharField(max_length=100)
#     isPaid = models.BooleanField(default=False)
#     order_date = models.DateTimeField(auto_now=True)
#
#     def __str__(self):
#         return self.order_product