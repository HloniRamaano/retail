from django.contrib import admin
from . models import Product, ShoppingCart,Payment,Account
from django.contrib.auth.admin import UserAdmin

class AccountAdmin(UserAdmin):
    list_display = ('firstname', 'lastname','email', 'username', 'date_joined',
                    'last_login', 'is_admin', 'is_staff')
    
    search_fields = ('email', 'username',)
    readonly_fields = ('date_joined', 'last_login')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(Account, AccountAdmin)
admin.site.register(Product)
admin.site.register(ShoppingCart)
admin.site.register(Payment)


