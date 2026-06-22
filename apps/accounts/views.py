from django.shortcuts import (
render,
redirect
)

from django.contrib.auth import (
login,
logout,
authenticate
)

from .forms import (
RegisterForm,
LoginForm
)


def register_view(
request
):

    if request.method=="POST":

        form=RegisterForm(
            request.POST
        )

        if form.is_valid():

            user=form.save()

            login(
                request,
                user
            )

            return redirect(
                '/'
            )

    return redirect('/')



def login_view(
request
):

    if request.method=="POST":

        email=request.POST.get(
            'username'
        )

        password=request.POST.get(
            'password'
        )

        user=authenticate(
            request,
            username=email,
            password=password
        )

        if user:

            login(
                request,
                user
            )

    return redirect('/')



def logout_view(
request
):

    logout(
        request
    )

    return redirect('/')