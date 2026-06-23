from django.shortcuts import (
    redirect,
    render
)

from django.contrib.auth import (
    login,
    logout,
    authenticate
)

from django.contrib.auth.models import User

from .models import UserProfile



# -------------------
# EMAIL VERIFY
# -------------------

def verify_email(
    request,
    token
):

    try:

        profile = UserProfile.objects.get(
            verification_token=token
        )

        profile.email_verified = True

        profile.save()

    except:

        pass


    return redirect('/')



# -------------------
# LOGOUT
# -------------------

def logout_view(
    request
):

    logout(request)

    return redirect('/')



# -------------------
# LOGIN
# -------------------

def login_view(
    request
):

    if request.method == "POST":

        username = request.POST.get(
            "username"
        )

        password = request.POST.get(
            "password"
        )


        user = authenticate(

            request,

            username=username,

            password=password

        )


        if user:

            login(

                request,

                user

            )


    return redirect('/')



# -------------------
# REGISTER
# -------------------

def register_view(
    request
):

    if request.method == "POST":

        username = request.POST.get(
            "username"
        )

        email = request.POST.get(
            "email"
        )

        password = request.POST.get(
            "password"
        )


        if not User.objects.filter(
            username=username
        ).exists():

            user = User.objects.create_user(

                username=username,

                email=email,

                password=password

            )

            UserProfile.objects.create(

                user=user

            )


    return redirect('/')