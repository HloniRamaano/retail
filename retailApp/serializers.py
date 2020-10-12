from rest_framework import serializers
from . models import Product, ShoppingCart, Payment, Account

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class ShoppingCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoppingCart
        fields = '__all__'

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'
        
        
#Account api

class accountsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id','firstname', 'lastname','email', 'username', 'date_joined',
                    'last_login', 'is_admin', 'is_staff']
        

class AccountSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type':'password'}, write_only=True)
    
    class Meta:
        model = Account
        fields = ['firstname','lastname','username','email', 'password','password2']
        extra_kwargs = {
            'password':{'write_only':True}
        }
    def save(self):
        account = Account(
            firstname = self.validated_data['firstname'],
            lastname = self.validated_data['lastname'],
            email=self.validated_data['email'],
            username=self.validated_data['username']
            )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        
        if password != password2:
            raise serializers.ValidationError({'password':'Password must match'})
        account.set_password(password)
        account.save()
        return account