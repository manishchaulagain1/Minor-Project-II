from django.db import models

# Create your models here.
import uuid

class PaymentGateway(models.Model):
    token = models.UUIDField(default= uuid.uuid4,editable=False)
    expiry_date = models.DateField()
    balance = models.FloatField()
    is_active = models.BooleanField()