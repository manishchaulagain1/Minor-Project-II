from django.contrib import admin

# Register your models here.
from .models import PaymentGateway
class PaymentGatewayAdmin(admin.ModelAdmin):
    list_display = ["token", "balance", "expiry_date", "is_active",]

    class Meta:
        model = PaymentGateway

admin.site.register(PaymentGateway, PaymentGatewayAdmin)