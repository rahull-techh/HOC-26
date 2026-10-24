from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


def home(request):
    return JsonResponse({
        "message": "Welcome to HOUR OF CODE",
        "user": str(request.user),
        "authenticated": request.user.is_authenticated,
    })

@csrf_exempt
def register(request):

    if request.method != "POST":
        return JsonResponse({
            "message": "POST request required"
        }, status=405)


    name = request.POST.get("name")
    number = request.POST.get("number")
    st_id = request.POST.get("")
    username = request.POST.get("username")
    email = request.POST.get("email")
    password = request.POST.get("password")   

    if not (('@' in password or '$' in password) and password.isalnum()):
        return JsonResponse({"error": "Password is weak use '@','$' and numbers to create a strong password"})

    if not number.isdigits():
        return JsonResponse({
            "error":"Enter a valid Mobile Number"
        },status=400)

    if 10<len(number)<10:
        return JsonResponse({
            "error":"Enter a valid 10 digit number"
        },status=400)

    if not name or not username or not email or not password or not number:
        return JsonResponse({
            "error": "All fields  are required"
        },status=400)

    try:
        validate_email(email)
    except ValidationError:
        return JsonResponse({
            "error":"Enter a Valid email"
        }, status=400)

    if User.objects.filter(email=email).exists():
        return JsonResponse({
            "error":"Email already exist"
        },status=400)