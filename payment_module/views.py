# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import PaymentGateway
from datetime import date
from django.db import transaction
from django.urls import reverse
from app.models import UserCourse, Course

# Create your views here.
def confirmpayment(request,slug):
    if request.method == "POST":
        token = request.POST.get("token")
        amount = request.POST.get("amount")

        # clean up
        token = token.strip()
        amount = float(amount)

        try:
            with transaction.atomic():
                # open an atomic transaction, i.e. all successful or none
                make_payment(token, amount)

        except Exception as e:
            request.session["message"] = str(e)
            return redirect(reverse('error_page'))

        else:
            course = Course.objects.get(slug = slug)
    
            course = UserCourse(
                user = request.user,
                course = course,
            )

            course.save()

            request.session["message"] = f"Payment successfully completed with NRs. {amount} from your balance!"
            return redirect(reverse('success_page'))

def make_payment(token, amount):
    try:
        payment_gateway = PaymentGateway.objects.get(token=token)
    except:
        raise Exception(f"Invalid token")

    # Check if available amount is sufficient for payment
    if payment_gateway.balance < amount:
        raise Exception("Insufficient balance")

    # check for expiry date
    if payment_gateway.expiry_date < date.today():
        raise Exception("Token has expired")

    # deduct amount and save
    payment_gateway.balance -= amount
    payment_gateway.save()







