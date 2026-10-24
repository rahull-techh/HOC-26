from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password




@csrf_exempt
def register(request):

    if request.method != "POST":
        return JsonResponse({
            "message":"POST method required"
        }, status=405)


    name = request.POST.get("name")
    number = request.POST.get("number")
    st_id = request.POST.get("st_id")
    uni_id = request.POST.get("uni_id")
    gender = request.POST.get("gender")
    year = request.POST.get("year")
    branch = request.POST.get("branch")
    residence = request.POST.get("residence")
    email = request.POST.get("email")
    password = request.POST.get("password")


    if not (('@' in password or '$' in password) and password.isalnum()):
        return JsonResponse({"error": "Password is weak use '@','$' and numbers to create a strong password"})

    if not name or not email or not password or not number or not st_id or not uni_id or not gender or not year or not branch or not residence:
        return JsonResponse({
            "error": "All fields  are required"
        },status=400)

    try:
        EmailValidator()(email)
    except ValidationError:
        return JsonResponse({
            "error":"Enter a Valid email"
        }, status=400)

    if User.objects.filter(email=email).exists():
        return JsonResponse({
            "error":"Email already exist"
        },status=400)
    if User.objects.filter(st_id=st_id).exists():
        return JsonResponse({
            "error":"Student already registered"
        }, status=400)
    if User.objects.filter(uni_id= uni_id).exists():
        return JsonResponse({"message":"Student already registered"}, status=400)

    hashed_password = make_password(password)

    user = User.objects.create(
        name = name,
        number = number,
        student_id = st_id,
        uni_roll = uni_id,
        branch = branch,
        email = email,
        password = hashed_password,
        gender = gender,
        residence = residence,
        year = year,
    )

    return JsonResponse({"message":"Registration successfull"}, status= 200)

    