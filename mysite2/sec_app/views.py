from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from sec_app.forms import mat_mov, UserForm, UserProfileInfoForm
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from django.db import transaction
from sec_app.signals import send_verification_emails
from django.shortcuts import get_object_or_404
from sec_app.models import Movement
def index(request):
    return render(request, 'sec_app/index.html')

def users(request):
    form = mat_mov()

    if request.method == "POST":
        form = mat_mov(request.POST)

        if form.is_valid():
            with transaction.atomic():
                instance = form.save(commit=False)
                instance.save()
            send_verification_emails(sender=instance.__class__, instance=instance)

            return index(request)
        else:
            print("Invalid form!!!")

    return render(request, 'sec_app/forms_page.html', {'form': form})

def register(request):
    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'sec_app/registration.html',
                  {'user_form':user_form,
                   'profile_form':profile_form,
                   'registered':registered})

@login_required
def special(request):
    return HttpResponse("you ae logged in!")

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('user_login'))

def user_login(request):
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('sec_app:index'))
            else:
                return HttpResponse("account not active!!")
        else:
            print("someone tried to login and failed")
            return HttpResponse("invalid login")
    else:
        return render(request, 'sec_app/login.html', {})

def verify_action(request, movement_id):
    # Retrieve the Movement instance to verify
    movement = get_object_or_404(Movement, pk=movement_id)

    # Implement your verification logic here
    # For example, update the status field or perform other actions

    # Redirect to a success or confirmation page
    return render(request, 'verify_success.html')

def reject_action(request, movement_id):
    # Retrieve the Movement instance to reject
    movement = get_object_or_404(Movement, pk=movement_id)

    # Implement your rejection logic here
    # For example, update the status field or perform other actions

    # Redirect to a success or confirmation page
    return render(request, 'reject_success.html')
