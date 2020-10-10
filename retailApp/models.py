from django.db import models

class Product(models.Model):
    product_id = models.CharField(max_length=100)
    name = models.CharField(max_length = 200)
    price = models.FloatField()
    description = models.TextField()
    category = models.CharField(max_length = 200)

    def __str__(self):
        return self.name

class ShoppingCart(models.Model):
    product_id = models.CharField(max_length=100)
    name = models.CharField(max_length = 200)
    price = models.FloatField()
    quantity = models.IntegerField()

    def __str__(self):
        return self.name

class Payment(models.Model):
    
    name = models.CharField(max_length = 200)
    bank_name = models.CharField(max_length = 200)	#First National Bank (FNB)
    account_name = models.CharField(max_length = 200)	#Unisa Student Fees Account
    account_number = models.CharField(max_length = 200)	#627 9963 0382
    account_type = models.CharField(max_length = 200)	#Cheque
    branch_code = models.CharField(max_length = 200)	#210554
    reference = models.CharField(max_length = 200)
    amount = models.FloatField()

    def __str__(self):
        return self.reference